# 13 · System Design, explained from zero

Read this first if "load balancer" and "sharding" sound like parts of a car engine. When the
lemonade stand below makes sense, open `LESSON.md`, which is the dense reference with the
45-minute protocol and the five walked designs. This file is the conversation before it.

One note on who needs this: Amazon gives new grads a light version at most, and Google does
not ask it below L4. If that is you, read this file, skim the lesson, and spend your hours on
chapters 14 and 15. If you are SDE2 / L4 or above, this round can fail your loop by itself.

## In one sentence

System design is arranging a handful of standard building blocks so that a service stays
fast and stays up while the number of people using it grows from ten to ten million.

## Start with something you already do

You open a lemonade stand. One table, one jug, you. A customer walks up, you take the order,
squeeze the lemons, take the money. Ten customers an hour. Life is good.

Word spreads. Now there is a line, and the line is the whole problem. Watch each fix:

1. **You hire a cashier and become the maker.** Taking money and squeezing lemons are now two
   jobs done by two people at the same time. In software these are two *services*, each doing
   one thing.
2. **You open a second stand next door.** Same menu, same recipe, twice the customers. That is
   *horizontal scaling*: more copies, not a bigger copy. (Buying a bigger jug is *vertical
   scaling*. Cheaper, but there is a biggest jug you can lift.)
3. **You hire a greeter** who points each arriving customer to the shorter line. That is a
   *load balancer*. If one stand runs out of cups, the greeter stops sending people there.
4. **You put a fridge of pre-made lemonade** at the front. Most people order plain lemonade, so
   you pour from the fridge in two seconds instead of squeezing for ten. That is a *cache*. The
   catch: fridge lemonade was made an hour ago. If you change the recipe, the fridge is stale
   until you refill it.
5. **Both stands need the same recipe book.** You photocopy it. That is *replication*. Now the
   hard part: when you change the recipe, the copy next door is wrong until someone walks over.
   For a few minutes the two stands disagree. That is a *consistency* problem, and "they will
   agree eventually" is called *eventual consistency*.
6. **The book of customer tabs gets too fat for one binder.** You split it: names A to M in one
   binder, N to Z in another. That is *sharding*. If half your customers are named Smith, the
   N to Z binder is swamped: a *hotspot*.
7. **Custom orders take twenty minutes.** Instead of holding up the line, you write them on a
   pad and the maker works through the pad. That pad is a *message queue*. The customer gets
   a ticket now and the drink later.

Every building block in the lesson is one of these moves. The recipe never changed. The
plumbing did.

## Now the same thing with numbers

The lesson calls this *back-of-envelope estimation*. Here is the whole skill on a lemonade
stand: 1,000 customers a day, 10 seconds each, open 10 hours. How many stands?

| Question | Arithmetic | Answer |
|----------|------------|--------|
| Seconds open per day | 10 × 3,600 | 36,000 |
| Customers per second, on average | 1,000 ÷ 36,000 | one every 36 seconds |
| At the lunch peak, roughly 3× average | 36 ÷ 3 | one every 12 seconds |
| Work per customer | | 10 seconds |
| Stands needed at peak | 10 ÷ 12 | less than one: a single stand, short line |

The number just made a decision for you: do not open a second stand. Interviewers care far
more that a number changed a decision than that it was exact. Being off by 3× is fine.

Pause and predict: your stand goes viral and gets 10,000 customers a day. How many stands at
the lunch peak? And which move from the story is cheaper than building that many?

<details><summary>Answer</summary>
Average: 10,000 ÷ 36,000 ≈ one every 3.6 seconds. Peak: one every 1.2 seconds. Each takes 10
seconds, so 10 ÷ 1.2 ≈ 8.3, call it 9 stands. Cheaper: the fridge. If pouring pre-made
lemonade takes 2 seconds, you need 2 ÷ 1.2 ≈ 2 stands. That is why the lesson says "caching is
not an optimization; it is the design."
</details>

## The words people use

- **Client.** The thing asking: a phone, a browser. The customer.
- **Server.** The machine answering. A stand.
- **Request / response.** One order and the drink that comes back.
- **API.** The menu: the fixed list of things a client may ask for and the shape of each answer.
- **Latency.** How long one customer waits for their drink. Measured in milliseconds.
- **Throughput.** How many drinks per second the whole operation produces.
- **QPS.** Queries per second. Requests arriving per second. The number you estimate first.
- **Database.** The binders: where data lives permanently. *SQL* databases keep strict tables
  and can join them; *NoSQL* ones trade that for easier spreading across machines.
- **Cache.** The fridge. A fast copy of data you read often. *Hit*: it was there. *Miss*: it
  was not, go to the database. *TTL*: how long before a fridge item is thrown out.
- **Load balancer.** The greeter. Spreads requests over identical servers and skips dead ones.
- **Horizontal / vertical scaling.** More stands / a bigger stand.
- **Stateless.** A stand that keeps no memory of past customers, so any stand can serve anyone.
- **Replication.** Photocopying the recipe book onto several machines. One *leader* takes
  writes; *replicas* serve reads.
- **Consistency.** Do all copies agree right now? *Strong*: yes. *Eventual*: soon.
- **Availability.** What fraction of the time you can serve at all. 99.9% is 8.7 hours down a
  year; 99.99% is 52 minutes.
- **CAP.** When copies cannot talk to each other, you pick: serve possibly-stale data, or
  refuse until they agree. You cannot have both.
- **Sharding / partitioning.** Splitting one huge binder by some key across machines.
- **Hotspot / hot key.** One shard or one item getting most of the traffic.
- **Consistent hashing.** A way to assign items to machines so adding a machine moves only a
  small fraction of items.
- **Message queue.** The order pad. Take the request now, do the work later.
- **CDN.** Fridges placed in every city so a faraway customer gets a nearby pour.
- **Blob storage.** A warehouse for big files (photos, video). The database keeps only the shelf label.
- **Rate limiting.** "Ten drinks per person per hour." Protects you from one greedy client.
- **Idempotent.** Placing the same order twice charges you once. Needed because networks retry.
- **Single point of failure.** The one stand, jug, or greeter that takes everything down when it breaks.
- **Trade-off.** Every choice above costs something. Saying the cost out loud is the round.

## Why this matters more than it looks

The concrete cost of a wrong design is an outage, and outages have numbers. A single database
serves perhaps 10,000 simple reads a second. Put a fridge in front and it serves 100,000. Now
the fridge dies at lunch: all 100,000 requests a second hit a database built for 10,000, and
the site is down until someone restocks. That is a real postmortem shape, and the fix (a
second fridge, warming the fridge before opening) is a design decision, not a code fix.

The interview cost is simpler. The lesson names three things that fail candidates at both
companies: drawing boxes before asking questions, never writing a number, and never saying
"alternatively." All three are habits, and all three are fixable in a week of practice.

## Try it in your head

1. Your stand tracks "cups sold today" on a whiteboard. You open a second stand. What goes
   wrong, and which building block is the fix?

<details><summary>Answer</summary>
Two whiteboards disagree. Either one shared board that both stands write to (a single
database, with a queue for the lunch rush) or accept eventual consistency and add the two
boards at closing. Say which and why: a cup count can be a little stale; a cash total cannot.
</details>

2. A service gets 4,000 reads a second and 40 writes a second. Where does the design effort go?

<details><summary>Answer</summary>
Reads. The ratio is 100:1. A cache in front of the database handles most reads; the writes fit
on one machine untouched. This is the URL shortener in the lesson.
</details>

3. You shard customer tabs by the first letter of the last name. Which shard becomes the
   hotspot, and what would you split by instead?

<details><summary>Answer</summary>
S, M, and a few others carry far more names than Q or X. Split by a hash of the customer ID so
names spread evenly.
</details>

## Common confusions, cleared

- **"Isn't there a right answer I should memorize?"** No. Two reasonable designs with the costs
  stated beat one recited architecture. "It depends, and here is what it depends on" is the
  winning sentence.
- **"Do I need to know Kafka, Redis, Cassandra by name?"** You need to know what the block does:
  queue, cache, wide-column database. Brand names are a convenience, not a requirement.
- **"More boxes means a better design."** The opposite. Under 1,000 QPS and 1 TB, one database
  with a replica is the right answer, and saying so is graded as good judgment.
- **"Isn't a cache just a faster database?"** It is a copy that may be stale and may vanish.
  Speed is what you buy; freshness and durability are what you pay.

## What to do next

Open `LESSON.md` and read §2, the 45-minute protocol, then §3, the building blocks. Next to
each block, write the lemonade move in the margin. Then a 20-minute first task: take "design a
URL shortener," set a timer for 20 minutes, and do only minutes 0 to 10 of the protocol on
paper, out loud: the clarifying questions and the estimate. Compare against §2.2. If your
numbers are within 3× and you reached a decision, you are ready for the rest of the lesson.
