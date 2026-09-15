# Phase 12: Heaps & Intervals

**Goal:** reach for `heapq` on any "k largest / closest / most frequent / merge k / median" problem, and sort intervals by start first.

## Key idea
A heap is a list whose smallest item is always at index 0. Push and pop cost O(log n).
Python only has a min-heap, so for a max-heap push negative numbers. For "top k", keep a
heap of size k. Intervals: sort by start, walk once. Overlap means `start <= last_end`.

## Cheat sheet
```python
import heapq
h = []
heapq.heappush(h, (priority, item))  # tuples compare by first element
smallest = heapq.heappop(h)          # h[0] peeks without popping

for x in nums:                       # k largest: root of a size-k min-heap
    heapq.heappush(h, x)
    if len(h) > k: heapq.heappop(h)

intervals.sort()                     # merge overlapping
out = [intervals[0]]
for s, e in intervals[1:]:
    if s <= out[-1][1]: out[-1][1] = max(out[-1][1], e)
    else: out.append([s, e])
```

## When you see... use...
- "k largest / smallest / closest / most frequent" -> heap of size k
- "merge k sorted lists" -> heap with one entry per list `(value, list_index, node)`
- "median of a stream" -> two heaps: max-heap for low half, min-heap for high half
- "minimum meeting rooms" -> sort by start, min-heap of end times
- "remove fewest intervals so none overlap" -> sort by end, keep greedily

## Common mistakes
- No max-heap in Python. Negate values.
- Tuples with equal priority compare the payload next. Add an index: `(dist, i, obj)`.
- `h[-1]` is not the max. Only `h[0]` is meaningful.
- `[1,2]` and `[2,3]` touch. Merge-intervals joins them, meeting rooms does not.

## Problems
- `01_kth_largest_element.py` — size-k min-heap
- `02_k_closest_points.py` — size-k max-heap on distance
- `03_top_k_frequent_heap.py` — Counter, then heap of `(count, value)`
- `04_merge_k_sorted_lists.py` — one heap entry per list
- `05_task_scheduler.py` — max-heap of counts plus cooldown queue
- `06_find_median_data_stream.py` — two heaps, rebalance each add
- `07_merge_intervals.py` — sort by start, extend the last one
- `08_non_overlapping_intervals.py` — sort by end, greedy keep
- `09_meeting_rooms_ii.py` — min-heap of end times
