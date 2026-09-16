# 13 · System Design

**In one sentence.** System design is arranging a handful of standard building blocks so a
service stays fast and stays up while its users grow from ten to ten million.

**Why you care.** This round is for SDE2 / L4 and above. Amazon gives SDE1 candidates an
object-oriented design question instead, and Google does not ask L3 candidates at all. If you
are a new grad, read the story, the protocol, and the object-oriented section, then spend the
time on chapters 14 and 15. If you are L4+ or SDE2+, this round can fail your loop on its own.
It decides whether the interviewer believes you can hold a whole system in your head, which is
what senior engineers are paid for.

## The idea, with a story

You open a lemonade stand. One table, one jug, you. Ten customers an hour. Life is good.

Word spreads. Now there is a line, and the line is the whole problem. Watch each fix.

1. You hire a cashier and become the maker. Two jobs, two people. In software: two *services*.
2. You open a second stand next door. More copies, not a bigger copy. That is *horizontal
   scaling*. A bigger jug would be *vertical scaling*, but there is a biggest jug you can lift.
3. You hire a greeter who points each customer to the shorter line. That is a *load balancer*.
4. You put a fridge of pre-made lemonade at the front. A pour takes two seconds instead of ten.
   That is a *cache*. The catch: fridge lemonade may be stale.
5. Both stands need the same recipe book, so you photocopy it. That is *replication*. When you
   change the recipe, the copies disagree for a while. That is *eventual consistency*.
6. The customer-tab binder gets too fat. You split it A to M and N to Z. That is *sharding*.
7. Custom orders take twenty minutes. You write them on a pad and the maker works through it.
   That pad is a *message queue*.

The recipe never changed. The plumbing did. Every block in this lesson is one of these moves.

## The same story with numbers

Interviewers call this *back-of-envelope estimation*. 1,000 customers a day, 10 seconds each,
open 10 hours. How many stands?

| Question | Arithmetic | Answer |
|----------|------------|--------|
| Seconds open per day | 10 × 3,600 | 36,000 |
| Customers per second, average | 1,000 ÷ 36,000 | one every 36 seconds |
| Lunch peak, about 3× average | 36 ÷ 3 | one every 12 seconds |
| Work per customer | | 10 seconds |
| Stands needed at peak | 10 ÷ 12 | less than one. One stand. |

The number made a decision for you: do not build a second stand. Being off by 3× is fine.
What matters is that a number changed a decision.

Pause and predict: the stand goes viral and gets 10,000 customers a day. How many stands at
the lunch peak, and which move from the story is cheaper than building them?

<details><summary>Answer</summary>
Average: 10,000 ÷ 36,000 ≈ one every 3.6 seconds. Peak: one every 1.2 seconds. Each takes 10
seconds, so 10 ÷ 1.2 ≈ 9 stands. Cheaper: the fridge. A 2-second pour needs 2 ÷ 1.2 ≈ 2 stands.
Caching is not an optimization. It is the design.
</details>

## The 45-minute protocol

Use the same shape every time, so you never have to think about what comes next.

| Minutes | Phase | What goes on the whiteboard |
|---------|-------|-----------------------------|
| 0–5 | Clarify | Functional list, non-functional list, explicit out-of-scope list |
| 5–10 | Estimate | Read QPS, write QPS, storage over 5 years, bandwidth. Three or four lines. |
| 10–15 | API and data model | 3 to 5 endpoints. Main table or key-value shape. |
| 15–25 | High-level diagram | Client → load balancer → services → cache → database → queue. Every arrow labeled. |
| 25–38 | Deep dive | One or two components at depth. Hire or no-hire is decided here. |
| 38–43 | Trade-offs and scaling | "At 10× I would..." Failure modes. |
| 43–45 | Wrap | Summarize. Ask what they would have pushed on. |

The clarifying questions are the same every time. Who are the users and what are their two or
three core actions? What is out of scope? Read-heavy or write-heavy, and by what ratio? How
many users and requests per second? What latency is fine? If a user writes and reads back
immediately, must they see it? One region or global? Then say the scope back and write it down.

In the deep dive, go two levels down: data layout inside the component, what happens when it
dies or fills up, what changes at 10× and 100×, and where two users might see different
answers. For every big choice, say one sentence starting with "alternatively." Both companies
fail candidates for the same three habits: drawing before asking, never writing a number, and
never saying that word.

## Building blocks

| Block | What it is | When you reach for it |
|-------|------------|-----------------------|
| Load balancer | Spreads requests over identical servers and skips dead ones | Whenever you have more than one copy of a service |
| Cache | A fast in-memory copy of data you read often, thrown out after a TTL | Reads outnumber writes and a little staleness is fine |
| CDN | Caches placed in every city so far-away users get a nearby copy | Images, video, scripts, any public response with a TTL |
| SQL database | Strict tables, joins, transactions, strong consistency | Orders, payments, anything needing transactions, under a few TB |
| NoSQL database | Key-value or wide-column store that spreads across machines by design | One-key lookups at huge volume, flexible schema, no joins |
| Replication | Copies of the data on several machines; one leader takes writes, replicas serve reads | Scaling reads 5 to 10× and surviving a dead machine |
| Sharding | Splitting one huge table across machines by a key | The data or the write rate no longer fits one machine |
| Consistent hashing | Machines and keys on a ring, so adding a machine moves only 1/N of the keys | Cache clusters and sharded stores that grow and shrink |
| Message queue | A durable buffer between a producer and a worker | Work the caller need not wait for: email, thumbnails, fan-out |
| Rate limiter | A token bucket per client that refills at a fixed rate; empty bucket means 429 | Public APIs, protection from one greedy client |
| Idempotency | The same request applied twice has the same effect as once, via a client-sent key | Payments and anything a network retry could double |
| Unique IDs | Snowflake: timestamp + machine ID + sequence. Sortable, no central counter | Any sharded system, where auto-increment stops working |
| Blob storage | An object store for big files; the database keeps only the URL | Photos, video, backups. Serve through the CDN. |

Two rules of thumb. A single tuned database handles thousands of writes a second and tens of
thousands of indexed reads. Under 1,000 QPS and 1 TB, one database with a read replica is
the right answer, and saying so is graded as good judgment.

## Numbers to memorize

| Fact | Value | Use |
|------|-------|-----|
| Seconds per day | about 100,000 | daily volume ÷ 100,000 = average QPS |
| Seconds per month | about 2.5 million | monthly volume to QPS |
| Peak vs average | say 3× | size for peak |
| Small text record | 100 bytes to 1 KB | row sizes |
| Photo | say 500 KB | blob storage |
| Memory, SSD, disk | 100 ns, 100 µs, 10 ms | each step is 100 to 1,000× slower |
| Datacenter round trip | 0.5 ms | one hop between services |
| Cross-continent round trip | 150 ms | why CDNs exist |
| One Redis node | about 100,000 ops/s | sizing a cache |
| 99.9% vs 99.99% uptime | 8.7 hours vs 52 minutes down per year | availability targets |

## Five designs in one paragraph each

**URL shortener.** Scope: create a short link, redirect. 100M links a month, 100 reads per
write, redirect under 100 ms. Numbers: 40 writes/s, 4,000 reads/s, 3 TB in five years, hot
set about 35 GB. Design: load balancer, stateless API nodes, Redis cache of code → URL, a
key-value store behind it, and Snowflake IDs converted to 7 base-62 characters so there is no
collision handling on the hot path. Key trade-off: 301 redirects let browsers cache and shed
your load; 302 forces every click through you and gives analytics. Ask which the product
wants.

**Rate limiter.** Scope: N requests per client per window across a fleet of API servers,
under 5 ms added latency. Design: token bucket per client stored in Redis as (tokens,
last_refill), updated in an atomic Lua script, run as middleware in the API gateway. Key
trade-off: one central counter in Redis is accurate but adds a hop and a dependency; local
counters on each node are free but over-admit by a factor of N. Also decide whether to fail
open or closed when Redis is down: open for public APIs, closed for expensive internal ones.

**News feed.** Scope: follow users, post, read a reverse-chronological feed. 10M daily users,
about 1,000 read QPS, 200 write QPS. Fan-out on write pushes each post ID into every
follower's cached feed list, so reads are one lookup but a celebrity post costs millions of
writes. Fan-out on read stores posts by author and merges at read time, so writes are cheap
and reads touch hundreds of shards. Key trade-off: the hybrid. Push for normal users, pull for
accounts over about 10k followers, merge at read time. That sentence is the one interviewers
wait for.

**Chat.** Scope: one-to-one and small groups, real-time delivery, receipts, consistent order.
HTTP cannot push, so each online client holds a WebSocket to a chat server, and a session
service in Redis maps user → server. Messages are stored keyed by (conversation_id,
message_id) with a server-assigned sequence number, never client timestamps. Read state is one
last_read_id per user per conversation. Key trade-off: at-least-once delivery with client-side
deduplication by message ID is what production does. Exactly-once is not achievable over a
lossy network without that anyway.

**Key-value store.** Scope: put and get, petabyte scale, always accept writes, no single
point of failure. Design: consistent hashing with virtual nodes; each key lives on N replicas
clockwise on the ring. A write returns after W acks, a read after R replies. If R + W > N,
reads see the latest acknowledged write. Typical N=3, W=2, R=2. Conflicts from concurrent
writes are tracked with vector clocks or resolved last-writer-wins. Key trade-off: this is the
AP design, availability over strong consistency. Say when you would not use it: anything that
needs a transaction across two keys.

## Amazon's object-oriented design round

Amazon runs a separate round for SDE1 and SDE2: design the classes for a parking lot, an
elevator, a vending machine, an LRU cache. No scale, no QPS. The grader wants clean
decomposition and code you could start writing. Present it in six steps: list the use cases in
plain sentences, name the nouns (classes) and verbs (methods), draw the relationships, code the
two or three important classes, walk one use case end to end, name what you would extend.

Parking lot requirements: floors; spots sized motorcycle, compact, large; a vehicle fits any
spot at least its size; ticket on entry, fee on exit.

```python
class SpotSize(Enum):
    MOTORCYCLE, COMPACT, LARGE = 1, 2, 3

class ParkingSpot:
    def fits(self, vehicle) -> bool:          # the size rule lives in one place
        return self.vehicle is None and vehicle.size.value <= self.size.value

class FeeStrategy(ABC):
    @abstractmethod
    def fee(self, ticket, now) -> float: ...  # HourlyFee, FlatDailyFee are subclasses

class ParkingLot:
    def __init__(self, floors, fee_strategy):
        self.floors, self.fee_strategy, self.tickets = floors, fee_strategy, {}

    def park(self, vehicle):                  # first floor with a fitting spot
        ...

    def unpark(self, ticket_id) -> float:
        return self.fee_strategy.fee(self.tickets.pop(ticket_id), datetime.now())
```

What the grader hears: the size rule is in one place (single responsibility). Pricing is an
injected strategy, so a weekend rate is a new class, not an `if` (open/closed). Vehicle
subclasses are interchangeable wherever a vehicle is accepted (Liskov). Then extend on request:
reserved spots are a check in `fits`, concurrency is a lock per floor.

## Words you will hear

- **Server.** The machine answering requests. A stand.
- **Latency.** How long one request waits for its answer. Milliseconds.
- **Throughput.** How many requests per second the whole system completes.
- **QPS.** Queries per second. The number you estimate first.
- **Cache.** A fast copy of data you read often. May be stale, may vanish.
- **Load balancer.** The greeter. Spreads requests over identical servers.
- **Replication.** Copies of the same data on several machines.
- **Sharding.** Splitting one dataset across machines by a key.
- **Consistency.** Do all copies agree right now? Strong: yes. Eventual: soon.
- **Availability.** The fraction of time you can serve at all.

## Mistakes everyone makes once

- **Drawing boxes before asking questions.** Your first words should be about scale, not a component.
- **Never writing a number.** "100 million links a month" is dread. "40 writes a second, fits on one Postgres" is a decision.
- **Adding boxes to look senior.** Under 1,000 QPS and 1 TB, one database with a replica is the right answer. Say so.
- **Picking NoSQL and then describing a join.** Choose the store from the access pattern, and say why.

## What to do next

Set a 20-minute timer. Take "design a URL shortener" and do only minutes 0 to 10 of the
protocol on paper, out loud: the clarifying questions, then the estimate. Compare with the
numbers in the URL shortener paragraph above. If yours are within 3× and a number made a
decision for you, do the same tomorrow for the rate limiter.
