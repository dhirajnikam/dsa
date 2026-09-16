# 11 · Greedy & Intervals

> A greedy algorithm makes the choice that looks best right now and never looks back. That is
> reckless in general and exactly right in a handful of situations. The skill is not writing
> the loop; it is knowing, and being able to say, why the loop is safe.

**Interview frequency:** medium-high. Interval problems are Amazon staples (meeting rooms,
merge intervals, scheduling). Google likes the proof: "why does taking the earliest end
work?" Expect a greedy problem to be short on code and long on justification.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

Greedy means making the choice that looks best right now and never going back to change it,
and interval problems are where that recklessness is provably correct, as long as you sort first.

### Start with something you already do

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

### Now the same thing with numbers

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

### The words people use

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

### Why the fast way is fast

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

### Try it in your head

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

### Common confusions, cleared

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

### What to do next

Open Part 2 below and read Part 2 §2, the merge trace, which is the calendar story with the `max` bug
caught in the act. Then read the toolkit table in Part 2 §1 until "merging, choosing, counting" maps
to "start, end, sweep" without thinking. Then do `merge_intervals` and `can_attend_meetings`
in `exercises.py`. When those pass, `non_overlapping_intervals` is the receptionist and
`min_meeting_rooms` is the sweep line. Before each one, say out loud which key you sort by.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** Google Calendar's "find a time" button is an interval
problem: overlay everyone's busy blocks, merge them, and the gaps are the free slots. Booking
a room is `min_meeting_rooms` with real furniture. Amazon schedules warehouse shifts and hands
delivery windows to drivers with greedy passes over sorted time blocks. Your operating system
picks the next job to run the same way. Every zip file you have ever opened was built by
Huffman coding, a greedy algorithm that always merges the two rarest symbols first. Greedy is
what production systems use when they need a good answer now and can prove it is the best one.

**The analogy.** A receptionist seating guests at a single table. Each guest has an arrival
and a departure time. To host the most guests in one evening, she seats whoever leaves
earliest, then whoever leaves earliest among those arriving after that, and so on. She never
reconsiders. If some longer-staying guest would have been "better," she can swap that guest
out for the early leaver and lose nothing, because the early leaver frees the chair sooner.
That swap is the entire theory of this chapter.

**How it works, in plain words.** Sort the intervals so that time flows left to right. Then
walk once, carrying one piece of state: the last interval you kept. Each new interval either
conflicts with it or does not, and you decide on the spot. Merging sorts by start, because the
only thing that can overlap you is the one you just kept. Choosing the most non-overlapping
sorts by end, because the one finishing first leaves the most room. Counting overlap turns
each interval into a +1 and a -1 event and runs a counter. Three tools, one sort, one pass.

**What learning this will feel like.** Greedy will feel like guessing. You will write a loop
that passes the examples and have no idea whether it is correct, and that uncertainty is
uncomfortable in a way DP never is. This is normal: the code is trivial and the reasoning is
the whole exercise. The aha arrives when you can say the exchange sentence out loud: "if the
optimal solution made a different choice here, I could swap in mine and be no worse." Once
that sentence is in your mouth, greedy stops being a gamble and becomes a proof. Expect one
memorable bug: merging `[1,10]` and `[2,3]` into `[1,3]` because you forgot the `max`. The
trace in section 2 catches it. Next time you will catch it yourself.

**You will know you have it when** the word "intervals" makes you sort before you think, and
your first question is "by start or by end?"

### 1. The core idea

Greedy means: at each step, take the locally optimal choice, and that choice is **provably
safe**, meaning some optimal solution agrees with it. No branching, no memo table, usually
one pass after a sort.

How to justify a greedy choice in one sentence, the **exchange argument**: "Take any optimal
solution that does not make my choice; swap in my choice; the result is no worse. So my choice
is safe." If you cannot say that sentence about your choice, you probably need DP instead.

Intervals are the natural home of greedy because sorting lines them up so a single sweep
sees every conflict. Compare the brute force with the pattern:

```
brute force: compare every pair               sorted sweep
for i in range(n):                            intervals.sort()
    for j in range(n):                        for cur in intervals:
        if i != j and overlaps(a[i], a[j])        if cur.start <= out[-1].end:  # overlap
            merge / count / remove...                 extend out[-1]
                                                  else: out.append(cur)
O(n²), and merging chains is fiddly          O(n log n), one pass, chains merge for free
```

**The interval toolkit.** Three tools cover almost every interval problem.

| Tool | When | Why it works |
|------|------|--------------|
| **Sort by start**, sweep and merge | merging, inserting, finding gaps | After sorting, the only interval that can overlap the current one is the last one kept. |
| **Sort by end**, take the earliest end | "max non-overlapping", "min removals", "min arrows" | The interval ending first leaves the most room for the rest. Exchange argument: swap any optimal first pick for the earliest-ending one and nothing else breaks. |
| **Sweep line** with +1 / −1 events | "max concurrent", "rooms needed", "at time t how many" | Turn every interval into two events, sort them, run a counter. The max the counter reaches is the answer. |

Rule of thumb: **merging → sort by start; choosing → sort by end; counting overlap → sweep.**

### 2. Anchor problem: Merge Intervals, fully worked

**Problem.** Given a list of closed intervals `[start, end]`, merge every pair that overlaps
and return the result in sorted order.

**Understand.** Do touching intervals like `[1,4]` and `[4,5]` merge? Yes, they share the
point 4. Is the input sorted? No. Can the list be empty? Yes, return `[]`. Can one interval be
fully inside another? Yes, `[1,10]` and `[2,3]` → `[1,10]`.

**Examples.** `[[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]`. `[[1,4],[4,5]] → [[1,5]]`.
`[[1,4],[0,4]] → [[0,4]]`.

**Brute force.** Repeatedly find any overlapping pair and merge it until none remain. Each
pass is O(n²) and there can be O(n) passes. Say it and leave it.

**Insight.** Sort by start. Now walk left to right. The current interval can only overlap the
**last interval I kept**, because everything before that ends earlier than that one and
starts earlier than the current one. So each step is one comparison: extend or append.

**Code.**

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda iv: iv[0])
    out = []
    for start, end in intervals:
        if out and start <= out[-1][1]:            # overlaps the last kept interval
            out[-1][1] = max(out[-1][1], end)      # extend; max handles "fully inside"
        else:
            out.append([start, end])
    return out
```

**Test trace.** `[[1,3],[2,6],[8,10],[15,18]]`, already sorted.

```
cur      out before             overlap?          out after
[1,3]    []                     no (empty)        [[1,3]]
[2,6]    [[1,3]]                2 <= 3  yes       [[1,6]]        end = max(3, 6)
[8,10]   [[1,6]]                8 <= 6  no        [[1,6],[8,10]]
[15,18]  [[1,6],[8,10]]         15 <= 10 no       [[1,6],[8,10],[15,18]]
```

And `[[1,4],[2,3]]`: `[2,3]` overlaps, end becomes `max(4, 3) = 4`. Without the `max` you would
shrink the interval to `[1,3]`. That is the bug the trace catches.

**Complexity.** O(n log n) for the sort, O(n) for the sweep. O(n) space for the output (O(1)
extra if the interviewer lets you reuse the input).

**What to say out loud.** "I sort by start so that any interval overlapping the current one
must be the last one I kept. Then one pass: if the start is at or before that end, extend the
end with a max; otherwise start a new interval. O(n log n) from the sort."

### 3. Patterns and templates in this chapter

#### Sort by end, take the earliest end (activity selection)

Maximum number of non-overlapping intervals. Everything else in this family is one line away:
minimum removals = `n - max_kept`; minimum arrows = number of groups kept.

```python
def max_non_overlapping(intervals):
    intervals.sort(key=lambda iv: iv[1])          # by END
    kept, last_end = 0, float("-inf")
    for start, end in intervals:
        if start >= last_end:                     # >= : touching does not overlap here
            kept += 1
            last_end = end
    return kept
```

Watch the boundary. "Non-overlapping" in `non_overlapping_intervals` treats `[1,2],[2,3]` as
fine (`>=`). "One arrow bursts both" in `min_arrows_burst_balloons` treats `[1,2],[2,3]` as
overlapping (`>`). Read the statement and pick the comparison on purpose.

#### Sweep line: +1 / −1 events

Minimum meeting rooms, maximum concurrent anything.

```python
def min_meeting_rooms(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))                 # a meeting begins
        events.append((end, -1))                  # a meeting ends
    events.sort()                                 # (t, -1) sorts before (t, +1): frees first
    rooms = best = 0
    for _, delta in events:
        rooms += delta
        best = max(best, rooms)
    return best
```

The tuple sort puts an end at time `t` before a start at time `t`, so back-to-back meetings
share a room. If your problem says touching intervals *do* conflict, flip the event codes.
Chapter 07 solves the same problem with a min-heap of end times; both are O(n log n).

#### Insert one interval into a sorted, disjoint list

Three phases: everything that ends before the new one, everything that overlaps (merge into
the new one), everything that starts after it.

```python
def insert_interval(intervals, new):
    out, i, n = [], 0, len(intervals)
    while i < n and intervals[i][1] < new[0]:     # entirely before
        out.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new[1]:    # overlaps: absorb
        new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]; i += 1
    out.append(new)
    out.extend(intervals[i:])                     # entirely after
    return out
```

#### Two pointers over two sorted lists (interval intersections)

Intersect the current pair, then advance whichever interval **ends first**, because it cannot
intersect anything further in the other list.

```python
def interval_intersections(a, b):
    i = j = 0; out = []
    while i < len(a) and j < len(b):
        lo, hi = max(a[i][0], b[j][0]), min(a[i][1], b[j][1])
        if lo <= hi:
            out.append([lo, hi])
        if a[i][1] < b[j][1]: i += 1
        else: j += 1
    return out
```

#### Farthest reach (Jump Game)

Keep the farthest index you can reach so far. If your position ever passes it, you are stuck.

```python
def jump_game(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True
```

Minimum jumps: treat it as BFS by levels without a queue. `cur_end` is the edge of the
current level; when you hit it, one more jump and the new edge is the farthest seen.

#### Reset the running total (Gas Station)

If the total gas is at least the total cost, exactly one start works. Walk once; whenever the
tank goes negative, no station in the stretch you just walked can be the start, so restart
from the next one. Exchange argument: any start inside a failing stretch has strictly less
gas at the failure point.

#### Last occurrence (Partition Labels)

Precompute the last index of each character. Sweep, extending the current partition's end to
`last[c]` for each character seen; when `i == end`, cut.

#### Range of possible counts (Valid Parenthesis String with `*`)

Track the minimum and maximum number of unmatched `(` that could be open. `(` adds one to
both, `)` subtracts one from both, `*` widens the range by one each way. Clamp `lo` at 0
(extra `)` may have been `*` treated as empty), and fail if `hi` ever goes negative.

#### Smallest first with a Counter (Hand of Straights)

Always start a group at the smallest remaining card, because nothing else can cover it.
Exchange argument: the smallest card must begin some group in any valid grouping.

#### Sort by the cost difference (Two City Scheduling)

Send everyone to A, then move the `n` people whose `costB - costA` is smallest to B. Sorting by
the *difference* is the whole trick; the exchange argument is swapping two people between
cities and seeing the total cannot improve.

### 4. Recognition cues

| You see | Think |
|---------|-------|
| "merge overlapping", "insert an interval", "free time / gaps" | sort by start, sweep, extend with `max` |
| "maximum non-overlapping", "minimum to remove", "minimum arrows / points" | sort by end, take earliest end |
| "how many rooms / machines / at the same time" | sweep line +1/−1, or heap of ends (Chapter 07) |
| "can attend all", "any conflict?" | sort by start, check `cur.start < prev.end` |
| "two sorted lists of intervals" | two pointers, advance the one that ends first |
| "can I reach the end", "minimum jumps" | farthest reach; levels for min jumps |
| "circular route, tank, deficit" | one pass, reset start when running total goes negative |
| "partition so each letter appears in one part" | last occurrence, cut when `i == end` |
| "wildcard that can be either" | track a range `[lo, hi]` of possibilities |
| "groups of consecutive values" | `Counter`, always start from the smallest remaining |
| "assign to minimize total cost, fixed group sizes" | sort by cost difference |
| "each child gets at most one", "match smallest to smallest" | sort both, two pointers |

### 5. Pitfalls

- **Sorting by the wrong key.** Merging needs start; choosing needs end. If your greedy is
  wrong on a test, this is the first thing to check.
- **Touching intervals.** `[1,2]` and `[2,3]` overlap in some problems and not in others. Decide
  `<` vs `<=` from the statement and say the choice aloud.
- **Forgetting `max` when extending.** `[1,10],[2,3]` must stay `[1,10]`.
- **Sweep-line tie order.** Ends before starts at equal time, or you will count a room that was
  just freed. The `(t, -1) < (t, +1)` tuple trick handles it; `(t, "end")` vs `(t, "start")`
  does not (`"end" < "start"` happens to work, but say why).
- **Greedy without a reason.** "It seemed to work on the example" is not an argument. Give the
  exchange sentence. If you cannot, consider DP (Chapter 10).
- **Mutating the input.** `intervals.sort()` sorts in place. Fine in interviews, but mention it,
  or use `sorted(...)`.
- **Jump Game II off-by-one.** Do not jump at the last index; loop `range(len(nums) - 1)`.
- **Gas Station.** Check `sum(gas) >= sum(cost)` or your reset loop returns a start that does
  not actually complete the circuit.

### 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|----------|-----------|----------|----------|
| 1 | `merge_intervals` | Medium | Amazon, Google | The anchor. Sort by start, extend with `max`. |
| 2 | `insert_interval` | Medium | Google, Amazon | Three phases: before, overlapping (absorb), after. |
| 3 | `non_overlapping_intervals` | Medium | Amazon, Google | Sort by end, count what you can keep; answer is `n - kept`. |
| 4 | `can_attend_meetings` | Easy | Amazon | Sort by start; any `start < previous end` is a conflict. |
| 5 | `min_meeting_rooms` | Medium | Amazon, Google | Sweep line. Ends before starts at the same time. |
| 6 | `jump_game` | Medium | Amazon, Google | Farthest reachable index; fail if `i > reach`. |
| 7 | `jump_game_ii` | Medium | Amazon, Google | BFS levels without a queue: `cur_end`, `farthest`, jump when `i == cur_end`. |
| 8 | `gas_station` | Medium | Amazon, Google | If total gas < total cost, -1. Otherwise reset the start whenever the tank goes negative. |
| 9 | `hand_of_straights` | Medium | Google | `Counter`; repeatedly start a run at the smallest remaining key. |
| 10 | `partition_labels` | Medium | Amazon | `last[c]`; extend `end`; cut when `i == end`. |
| 11 | `valid_parenthesis_string` | Medium | Google, Amazon | `lo`/`hi` open count; `*` widens both; clamp `lo` at 0; `hi < 0` fails. |
| 12 | `min_arrows_burst_balloons` | Medium | Google | Sort by end; new arrow when `start > last_arrow`. |
| 13 | `assign_cookies` | Easy | Amazon | Sort both; smallest cookie that satisfies the least greedy child. |
| 14 | `two_city_scheduling` | Medium | Amazon, Google | Sort by `a - b`; first half to A, second half to B. |
| 15 | `interval_intersections` | Medium | Google, Amazon | Two pointers; advance the interval that ends first. |

Solve 1–8 in order, then 9–13. 14–15 are the stretch set; do them when the rest pass cold.
