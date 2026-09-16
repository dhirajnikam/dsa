# 11 · Greedy & Intervals

**In one sentence.** Greedy means taking the choice that looks best right now and never going
back to change it. Interval problems are where that is provably correct, as long as you sort first.

**Why you care.** Google Calendar's "find a time" button merges everyone's busy blocks and shows
the gaps. Booking rooms and scheduling shifts are greedy passes over sorted time blocks. Interview
frequency is medium-high. Amazon asks meeting rooms and merge intervals. Google asks you to prove
why the greedy choice is safe.

## The idea, with a story

You run the front desk at a company with one meeting room. Eight teams have each asked for a time
slot, and the slots overlap. Fit in as many meetings as possible. Nobody cares which teams.

Shortest meetings first? Whoever asked first? Both can be beaten. The plan that cannot be beaten:
among the requests that have not started yet, pick the one that **ends earliest**. Book it. Cross
out everything that clashes with it. Repeat. You never reconsider a booking once it is made.

Why is that safe? Suppose a perfect schedule exists that does not start with your earliest-ending
meeting. Whatever it booked first ends later than yours. Swap yours in. Yours frees the room
sooner, so nothing later in the perfect schedule is disturbed, and the count is the same. So the
perfect schedule was never better than yours.

That swap is the **exchange argument**. It is the one sentence that turns greedy from a gamble into
a proof: "If a perfect plan chose differently here, I could swap my choice in and it would still be
perfect." If you cannot say that sentence about your choice, do not trust your greedy.

## The same story with numbers

A second, smaller job. Your boss hands you busy blocks and says "show me one bar per stretch of
busy time." Sort by start, put your pen on the first block, and slide right. Each next block either
starts before your bar ends, so you stretch the bar, or starts after, so you lift the pen.

Merge `[1,3] [2,6] [8,10] [15,18]`, already sorted by start.

| Next block | Current bar | Starts at or before the bar ends? | Bar after |
|------------|-------------|-----------------------------------|-----------|
| [1,3] | none | start fresh | [1,3] |
| [2,6] | [1,3] | 2 ≤ 3, yes | [1,6] |
| [8,10] | [1,6] | 8 ≤ 6, no | finish [1,6], start [8,10] |
| [15,18] | [8,10] | 15 ≤ 10, no | finish [8,10], start [15,18] |

Result: `[1,6] [8,10] [15,18]`.

Notice the two stories sorted differently. Choosing what to keep: sort by **end**. Merging what
overlaps: sort by **start**. "By start or by end?" is the first question on any interval problem.

Pause and predict: merge `[1,10]` then `[2,3]`. What should the bar be after the second block?

<details><summary>Answer</summary>
[1,10]. The block [2,3] sits entirely inside, so the bar must not change. The trap is writing
"new end = 3" instead of "new end = the larger of 10 and 3." That missing `max` is the most common
bug in this chapter.
</details>

Now a warning. Greedy is not always right. Coins worth 1, 3, and 4. Make 6 with the fewest coins.
Greedy says "take the biggest coin that fits": 4, then 1, then 1. Three coins. The best answer is
3 + 3, two coins. The 4 cannot be swapped into the perfect answer without breaking it. No exchange
argument, no greedy. That problem belongs to dynamic programming, Chapter 10.

## The anchor problem: Merge Intervals

Given a list of closed intervals `[start, end]`, merge every pair that overlaps and return the
result sorted. Touching intervals like `[1,4]` and `[4,5]` merge.

**Brute force.** Find any overlapping pair, merge it, repeat until nothing changes. O(n²) per pass
and up to n passes.

**Insight.** Sort by start. Now the only interval that can overlap the current one is the last one
you kept. Each step is one comparison: extend it or start a new one.

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda iv: iv[0])          # sort by START
    out = []
    for start, end in intervals:
        if out and start <= out[-1][1]:           # overlaps the last kept interval
            out[-1][1] = max(out[-1][1], end)     # extend; max handles "fully inside"
        else:
            out.append([start, end])              # no overlap: start a new bar
    return out
```

**Complexity.** O(n log n) for the sort, then one O(n) pass. O(n) space for the output.

**What to say.** "I sort by start so any interval overlapping the current one must be the last one
I kept. Then one pass: if the start is at or before that end, extend with a max, otherwise start a
new interval. O(n log n) from the sort."

## Templates you memorize

**Merge: sort by start, extend with max.** The anchor above. Use it for merging, inserting, and
finding gaps.

**Choose: sort by end, take the earliest end.** Maximum non-overlapping intervals. Minimum
removals is `n - kept`. Minimum arrows is the number of groups kept.
```python
def max_non_overlapping(intervals):
    intervals.sort(key=lambda iv: iv[1])          # sort by END
    kept, last_end = 0, float("-inf")
    for start, end in intervals:
        if start >= last_end:                     # >= means touching is fine here
            kept += 1
            last_end = end
    return kept
```

**Count: sweep line with +1 and −1 events.** Rooms needed, maximum concurrent anything.
```python
def min_meeting_rooms(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))                 # a meeting begins
        events.append((end, -1))                  # a meeting ends
    events.sort()                                 # (t, -1) sorts before (t, +1): free first
    rooms = best = 0
    for _, delta in events:
        rooms += delta
        best = max(best, rooms)
    return best
```
For `[0,30] [5,10] [15,20]` the counter reads 1, 2, 1, 2, 1, 0. Peak is 2, so two rooms.

**Insert into a sorted, disjoint list.** Three phases: before, overlapping, after.
```python
def insert_interval(intervals, new):
    out, i, n = [], 0, len(intervals)
    while i < n and intervals[i][1] < new[0]:     # entirely before the new one
        out.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new[1]:    # overlaps: absorb into new
        new = [min(new[0], intervals[i][0]), max(new[1], intervals[i][1])]; i += 1
    out.append(new)
    out.extend(intervals[i:])                     # entirely after
    return out
```

**Farthest reach (Jump Game).** Keep the farthest index you can reach. If you pass it, you are stuck.
```python
def jump_game(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True
```

## When you see X, think Y

| You see | Think |
|---------|-------|
| "merge overlapping", "insert an interval", "free time" | sort by start, extend with `max` |
| "maximum non-overlapping", "minimum to remove", "minimum arrows" | sort by end, take earliest end |
| "how many rooms at the same time" | sweep line +1/−1 |
| "can attend all", "any conflict?" | sort by start, check `start < previous end` |
| "two sorted lists of intervals" | two pointers, advance the one that ends first |
| "can I reach the end", "minimum jumps" | farthest reach |
| "circular route, tank, deficit" | one pass, reset start when the tank goes negative |
| "each letter in only one part" | last index of each letter, cut when `i == end` |
| "assign to minimize cost, fixed group sizes" | sort by the cost difference |

## Words you will hear

- **Interval.** A start and an end, written `[start, end]`. A meeting, a busy block.
- **Overlap.** Two intervals share at least one moment. `[1,4]` and `[3,6]` overlap.
- **Touching.** They share exactly one endpoint, like `[1,2]` and `[2,3]`. Some problems count
  this as overlap, some do not. Read the statement and pick `<` or `<=` on purpose.
- **Greedy.** Take the choice that looks best now, commit, never revisit.
- **Exchange argument.** The swap proof from the receptionist story.
- **Activity selection.** The textbook name for the receptionist problem.
- **Sweep line.** Walk through time once, reacting to +1 and −1 events in order.
- **In place.** `intervals.sort()` rearranges the list you were given, not a copy.

## Mistakes everyone makes once

- **Sorting by the wrong key.** Merging needs start. Choosing needs end. Check this first when a
  test fails.
- **Forgetting `max` when extending.** `[1,10]` then `[2,3]` must stay `[1,10]`.
- **Touching intervals.** Decide `<` versus `<=` from the problem statement, and say the choice
  out loud.
- **Greedy without a reason.** "It worked on the example" is not an argument. Say the exchange
  sentence. If you cannot, think DP.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `merge_intervals` | Medium | The anchor. Sort by start, extend with `max`. |
| 2 | `insert_interval` | Medium | Three phases: before, overlapping, after. |
| 3 | `non_overlapping_intervals` | Medium | Sort by end, count what you keep. Answer is `n - kept`. |
| 4 | `can_attend_meetings` | Easy | Sort by start. Any `start < previous end` is a conflict. |
| 5 | `min_meeting_rooms` | Medium | Sweep line. Ends before starts at the same time. |
| 6 | `jump_game` | Medium | Farthest reachable index. Fail if `i > reach`. |
| 7 | `jump_game_ii` | Medium | Levels without a queue. Jump when `i == cur_end`, new edge is the farthest seen. |
| 8 | `gas_station` | Medium | If total gas < total cost, return -1. Otherwise reset the start when the tank goes negative. |
| 9 | `hand_of_straights` | Medium | `Counter`. Always start a run at the smallest remaining card. |
| 10 | `partition_labels` | Medium | Last index of each letter. Extend `end`. Cut when `i == end`. |
| 11 | `valid_parenthesis_string` | Medium | Track `lo` and `hi` open counts. `*` widens both. Clamp `lo` at 0. |
| 12 | `min_arrows_burst_balloons` | Medium | Sort by end. New arrow when `start > last_arrow`. |
| 13 | `assign_cookies` | Easy | Sort both. Smallest cookie that satisfies the least greedy child. |
| 14 | `two_city_scheduling` | Medium | Sort by `a - b`. First half to A, second half to B. |
| 15 | `interval_intersections` | Medium | Two pointers. Advance the interval that ends first. |

Start with 1 and 4 today. Then 3 and 5, the receptionist and the sweep line. Do 2 and 6 to 13 over
the week. 14 and 15 are for when the rest pass cold.
