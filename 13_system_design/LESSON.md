# 13 · System Design

> A system design interview is not a test of whether you know Kafka. It is a test of whether
> you can turn "build Twitter" into a set of numbers, a handful of boxes, and a defended
> choice between two reasonable options. The candidate who says "it depends, and here is what
> it depends on" beats the one who recites an architecture.

**Who this is for:** SDE2 / L4 and above. Amazon gives SDE1 candidates a light version at most
(often an object-oriented design question instead), and Google does not ask L3 candidates
system design at all. If you are a new grad, read sections 1, 3, and 5, skim the rest, and
spend the time on chapters 14 and 15. If you are L4+ or SDE2+, this round can fail your loop
by itself. Give it the full week.

## 1. What the round is and how it is graded

You get one vague prompt ("design a URL shortener", "design the Amazon order history page")
and 45 to 60 minutes. There is no single right answer. The interviewer writes notes on roughly
six things:

| Signal | What the interviewer is checking |
|--------|----------------------------------|
| **Requirements gathering** | Did you ask before you drew? Did you separate functional from non-functional? Did you narrow scope on purpose? |
| **Estimation** | Can you produce QPS, storage, and bandwidth from a few assumptions, and do the numbers then drive the design? |
| **High-level design** | Are the boxes right? Does every arrow have a reason? Could a team build from this? |
| **Deep dive** | When pushed on one component, can you go two levels deeper: data layout, failure modes, what breaks at 10x? |
| **Trade-offs** | Did you name at least one alternative for each big decision and say why you did not pick it? |
| **Communication** | Did you drive the conversation, check in, and adjust when the interviewer redirected you? |

**Amazon** grades this round against the bar for the level and also listens for Leadership
Principles: Customer Obsession (did you start from the user?), Frugality (did you avoid
over-building?), Dive Deep (the deep-dive section), Are Right, A Lot (defended judgment). The
interviewer often has a specific real Amazon system in mind and will steer you toward the
part they care about. Follow the steer.

**Google** grades on a rubric that mostly matches the table above and cares more about
estimation and about scaling behavior: "what happens at 100x?" is guaranteed. Google
interviewers tend to give less direction and want to see you drive. Silence from them is not
disapproval. Keep going, but check in every few minutes.

Both companies fail candidates for the same three reasons: drawing before asking, never
producing a number, and never saying the word "alternatively."

## 2. The 45-minute protocol

Use the same shape every time so you never have to think about what comes next.

| Minutes | Phase | Output on the whiteboard |
|---------|-------|--------------------------|
| 0–5 | Clarify requirements | Two short lists: functional, non-functional. Explicit out-of-scope list. |
| 5–10 | Estimate | QPS (read and write), storage over 5 years, bandwidth. Three or four lines. |
| 10–15 | API and data model | 3–5 endpoints. Main tables or key-value shapes. |
| 15–25 | High-level diagram | Client → LB → services → caches → DBs → queues. Every arrow labeled. |
| 25–38 | Deep dive | One or two components at depth. This is where hire/no-hire is decided. |
| 38–43 | Trade-offs and scaling | "At 10x I would..."; failure modes; what you would change with more time. |
| 43–45 | Wrap | Summarize. Ask what they would have pushed on. |

If the interviewer pulls you into a deep dive early, go. The budget is a default, not a law.

### 2.1 Clarifying questions (minutes 0–5)

Say: "Before I draw anything, let me pin down what we are building and for whom." Then ask,
in this order:

**Functional**
- Who are the users, and what are the 2–3 core actions? ("Create a short link; follow it.")
- What is explicitly out of scope? (Analytics? Custom aliases? Editing?)
- Read-heavy or write-heavy? What is the ratio? (Usually 10:1 to 100:1 for consumer systems.)
- Any special data: files, media, location, real-time?

**Non-functional**
- Scale: how many users, daily active, requests per second?
- Latency target: is 200 ms fine, or do we need under 50 ms?
- Consistency: if a user writes and reads back immediately, must they see it? (This one
  question decides half your database choices.)
- Availability: 99.9% (8.7 hours down per year) or 99.99% (52 minutes)?
- Durability: can we ever lose a write?
- Geography: one region or global?

Then say the scope back: "So: shorten, redirect, 100M new links a month, reads 100x writes,
redirect under 100 ms, we can tolerate a few seconds of staleness. Analytics out of scope."
Write that on the board. You will refer to it.

### 2.2 Back-of-envelope estimation (minutes 5–10)

Interviewers do not care if you are off by 3x. They care that you can get within an order of
magnitude in two minutes and that the number then changes a decision ("that fits on one
machine, so I will not shard yet").

**Numbers to memorize**

| Fact | Value | Use |
|------|-------|-----|
| Seconds per day | 86,400 ≈ 10^5 (use 100,000) | Daily volume ÷ 10^5 = average QPS |
| Seconds per month | ≈ 2.5 × 10^6 | Monthly volume to QPS |
| Peak vs average | 2–5x average; say 3x | Size for peak |
| 1 ASCII char | 1 byte | URL, username, tweet sizes |
| Small text record (ID, timestamps, few fields) | ~100 bytes to 1 KB | Row-size guesses |
| Photo | ~200 KB to 2 MB; say 500 KB | Blob storage |
| Minute of video | ~50 MB at HD | Bandwidth |
| 2^10 / 2^20 / 2^30 / 2^40 | KB / MB / GB / TB (thousand, million, billion, trillion) | Convert |
| Base-62 characters | 62^6 ≈ 5.7 × 10^10, 62^7 ≈ 3.5 × 10^12 | ID length |

**Latency numbers everyone quotes (Jeff Dean's table, rounded)**

| Operation | Time |
|-----------|------|
| L1 cache reference | ~1 ns |
| Main memory reference | ~100 ns |
| Compress 1 KB | ~2 µs |
| Read 1 MB sequentially from memory | ~10 µs |
| SSD random read | ~100 µs |
| Read 1 MB from SSD | ~1 ms |
| Round trip inside one datacenter | ~0.5 ms |
| Disk (HDD) seek | ~10 ms |
| Read 1 MB from HDD | ~20 ms |
| Round trip California ↔ Netherlands | ~150 ms |

The lesson from the table: memory beats SSD by 1,000x, SSD beats disk by 100x, and a
cross-continent hop costs more than any local operation. Caching is not an optimization; it is
the design.

**One-machine rule of thumb**

- A stateless web server handles ~1,000 to 10,000 simple requests per second. Say 1,000 for
  anything that touches a database.
- A single well-tuned relational database handles ~1,000 to 10,000 writes per second and
  perhaps 10,000 to 50,000 simple indexed reads.
- A Redis node handles ~100,000 simple operations per second.
- A single machine stores a few TB on disk comfortably, and 64 to 512 GB in memory.

So: under 1,000 QPS and under 1 TB, you do not need to shard. Say so. Interviewers respect
"one Postgres with a read replica is enough for this; here is when it stops being enough."

**Worked estimate: URL shortener**

```
Writes:  100M new links / month ÷ (2.5 × 10^6 s) ≈ 40 writes/s   (peak ~120/s)
Reads:   100 : 1 ratio                              ≈ 4,000 reads/s  (peak ~12,000/s)
Storage: 100M links/month × 500 bytes × 12 × 5 yr    ≈ 3 TB over 5 years
Bandwidth (reads): 4,000/s × 500 bytes               ≈ 2 MB/s. Trivial.
Cache:   80/20 rule. 20% of daily reads = 0.2 × 4,000 × 86,400 × 500 B ≈ 35 GB. Fits in one Redis.
```

Say the conclusion out loud: "Writes are tiny; reads matter. The whole hot set fits in a
cache. The design is a read-through cache in front of a key-value store."

### 2.3 API sketch (minutes 10–12)

Three to five endpoints. REST is fine unless the interviewer wants gRPC. Include the shape of
the request and response and note what is idempotent.

```
POST /v1/links          body: { long_url, custom_alias?, expires_at? }   → { short_code }
GET  /{short_code}      → 301/302 redirect to long_url
DELETE /v1/links/{code} (auth required)
```

Mention: pagination on list endpoints, auth headers, rate limits, and that redirects should be
302 (not cached by browsers) if you want analytics, 301 if you want to shed load.

### 2.4 Data model (minutes 12–15)

Write the main entity as a table or a key-value shape. Name the primary key and the one or two
indexes you need.

```
links:  short_code (PK, 7 chars) | long_url (text) | user_id | created_at | expires_at
index on user_id if "list my links" is in scope
```

Then say which store. "This is a key lookup by short_code with no joins. A key-value store
(DynamoDB, Cassandra) or Postgres both work. I will pick DynamoDB for horizontal scaling; if
the interviewer prefers relational, Postgres with a single index is fine at this scale."

### 2.5 High-level diagram (minutes 15–25)

Draw left to right. Label every arrow with the protocol or purpose. Start simple, then add
components one at a time, saying why each one exists.

```
 client ──HTTPS──▶ [ DNS / CDN ] ──▶ [ Load balancer ]
                                          │
                              ┌───────────┴───────────┐
                              ▼                       ▼
                       [ API service ]  ...    [ API service ]   (stateless, N copies)
                              │                       │
                    ┌─────────┴──────────┐            │
                    ▼                    ▼            ▼
              [ Redis cache ]      [ DB primary ] ──▶ [ read replicas ]
                                          │
                                          ▼
                                   [ message queue ] ──▶ [ async workers: analytics, cleanup ]
```

Talk through one request path end to end: "A GET hits the LB, an API node checks Redis, on a
miss reads the DB, writes back to Redis with a TTL, and returns a 302."

### 2.6 Deep dive (minutes 25–38)

The interviewer picks, or you offer: "The two interesting parts are ID generation and the
cache. Which would you like me to go deeper on?" Then go two levels down:

- Data layout inside the component. Keys, partitions, indexes.
- Failure modes. What happens when this node dies? When it is slow? When it fills up?
- Scaling. What changes at 10x and 100x?
- Consistency. Where can two users see different answers, and is that acceptable?

### 2.7 Trade-offs and wrap (minutes 38–45)

For every major choice, one sentence of "alternatively": "I chose fan-out on write for the
feed; alternatively, fan-out on read avoids the celebrity problem at the cost of slower reads.
A hybrid is what production systems do." Then: bottlenecks, single points of failure,
monitoring, and what you would build first if you had two weeks.

## 3. Building blocks

Each block below is three to six lines: what it is, when to reach for it, and the sentence to
say in the room.

**Load balancer.** Distributes requests across N identical servers. Layer 4 (TCP) is fast and
dumb; layer 7 (HTTP) can route on path or header. Algorithms: round robin, least connections,
consistent hashing for sticky routing. It also does health checks and removes dead nodes.
Say: "An LB in front of stateless API nodes gives horizontal scale and hides failures."

**Horizontal vs vertical scaling.** Vertical: a bigger machine. Simple, no code changes, hard
ceiling, single point of failure. Horizontal: more machines. No ceiling, but requires
statelessness or partitioning and adds coordination. Say: "Vertical first because it is
free; horizontal when one box is not enough or when we need availability."

**Stateless services.** No per-user state in process memory. Session data lives in a cache or
a signed cookie. Any node can serve any request, so the LB can spray traffic and a dead node
costs nothing. Say: "Stateless API tier; state lives in Redis and the database."

**Caching.** Keep hot data in memory close to the reader. **Cache-aside**: the app checks the
cache, on a miss reads the DB and populates the cache. Simple; risk of stale data until TTL.
**Write-through**: the app writes to cache and DB together. Consistent, slower writes.
**Write-behind**: write to cache, flush to DB later. Fast, risk of loss. **Eviction**: LRU
(default), LFU, or TTL. **Hot keys**: one key read a million times a second overwhelms a
single cache node; fix by replicating that key across nodes or adding a local in-process
cache. Say: "Cache-aside with a TTL; 80% of reads hit 20% of keys."

**CDN.** A globally distributed cache for static assets and cacheable responses. Users hit
the edge 20 ms away instead of your origin 150 ms away. Push (you upload) or pull (edge
fetches on first miss). Say: "Images, JS, and any public GET with a TTL go through a CDN."

**SQL vs NoSQL.** SQL (Postgres, MySQL): schemas, joins, transactions, strong consistency, well
understood, scales reads via replicas and writes via sharding with effort. NoSQL key-value
and wide-column (DynamoDB, Cassandra): horizontal write scaling built in, flexible schema,
no joins, tunable consistency. Document (MongoDB): nested objects. Interviewers accept either
when: the data is under a few TB, the access pattern is by primary key, and you say why. They
push back when you pick NoSQL and then describe a join, or pick SQL for a 1M-writes-per-second
firehose. Say: "Relational for the order and payment data because we need transactions;
key-value for the session store because it is one key, one blob, huge volume."

**Replication.** Copy data to multiple nodes. **Leader/follower** (primary/replica): all writes
go to the leader, followers replay the log and serve reads. **Synchronous** replication
waits for followers (durable, slower); **asynchronous** does not (fast, replication lag, a
user may not see their own write on a replica). **Read replicas** scale reads 5–10x for free.
Failover: promote a follower when the leader dies. Say: "One primary, two async replicas for
reads, promote on failure. Read-your-own-writes by routing a user to the primary for a few
seconds after they write."

**Sharding / partitioning.** Split one big table across many nodes because it no longer fits
or the write rate is too high. **By key (hash)**: `node = hash(user_id) % N`. Even spread,
but range queries scatter and resharding moves everything (fix: consistent hashing). **By
range**: users A–F on node 1. Range queries are cheap; hot ranges (this month's dates) pile
up on one node. **Hotspot problem**: one celebrity or one tenant overwhelms its shard; fix
by salting the key or splitting that shard. Say: "Shard by user_id so all of one user's data
is on one node; that keeps the common query local."

**Consistent hashing.** Place nodes and keys on a ring of hash values; each key belongs to
the first node clockwise. Adding or removing a node moves only about 1/N of the keys instead
of nearly all of them. Virtual nodes (each physical node appears many times on the ring)
smooth the distribution.

```
              0
        ┌───────────┐
   n3 ──┤           ├── n1        key k hashes to position ●
        │     ●─────┼──▶ owned by n1 (first node clockwise)
        │           │
   n2 ──┤           ├── n1'  (virtual node of n1)
        └───────────┘
             2^32
```

Say: "Consistent hashing so adding a cache node only remaps 1/N of keys."

**CAP and eventual consistency.** During a network partition you choose: keep serving
possibly stale data (available, AP) or refuse until nodes agree (consistent, CP). In one
sentence: **eventually consistent** means every replica will converge to the same value if
writes stop, but a read right now may return an older value. Most consumer features (feeds,
likes, view counts) are fine with this; money and inventory are not. Say: "The feed can be
eventually consistent; the payment ledger cannot."

**Message queues (Kafka, SQS, RabbitMQ).** A durable buffer between a producer and a consumer.
**Decoupling**: the web tier returns fast, workers process later. **Backpressure**: if
consumers slow down, the queue grows instead of the web tier falling over. **Retry and dead
letter**: failed messages are retried, then parked. Kafka is a partitioned log (ordered
within a partition, replayable, high throughput); SQS is a managed queue (simple, at-least-once,
no ordering unless FIFO). Say: "Writes go to a queue; workers fan out asynchronously so the
request path stays under 100 ms."

**Rate limiting.** Protect the system from one client. **Token bucket**: a bucket of capacity
B refills at R tokens per second; each request takes one token; empty bucket means 429. Allows
bursts up to B while enforcing an average of R. Alternatives: fixed window (simple, spiky at
boundaries), sliding window log (exact, memory-heavy), sliding window counter (compromise).
Say: "Token bucket per user in Redis; capacity 100, refill 10 per second."

**Idempotency.** The same request applied twice has the same effect as once. Needed because
networks retry. Implement by having the client send an idempotency key (UUID) and the server
store `key → result` for 24 hours; a repeat returns the stored result. Say: "Payment POSTs
carry an idempotency key so a retried request cannot charge twice."

**Unique ID generation.** Auto-increment does not work across shards. **UUID v4**: 128 bits,
random, no coordination, not sortable, large index. **Snowflake**: 64 bits = 41-bit
timestamp (ms) + 10-bit machine ID + 12-bit sequence. Time-sortable, 4,096 IDs per ms per
machine, no coordination beyond assigning machine IDs. **Ticket server**: one DB row you
increment; simple, single point of failure. Say: "Snowflake IDs: sortable by time, generated
locally, no central bottleneck."

**Search indexing.** Databases find rows by key; they cannot find "documents containing
these words" quickly. An **inverted index** maps each term to the list of documents containing
it (Elasticsearch, Solr, Lucene). Updated asynchronously from the primary store via a queue.
Say: "Full-text search goes through Elasticsearch, fed by a change stream from the DB."

**Blob storage.** Files (images, video, backups) do not belong in a database. Object stores
(S3, GCS) give cheap, durable, effectively infinite storage addressed by key, with the DB
holding only the URL. Serve through a CDN. Upload directly from the client with a pre-signed
URL so the API tier never touches the bytes. Say: "Metadata in the DB, bytes in S3, delivery
via CDN."

## 4. Five walked designs

Each design below is a compressed version of what you would say in 45 minutes. Practice
reproducing the diagram and the trade-off from memory before you read the next one.

### 4.1 URL shortener

**Scope.** Create short link, redirect. 100M links/month, 100:1 read ratio, redirect under
100 ms, links live 5 years.

**Numbers.** 40 writes/s, 4,000 reads/s, 3 TB in 5 years, hot set ~35 GB (section 2.2).

**ID generation.** 7 base-62 characters give 3.5 trillion codes. Options: (a) hash the long URL
(MD5) and take 7 chars, handle collisions by probing; (b) a Snowflake-style counter converted
to base 62, which is collision-free and sortable but predictable; (c) a pre-generated key
service that hands out random unused codes in batches. Pick (b) or (c) and say why: no
collision handling in the hot path.

```
 client ─▶ [ LB ] ─▶ [ API nodes ] ─▶ [ Redis: code → url ] ─miss─▶ [ KV store: links ]
                          │
                          └─▶ [ ID service (Snowflake) ]  on writes
```

**Key trade-off.** 301 vs 302 redirect. 301 lets browsers cache and removes load from you, but
you lose click data. 302 forces every click through you, which costs QPS and gives analytics.
Ask which the product wants.

**Deep-dive question you will get.** "How do you handle a link that goes viral?" Answer: it is
a hot key. Redis serves ~100k ops/s per node, so one link at 50k reads/s is fine on one node;
beyond that, replicate the key to several cache nodes or add an in-process LRU on each API
node with a 1-second TTL. Also: "How do you expire links?" A background job scanning by
`expires_at` index, or a DynamoDB TTL attribute.

### 4.2 Rate limiter

**Scope.** Limit each client to N requests per time window across a fleet of API servers.
Return 429 with a Retry-After header. Must add under 5 ms of latency. Slight over-admission
during failures is acceptable; blocking everyone is not.

**Algorithm.** Token bucket per client key. Store `(tokens, last_refill_ts)` in Redis. On each
request, compute tokens to add since last refill, cap at capacity, subtract one if available.
Do it in a Lua script so the read-modify-write is atomic.

```
 client ─▶ [ LB ] ─▶ [ API node ]
                        │  1. rate-limit middleware
                        ▼
                  [ Redis cluster ]  key: rl:{client_id} → {tokens, ts}
                        │  2. allowed? proceed : 429
                        ▼
                  [ downstream service ]
```

**Placement.** As middleware in the API gateway so every service gets it for free. Rules
(limits per endpoint, per tier) live in a config service and are cached locally on each node.

**Key trade-off.** Centralized counter in Redis (accurate, one extra network hop, Redis is a
dependency) vs local counters on each node (zero latency, but N nodes each allow the limit, so
over-admission by a factor of N). Middle ground: local bucket sized limit/N, synced
periodically. Also: fail open or fail closed when Redis is down? Fail open for public APIs,
fail closed for expensive internal ones.

**Deep-dive question.** "What about race conditions when two requests for the same user hit
two API nodes at once?" The Lua script makes the Redis operation atomic. "What if Redis is
sharded?" Hash the client key to a shard; each client's bucket lives on exactly one node.

### 4.3 News feed / timeline

**Scope.** Users follow users, post short items, and read a reverse-chronological feed of
people they follow. 10M daily active users, each reads the feed 10 times a day, posts twice.
Feed load under 200 ms. A few seconds of delay before a post appears is fine.

**Numbers.** Reads: 10M × 10 ÷ 10^5 ≈ 1,000 QPS (peak 3,000). Writes: 200 QPS. Read-heavy by
5:1 on the surface, but see fan-out below.

**Two strategies.**
- **Fan-out on write (push).** When a user posts, a worker appends the post ID to the cached
  feed list of every follower. Reads are one cache lookup: fast. Writes are expensive: a user
  with 10M followers causes 10M cache writes.
- **Fan-out on read (pull).** Store posts by author. At read time, fetch recent posts from all
  followed users and merge. Writes are cheap; reads touch hundreds of shards.

```
 post ─▶ [ API ] ─▶ [ posts DB ] ─▶ [ queue ] ─▶ [ fan-out workers ]
                                                       │  for each follower:
                                                       ▼
                                      [ Redis: feed:{user_id} → [post_id, ...] (cap 1,000) ]
 read ─▶ [ API ] ─▶ Redis feed list ─▶ hydrate post_ids from [ posts cache / DB ] ─▶ client
```

**Key trade-off.** The hybrid is the real answer: push for normal users, pull for accounts
with more than ~10k followers (celebrities), and merge the two at read time. Say this
explicitly; it is the sentence interviewers wait for.

**Deep-dive question.** "A celebrity with 50M followers posts. Walk me through it." Answer:
their posts are not fanned out. Readers who follow them fetch the celebrity's recent posts at
read time from a heavily cached per-author list and merge by timestamp with the pushed feed.
Also expect: "How do you rank instead of sort by time?" (a separate ranking service scores the
candidate set) and "What if a user has been inactive for a year?" (do not fan out to inactive
users; rebuild their feed with pull on next login).

### 4.4 Chat system

**Scope.** One-to-one and small group chat. Messages delivered in real time when the recipient
is online, stored for later if not. Sent, delivered, and read receipts. Message order within a
conversation must be consistent for all participants. 50M daily active users.

**Connections.** HTTP is request/response; the server cannot push. Use **WebSockets**: a
persistent bidirectional TCP connection per online client. A chat server holds ~100k to 1M
connections. A **presence / session service** maps `user_id → chat_server` so any server can
find where a user is connected.

```
 alice ═WS═▶ [ chat server A ]                      [ chat server B ] ◀═WS═ bob
                  │  1. store message                        ▲
                  ▼                                          │ 4. push to bob
            [ messages DB ]  (partition by conversation_id,  │
                  │           sort by message_id)            │
                  ▼                                          │
            [ queue / pub-sub ] ── 3. route via session lookup: bob → server B
                  ▲
            [ session service: user → server ]  (Redis)
```

**Message IDs and ordering.** Do not use client timestamps. The chat server assigns a
per-conversation monotonically increasing sequence number (or a Snowflake ID, which is
time-sortable). Store messages keyed by `(conversation_id, message_id)`, so fetching a
conversation is one range read. Cassandra or HBase fit this write-heavy, range-read pattern.

**Receipts.** Sent: the server has persisted it (ack to sender). Delivered: the recipient's
client acked over its WebSocket. Read: the client reports the highest message_id it has
rendered. Store `last_read_id` per user per conversation; do not store a row per message per
user.

**Key trade-off.** Delivery guarantees vs complexity. At-least-once delivery with client-side
deduplication by message_id is what production systems do; exactly-once is not achievable
over a lossy network without idempotency at the receiver anyway.

**Deep-dive question.** "Bob is offline. Then he comes online on two devices." Answer: the
message is stored; on connect, each device sends its `last_seen_id` for each conversation and
the server sends the gap. Multi-device means receipts are per device, but read state is per
user (the max across devices). Also: "How do group messages scale?" For groups under ~500,
fan out on write to each member's inbox; for larger channels, members pull from the channel.

### 4.5 Key-value store (Dynamo-style)

**Scope.** `put(key, value)`, `get(key)`. Values under 10 KB. Horizontally scalable to
petabytes, highly available (always accept writes), tunable consistency, no single point of
failure.

**Partitioning.** Consistent hashing with virtual nodes (section 3). Each key lives on the
first node clockwise on the ring, and the N−1 following distinct nodes hold replicas. This
list is the key's **preference list**.

**Replication and quorum.** N replicas. A write is acknowledged after W replicas confirm; a
read waits for R replicas. If **R + W > N**, at least one node in every read set has the latest
write, so reads see the most recent acknowledged value. Typical: N=3, W=2, R=2. For a
write-heavy log, W=1, R=3. For a read-heavy config store, W=3, R=1.

```
   ring:  ... ─ n1 ─ n2 ─ n3 ─ n4 ─ n5 ─ ...
   key k → coordinator n2; preference list [n2, n3, n4]  (N = 3)

   put(k): coordinator writes locally, forwards to n3, n4; returns after W = 2 acks
   get(k): reads from n2, n3, n4; returns after R = 2 respond; reconciles versions
```

**Conflicts and vector clocks.** Because the system accepts writes even when replicas cannot
talk to each other, two replicas can hold different values for the same key. A **vector
clock** is a list of `(node, counter)` pairs attached to each version; every write increments
the coordinating node's counter. If version A's counters are all less than or equal to B's,
A is an ancestor and B wins. If neither dominates, the versions are concurrent and the store
returns both to the client to reconcile (or uses last-writer-wins if the application accepts
losing one). Dynamo returns both; DynamoDB and Cassandra default to last-writer-wins.

**Availability under failure.** **Sloppy quorum**: if a node in the preference list is down,
write to the next healthy node on the ring with a **hinted handoff** note; it forwards the data
when the original node returns. **Anti-entropy**: replicas compare **Merkle trees** of their
key ranges in the background and repair differences. **Gossip protocol**: nodes exchange
membership and health information peer-to-peer, so there is no central coordinator to fail.

**Key trade-off.** This is the AP design: availability and partition tolerance over strong
consistency. Say when you would not use it: anything that needs a transaction across two
keys, or where returning two versions to the caller is unacceptable.

**Deep-dive question.** "N=3, W=1, R=1. What can go wrong?" Answer: R + W = 2 ≤ N, so a read
can hit a replica that never saw the write and return stale data. "What if a coordinator dies
mid-write after 1 of 2 acks?" The client times out and retries (writes must be idempotent by
key); the one replica that has it will spread it via read repair or anti-entropy.

## 5. Amazon's Low-Level / Object-Oriented Design round

Amazon runs a separate round, usually for SDE1 and SDE2, where you design the classes for a
small system: parking lot, elevator, vending machine, LRU cache, library, movie ticket booking,
a deck of cards. There is no scale, no QPS. The grader wants clean decomposition, sensible
interfaces, and code you could start writing.

**SOLID in one line each**

| Letter | Principle | The one sentence to remember |
|--------|-----------|------------------------------|
| S | Single responsibility | A class has one reason to change. |
| O | Open/closed | Add behavior by adding a class, not by editing a `switch`. |
| L | Liskov substitution | Anywhere you accept the base type, every subtype must work. |
| I | Interface segregation | Many small interfaces beat one fat one. |
| D | Dependency inversion | Depend on abstractions; inject the concrete class. |

**How to present.** Same protocol as system design, compressed: (1) clarify requirements and
list the use cases in plain sentences; (2) name the nouns (classes) and verbs (methods); (3)
draw the class diagram with relationships; (4) write the two or three most important classes
in code; (5) walk through one use case end to end; (6) name what you would extend. Talk about
where an enum becomes a class hierarchy and where a strategy interface lets a rule change
without editing the core.

**Worked example: parking lot**

Requirements: multiple floors; spots of sizes motorcycle, compact, large; vehicles of the
matching kinds; a large vehicle only fits a large spot, a motorcycle fits anything; issue a
ticket on entry, compute a fee on exit; report free spots per size per floor.

```
 ┌──────────────────────┐        ┌────────────────────┐
 │ ParkingLot           │ 1    * │ ParkingFloor       │
 │ - floors: list       │───────▶│ - spots: dict      │
 │ - tickets: dict      │        │ + find_spot(v)     │
 │ + park(vehicle)      │        │ + free_count(size) │
 │ + unpark(ticket_id)  │        └─────────┬──────────┘
 │ - fee_strategy       │                  │ 1     *
 └──────────┬───────────┘        ┌─────────▼──────────┐
            │ uses               │ ParkingSpot        │
            ▼                    │ - size: SpotSize   │
 ┌──────────────────────┐        │ - vehicle: Vehicle?│
 │ <<interface>>        │        │ + fits(vehicle)    │
 │ FeeStrategy          │        │ + occupy / vacate  │
 │ + fee(ticket, now)   │        └────────────────────┘
 └──────────┬───────────┘
            │ implements                  ┌───────────────────┐
 ┌──────────┴──────────┐                  │ Vehicle (abstract)│
 │ HourlyFee           │                  │ - plate           │
 │ FlatDailyFee        │                  │ - size: SpotSize  │
 └─────────────────────┘                  └─────────┬─────────┘
                                                    │
 ┌─────────────────────────────────┐   Motorcycle ─ Car ─┴─ Truck
 │ Ticket                          │
 │ - id, spot, vehicle, entry_time │
 └─────────────────────────────────┘
```

Python-style sketches. Enough to show the shape; you would not write every method in the room.

```python
from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime

class SpotSize(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3

class Vehicle(ABC):
    size: SpotSize                      # each subclass sets this

    def __init__(self, plate: str):
        self.plate = plate

class Motorcycle(Vehicle):
    size = SpotSize.MOTORCYCLE

class Car(Vehicle):
    size = SpotSize.COMPACT

class Truck(Vehicle):
    size = SpotSize.LARGE

class ParkingSpot:
    def __init__(self, spot_id: str, size: SpotSize):
        self.id, self.size, self.vehicle = spot_id, size, None

    def fits(self, vehicle: Vehicle) -> bool:
        return self.vehicle is None and vehicle.size.value <= self.size.value

    def occupy(self, vehicle: Vehicle) -> None:
        self.vehicle = vehicle

    def vacate(self) -> None:
        self.vehicle = None

class FeeStrategy(ABC):
    @abstractmethod
    def fee(self, ticket: "Ticket", now: datetime) -> float: ...

class HourlyFee(FeeStrategy):
    def __init__(self, rate_per_hour: float):
        self.rate = rate_per_hour

    def fee(self, ticket, now):
        hours = max(1, (now - ticket.entry_time).total_seconds() / 3600)
        return round(hours) * self.rate

class ParkingLot:
    def __init__(self, floors: list["ParkingFloor"], fee_strategy: FeeStrategy):
        self.floors = floors
        self.fee_strategy = fee_strategy       # injected: swap pricing without touching this class
        self.tickets: dict[str, "Ticket"] = {}

    def park(self, vehicle: Vehicle) -> "Ticket | None":
        for floor in self.floors:
            spot = floor.find_spot(vehicle)
            if spot:
                spot.occupy(vehicle)
                ticket = Ticket(spot, vehicle, datetime.now())
                self.tickets[ticket.id] = ticket
                return ticket
        return None                             # lot full; caller decides what to show

    def unpark(self, ticket_id: str) -> float:
        ticket = self.tickets.pop(ticket_id)
        ticket.spot.vacate()
        return self.fee_strategy.fee(ticket, datetime.now())
```

What the grader hears: `fits` encodes the size rule in one place (S). Pricing is a strategy
interface, so a weekend rate is a new class, not an `if` (O, D). `Vehicle` subtypes are
interchangeable wherever `Vehicle` is accepted (L). Then extend on request: reserved spots
become a `SpotType` enum plus a check in `fits`; electric charging is a `ChargingSpot`
subclass; concurrency is a lock per floor around `find_spot` and `occupy`.

The same shape works for the other classics. Elevator: `ElevatorSystem` → `Elevator` with a
`Direction` enum and a `SchedulingStrategy` interface. Vending machine: a `State` interface
(`Idle`, `HasMoney`, `Dispensing`) is the textbook State pattern. LRU cache: a dict plus a
doubly linked list, which you already built in chapter 04; here you present it as a class
with `get` and `put` and talk about thread safety.

## 6. Trade-off vocabulary

Use these pairs by name. Each row is a sentence you can say in the room.

| Trade-off | Choose the left when | Choose the right when | Say |
|-----------|---------------------|-----------------------|-----|
| **Consistency vs availability** | Money, inventory, bookings: a wrong answer is worse than no answer | Feeds, counters, presence: a stale answer beats an error | "During a partition this component should refuse rather than lie." |
| **Latency vs throughput** | Interactive requests; users are waiting | Batch, analytics, backfills; total work per hour is what matters | "I will batch writes to the DB in 100s to raise throughput; the queue hides the latency." |
| **Normalization vs denormalization** | Writes dominate; data changes often; storage is precious | Reads dominate; joins are the bottleneck; storage is cheap | "I will denormalize the author name into the post row and accept an update fan-out on rename." |
| **Push vs pull** | Few producers, many idle consumers who want it now (notifications, feeds for normal users) | Many producers or bursty consumers; consumers control rate (celebrity feeds, polling dashboards) | "Push to online clients over WebSocket; offline clients pull on reconnect." |
| **Sync vs async** | The caller needs the result to continue (auth check, payment authorization) | The caller needs only an acknowledgment (email, thumbnail generation, analytics) | "Return 202 and finish the work from a queue." |
| **Strong vs eventual consistency** | Same as consistency column, plus read-your-own-writes UX | Cross-region replication, high write volume | "Eventual across regions, strong within a region." |
| **SQL vs NoSQL** | Joins, transactions, ad-hoc queries, under a few TB | Key access, huge write volume, flexible schema | "Postgres now, with a plan to shard by tenant if we pass 10k writes/s." |
| **Stateful vs stateless** | Long-lived connections (WebSockets), in-memory session affinity | Everything else | "Stateless API nodes; the connection servers are the one stateful tier." |

## 7. Practice

**Ten prompts to design on paper**, 45 minutes each, out loud, with the protocol from section 2.
After each, compare against a reference design and write down what you missed.

1. Design a URL shortener (redo the one above without looking).
2. Design a distributed rate limiter for a public API.
3. Design Twitter's home timeline.
4. Design WhatsApp (one-to-one and group chat with receipts).
5. Design a key-value store that survives node failure.
6. Design a web crawler that indexes 1 billion pages a month.
7. Design YouTube's upload and playback path (transcoding, CDN, adaptive bitrate).
8. Design Google Drive (file sync, conflict handling, deduplicated storage).
9. Design a ride-matching service like Uber (geospatial index, matching, location updates).
10. Design a notification system (push, SMS, email; priorities; deduplication; user preferences).

Amazon extras: the order history page, a product search autocomplete, an inventory service
that never oversells. Google extras: Google Maps nearby search, a distributed
autocomplete/typeahead, a metrics and alerting pipeline.

**Object-oriented design prompts**: parking lot, elevator, vending machine, LRU cache, library
management, movie ticket booking, chess, a file system with directories and permissions.

**Resources**, named plainly:

- *Designing Data-Intensive Applications* by Martin Kleppmann. Chapters 5 (replication), 6
  (partitioning), 7 (transactions), and 9 (consistency and consensus) are the ones interviewers
  have read. Read those four even if you skip the rest.
- The **System Design Primer** repository on GitHub (donnemartin/system-design-primer). Free,
  covers every building block in section 3 with links, and has worked solutions to most of
  the ten prompts above.
- **Alex Xu**, *System Design Interview: An Insider's Guide*, volumes 1 and 2. Volume 1 walks
  through the same five designs as section 4 plus about ten more, one chapter each, in
  interview format. Volume 2 covers harder prompts (payments, stock exchange, ad click
  aggregation). Best return on time of the three for interview preparation specifically.
- The original Dynamo paper (DeCandia et al., 2007) is 16 pages and readable. Read it once so
  section 4.5 is yours instead of memorized.
- **Grokking the Object-Oriented Design Interview** (Educative) for the Amazon LLD round.

One design a day for a week, out loud, drawing on paper, is enough to make this round a fair
fight. Two weeks makes it a strength.
