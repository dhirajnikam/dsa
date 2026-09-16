# 07 · Heaps

**In one sentence.** A heap is a container that always knows which item is smallest without
keeping everything sorted, so you can add items and pull out the top one very quickly.

**Why you care.** Your operating system picks the next process with a heap. Google Maps keeps a
heap of "closest unexplored intersection." Interview frequency is medium but concentrated.
Amazon asks Top-K and "merge k sorted" constantly. Google likes the two-heap median.

## The idea, with a story

Picture a hospital emergency room. Patients arrive all day. The sickest patient is seen next, no
matter when they walked in. When a new patient arrives, the nurse does not re-sort the whole
waiting room. They rank the newcomer against a few people and slot them in. When the doctor is
free, the nurse asks one question: "who is the sickest right now?" One glance answers it.

That is the whole chapter. You do not need everyone sorted. You only need the top one to be
correct.

A second picture shows how the heap keeps the top correct cheaply. A tournament bracket. The
champion sits at the top, the two finalists below, the four semi-finalists below those. A new
player joins. You do not replay the tournament. The newcomer starts at the bottom and plays
upward along one path, beating whoever they are worse than, until they lose. Everyone on the
other paths is untouched. For a million players that path is about twenty matches.

## The same story with numbers

A min-heap is a bracket where the smallest number wins each match. The only rule: every parent
is smaller than its two children. Nothing else is promised.

Start with `[2, 5, 4]` and add `1`. It goes at the bottom, then climbs one path.

```
      2              2              2              1
     / \    add 1   / \    swap    / \    swap    / \
    5   4   --->   5   4   --->   1   4   --->   2   4
                  /              /              /
                 1              5              5
```

The 1 beat 5, then beat 2, and stopped at the top. The 4 was never asked to play. Python stores
this as a plain list, `[1, 2, 4, 5]`, where the children of position `i` sit at `2i + 1` and
`2i + 2`.

Removing the top is the reverse. Move the last item to the top, then let it sink down past
whichever child is smaller.

Pause and predict: after removing 1 from `[1, 2, 4, 5]`, what does the list look like?

<details><summary>Answer</summary>
Move 5 to the top: `[5, 2, 4]`. 5 is bigger than its smaller child 2, so swap: `[2, 5, 4]`.
5 has no children now, so stop. The new top is 2, the correct next-smallest.
</details>

## The anchor problem: Kth Largest

Given an unsorted array and `k`, return the kth largest element. Duplicates count separately.

**Brute force.** Sort and index: `sorted(nums)[-k]`. O(n log n). Say it and ask "should I do better?"

**Insight.** I do not need all n elements sorted. I need only the k largest. Keep a VIP room of
size k. When someone new arrives, let them in. If the room is now over capacity, kick out the
smallest person. The room is a min-heap even though you want the largest, because the person
you must find instantly is the smallest survivor, the one to evict.

```python
import heapq

def kth_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)        # evict the smallest; it cannot be in the top k
    return heap[0]                     # the smallest survivor is the kth largest
```

Trace `[3, 2, 1, 5, 6, 4]`, k = 2. Room after each arrival: {3}, {2, 3}, {2, 3}, {3, 5},
{5, 6}, {5, 6}. Answer 5.

**Complexity.** O(n log k) time, O(k) space. For the top ten of a million, nearly linear.

**What to say.** "Sorting is O(n log n). I only need the top k, so a min-heap of size k gives
O(n log k). Whenever the heap exceeds k, I pop the smallest, which cannot be in the top k."

## Templates you memorize

**Min-heap of size k for "k largest".** For "k smallest," negate. For "k closest," the priority
is the distance.
```python
heap = []
for x in items:
    heapq.heappush(heap, (priority(x), x))
    if len(heap) > k:
        heapq.heappop(heap)
```
`heapq.nlargest(k, items, key=...)` does the same in one line.

**Negate for a max-heap.** `heapq` is min-only. Push `-x`. Pop and flip back.
```python
heap = [-x for x in nums]
heapq.heapify(heap)                    # O(n) for a whole list
largest = -heapq.heappop(heap)
```

**Tuple priorities with a tie-breaker.** Python compares tuples left to right. When the payload
cannot be compared, like a tree node, put a unique integer in the middle so the comparison never
reaches it.
```python
heapq.heappush(heap, (value, list_index, element_index))
```
This is exactly what merging k sorted lists needs. Pop one, push that list's next item.

**Two heaps for a running median.** The small half lives in a max-heap (`low`, negated). The
large half lives in a min-heap (`high`). The median is the top of `low`, or the average of both
tops when the count is even.
```python
def add(x):
    heapq.heappush(low, -x)                          # 1. into low
    heapq.heappush(high, -heapq.heappop(low))        # 2. low's max moves to high
    if len(high) > len(low):                         # 3. keep low at least as big
        heapq.heappush(low, -heapq.heappop(high))
```
Three lines, always in this order. Never skip step 2.

## When you see X, think Y

| You see | Think |
|---------|-------|
| "k largest", "k most frequent", "k closest" | min-heap of size k, O(n log k) |
| "stream", "add one, query the top" | keep the heap alive between calls |
| "median of a stream" | two heaps, low max-heap and high min-heap |
| "merge k sorted ..." | one head per list in a heap, tuple with indices |
| "smallest in a sorted matrix" | same as merge k sorted, one head per row |
| "minimum rooms / machines" | sort by start, heap of end times |
| "no two adjacent the same", "cooldown" | max-heap of counts, hold back the one just used |
| "repeatedly combine the two largest" | max-heap, pop two, push the result |

## Words you will hear

- **Heap.** A list arranged so every parent beats its children. Python's is `heapq`.
- **Min-heap, max-heap.** Smallest on top, or largest. Python only ships min.
- **Priority queue.** "Always give me the most important item next." A heap is how you build one.
- **Push, pop.** Add at the bottom and climb. Remove the top and let the last item sink.
- **`heapify`.** Turn a whole list into a heap at once. O(n), faster than pushing one by one.
- **Negate.** Push `-x` so a min-heap acts like a max-heap. Flip back on pop.
- **Top-K.** The k best items. The heap's home turf.

## Mistakes everyone makes once

- **Forgetting to negate on the way out.** Negate on push and on pop, both times, or you hand
  back a negative stone.
- **Reading `heap[1]`.** Only `heap[0]` is guaranteed. `heap[1]` is one of two children, not the
  second smallest.
- **Pushing a tuple whose payload cannot be compared.** `(3, node)` crashes on a tie. Add an
  integer tie-breaker in the middle.
- **Using a heap when you need sorted order.** Popping everything costs the same as sorting,
  with more code.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `KthLargest` | Easy | The anchor as a class. Keep the heap at size k between calls. |
| 2 | `kth_largest` | Medium | Min-heap of size k. Then read about quickselect in solutions.py. |
| 3 | `last_stone_weight` | Easy | Max-heap. Pop two, push the difference if non-zero. |
| 4 | `k_closest_points` | Medium | Max-heap of size k on squared distance, negated. No `sqrt`. |
| 5 | `top_k_frequent_heap` | Medium | `Counter`, then min-heap of `(count, value)` size k. |
| 6 | `task_scheduler` | Medium | Max-heap of counts. Each round pulls up to `n + 1` tasks. Pad with idle unless last. |
| 7 | `MedianFinder` | Hard | Two heaps. Push to low, move top to high, rebalance. |
| 8 | `merge_k_sorted` | Medium | Heap of `(val, list_idx, elem_idx)`. Pop one, push that list's next. |
| 9 | `reorganize_string` | Medium | Max-heap of counts. Pop the most frequent that is not the char just placed. |
| 10 | `meeting_rooms_ii` | Medium | Sort by start. Heap of end times. Pop if `end <= start`. Peak heap size. |
| 11 | `kth_smallest_in_sorted_matrix` | Medium | Row heads in a heap: `(val, row, col)`. Pop k times. |
| 12 | `smallest_range_covering_k_lists` | Hard | One pointer per list in a min-heap. Track the current max. Advance the min. |

Do 1 and 3 today with a 30-minute timer. The first is the VIP room as a class, the second is
the sign flip. Then 8, which makes tuple priorities click. 2 to 10 over the week. 11 and 12 are
for when the rest pass cold.
