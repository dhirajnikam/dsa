# 11 · Greedy & Intervals, explained from zero

Read this first if "greedy algorithm" sounds like an insult and "sweep line" sounds like a
janitor's tool. When the stories below make sense, move to `LESSON.md`, the dense reference.
This file is the chat with a patient friend that comes before it.

## In one sentence

Greedy means making the choice that looks best right now and never going back to change it,
and interval problems are where that recklessness is provably correct, as long as you sort first.

## Start with something you already do

**The receptionist.** You run the front desk at a company with one meeting room. Eight teams
have each requested a time slot, and the slots overlap. Fit in as many meetings as possible.
Nobody cares which teams, only the count.

Shortest meetings first? Whoever asked first? Both can be beaten. The plan that cannot: among
the requests that have not started yet, pick the one that **ends earliest**, book it, cross out
everything that clashes with it, repeat. You never reconsider a booking once it is made.

Why is that safe? Suppose a perfect schedule exists that does *not* start with the
earliest-ending meeting. Whatever it booked first ends later than yours, or at the same time.
Swap yours in. Yours frees the room sooner, so nothing later in the perfect schedule is
disturbed, and the count is unchanged. So the perfect schedule was never better than yours.
That swap is the **exchange argument**, the one sentence that turns greedy from a gamble into
a proof: "if a perfect plan chose differently here, I could swap my choice in and it would
still be perfect."

**The calendar merge.** Your boss hands you everyone's busy blocks and says "show me one bar
per stretch of busy time." You sort the blocks by start time, put your pen on the first one,
and slide right. Each next block either begins before your current bar has ended, so you
stretch the bar, or begins after, so you lift the pen and start a new bar. One pass, never
looking back. Also greedy.

The two stories sorted differently. Choosing what to keep: sort by **end**. Merging what
overlaps: sort by **start**. "By start or by end?" is the first question on any interval problem.

## Now the same thing with numbers

Merge `[1,3] [2,6] [8,10] [15,18]`, already sorted by start. Your pen holds the "current bar."

| Next block | Current bar | Starts at or before the bar ends? | Bar after |
|------------|-------------|-----------------------------------|-----------|
| [1,3] | none | start fresh | [1,3] |
| [2,6] | [1,3] | 2 ≤ 3, yes | [1,6] |
| [8,10] | [1,6] | 8 ≤ 6, no | finish [1,6], start [8,10] |
| [15,18] | [8,10] | 15 ≤ 10, no | finish [8,10], start [15,18] |

Result: `[1,6] [8,10] [15,18]`. Pause and predict: merge `[1,10]` then `[2,3]`. What should the
bar be after the second block, and what is the trap?

<details><summary>Answer</summary>
[1,10]. The block [2,3] sits entirely inside, so the bar must not change. The trap is writing
"new end = 3" instead of "new end = the larger of 10 and 3." That missing `max` is the most
common bug in this chapter.
</details>

Now the sweep line, for "how many rooms do I need at once?" Every booking becomes two events:
+1 when someone enters a room, −1 when they leave. Bookings `[0,30] [5,10] [15,20]` become
`(0,+1) (5,+1) (10,−1) (15,+1) (20,−1) (30,−1)`. Run a counter: 1, 2, 1, 2, 1, 0. The peak
was 2, so two rooms. When a start and an end share a time, process the end first, so a room
freed at 10 can be reused at 10.

## The words people use

- **Interval.** A start and an end, written `[start, end]`. A meeting, a busy block.
- **Closed interval.** Both endpoints count as inside. `[1,4]` contains 4.
- **Overlap.** Two intervals share at least one moment. `[1,4]` and `[3,6]` overlap.
- **Touching.** They share exactly one endpoint, like `[1,2]` and `[2,3]`. Some problems call
  this overlapping, some do not. Read the statement and pick `<` versus `<=` on purpose.
- **Greedy.** Take the choice that looks best right now, commit, never revisit.
- **Locally optimal.** Best for this step alone, ignoring the future.
- **Provably safe.** You can show some perfect solution agrees with your choice.
- **Exchange argument.** The swap proof from the receptionist story.
- **Sort by start.** Used for merging, because the only interval that can overlap the current
  one is the last one you kept.
- **Sort by end.** Used for choosing, because the one finishing first leaves the most room.
- **Activity selection.** The textbook name for the receptionist problem.
- **Sweep line.** Walk through time once, reacting to +1 and −1 events in order.
- **Two pointers.** One finger on each of two sorted lists, advancing whichever is behind.
- **Farthest reach.** In jumping problems, the furthest index you could get to so far.
- **In place.** `intervals.sort()` rearranges the list you were given rather than a copy.
- **O(n log n).** The cost of sorting, and the price of admission to every problem here.

## Why the fast way is fast

The brute force for merging compares every interval with every other, and may repeat until
nothing changes. The greedy way sorts once, then passes once.

| Intervals | Compare every pair | Sort, then one pass |
|-----------|--------------------|---------------------|
| 10 | about 100 | about 40 |
| 1,000 | about 1,000,000 | about 11,000 |
| 100,000 | about 10,000,000,000 | about 1,800,000 |

At 100,000 the slow way takes minutes and the fast way a blink. What did you pay? The sort.
If the input arrives sorted, greedy is O(n), and you should say so. The other price is trust:
DP explores options and cannot be wrong; greedy commits, and is only right when you can say the
exchange sentence.

## Try it in your head

1. Requests `[1,4] [3,5] [0,6] [5,7] [8,9]`. Sort by end and pick greedily. How many fit?

<details><summary>Answer</summary>
Sorted by end: [1,4] [3,5] [0,6] [5,7] [8,9]. Take [1,4]. Skip [3,5] and [0,6], which start
before 4. Take [5,7]. Take [8,9]. Three meetings.
</details>

2. Can one person attend all of `[7,10] [2,4] [4,7]`? What do you sort by, and what do you check?

<details><summary>Answer</summary>
Sort by start: [2,4] [4,7] [7,10]. Check each start against the previous end. 4 is not less than
4, and 7 is not less than 7. No conflict, so yes, if touching does not count as overlap.
</details>

3. Coins worth 1, 3, and 4. Make 6 with as few coins as possible. Greedy says "take the biggest
   coin that fits, repeat." What does greedy give, and is it best?

<details><summary>Answer</summary>
Greedy: 4, then 1, then 1. Three coins. Best: 3 + 3, two coins. Greedy fails because the 4
cannot be swapped into the perfect answer without breaking it. No exchange argument, no greedy.
That is Chapter 10's territory.
</details>

## Common confusions, cleared

- **"If greedy is this simple, why not always use it?"** Because it is often wrong. The coin
  question is the standard counterexample. Test your greedy idea on a tiny nasty case before
  trusting it, and if you cannot say the exchange sentence, reach for DP.
- **"Sort by start or by end? I keep guessing."** Ask what the loop does. *Merges* things: sort
  by start, so the only possible overlap is the last bar. *Chooses* which to keep: sort by end,
  so each pick frees the room soonest. *Counts* how many are active: sweep line.
- **"Why does the sweep line process ends before starts at the same time?"** A meeting ending at
  10 and one starting at 10 can share a room. Count the start first and the counter briefly reads
  one too high, so you buy a room you never needed.
- **"Isn't the receptionist just picking the shortest meeting?"** No. A short meeting in the
  middle of the day can block two long ones on either side. Earliest *end* frees the room
  soonest, and that is the property the exchange argument needs.

## What to do next

Open `LESSON.md` and read §2, the merge trace, which is the calendar story with the `max` bug
caught in the act. Then read the toolkit table in §1 until "merging, choosing, counting" maps
to "start, end, sweep" without thinking. Then do `merge_intervals` and `can_attend_meetings`
in `exercises.py`. When those pass, `non_overlapping_intervals` is the receptionist and
`min_meeting_rooms` is the sweep line. Before each one, say out loud which key you sort by.
