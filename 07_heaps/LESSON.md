# 07 · Heaps

*New to this topic? Read `THEORY.md` in this folder first. It explains the idea from zero.*

> A heap answers one question fast: "what is the smallest thing I have right now?" It does not
> sort. It does not search. It gives you the minimum in O(1) and lets you insert or remove in
> O(log n). When a problem repeatedly asks for the current smallest, largest, earliest, or
> closest, that is the whole hint.

**Interview frequency:** medium, but concentrated. Amazon asks Top-K and "merge k sorted"
constantly. Google likes the two-heap median and scheduling problems where a heap holds
"what is available right now."

## 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** A hospital emergency room does not treat patients in
arrival order. It treats the most urgent one next, and a new arrival only needs ranking, not a
re-sort of the whole waiting room. Your operating system's CPU scheduler does the same with
processes. Dijkstra's algorithm inside Google Maps keeps a heap of "closest unexplored
intersection" and pops it millions of times per route. Amazon's "top sellers" list is a heap of
size k over a firehose of sales events. Monitoring dashboards that show a live median response
time use the two-heap trick from exercise 7, `MedianFinder`.

**The analogy.** A tournament bracket. The champion is at the top, and to know who it is you
look at exactly one spot. Suppose the champion retires. You do not replay the tournament. You
re-run only the matches along one path from the bottom to the top, about log n of them, and a
new champion appears. A new player climbs one path upward, beating whoever they are better
than, until they stop. Everyone else's position is untouched.

**How it works, in plain words.** A heap is an array arranged so that every parent is smaller
than its two children. Nothing else is promised: the second smallest could be at index 1 or
index 2. Because the rule holds at every level, the smallest element is always at the front. To
insert, append to the end and swap upward while smaller than the parent. To remove the minimum,
move the last element to the front and swap downward. Each swap moves one level, and n items
make about log n levels, so both operations cost log n. Python ships this as `heapq`.

**What learning this will feel like.** The first instinct is to keep everything sorted, because
sorted feels safe. Then you meet the anchor, `kth_largest`, and see that sorting costs n log n
while a heap of size k costs n log k, which for the top ten of a million is enormous. The aha:
you only ever need the top, so only the top needs to be right. Expect the confusion everyone
shares: for the k largest you keep a *min*-heap, because what you evict is the smallest
survivor. And expect the bug everyone writes: `heapq` is min-only, so a max-heap means pushing
`-x` and negating again on the way out. Forget the second negation once and you will never
forget it again.

**You will know you have it when** the words "k most" or "repeatedly take the smallest" make
you type `import heapq` before you have read the rest of the problem.

## 1. The core idea

A binary heap is an array that pretends to be a tree: the children of index `i` live at
`2i + 1` and `2i + 2`. The one rule is that every parent is ≤ its children (min-heap). The
minimum is therefore always at index 0. Insert by appending and bubbling up; remove the
minimum by moving the last element to the root and sifting down. Both are O(log n) because
the tree has height log n.

Python gives you this as `heapq`, min-heap only. You will never implement one in an
interview, but you must be able to say how it works in three sentences.

```
sort to find the k largest             heap of size k
nums.sort()                            heap = []
return nums[-k:]                       for x in nums:
                                           heappush(heap, x)
                                           if len(heap) > k:
                                               heappop(heap)     # drop the smallest
                                       return heap               # the k largest survive
O(n log n)                             O(n log k)
```

The recognition cue: **"k largest / smallest / closest / most frequent," or "repeatedly take
the smallest of what is available."** If k is small relative to n, the heap wins. If you
need the full sorted order, just sort.

## 2. Anchor problem: Kth Largest Element in an Array, fully worked

**Problem.** Given an unsorted array `nums` and an integer `k`, return the kth largest
element in sorted order (not the kth distinct element).

**Understand.** "Kth largest in sorted order": in `[3, 2, 3, 1, 2, 4, 5, 5, 6]`, sorted
descending is `[6, 5, 5, 4, 3, 3, 2, 2, 1]`, and k=4 gives 4. Duplicates count separately.
`1 <= k <= len(nums)` always, so no empty case.

**Examples.** `[3, 2, 1, 5, 6, 4], 2 → 5`. `[3, 2, 3, 1, 2, 4, 5, 5, 6], 4 → 4`.
`[1], 1 → 1`.

**Brute force.** Sort and index: `sorted(nums)[-k]`. O(n log n) time. Correct and short. In
an interview, write it, say the complexity, and ask "should I do better?" They will say yes.

**Insight, first improvement.** I do not need all n elements sorted; I need only the k
largest. Keep a min-heap of at most k elements. When it grows past k, pop the smallest. After
the pass, the heap holds exactly the k largest, and its minimum is the kth largest.

**Code.**

```python
import heapq

def kth_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)           # evict the smallest; it cannot be in the top k
    return heap[0]
```

**Test.** `[3, 2, 1, 5, 6, 4], k=2`: push 3 → [3]. push 2 → [2, 3]. push 1 → [1, 2, 3], too
big, pop 1 → [2, 3]. push 5 → [2, 3, 5], pop 2 → [3, 5]. push 6 → [3, 5, 6], pop 3 → [5, 6].
push 4 → [4, 5, 6], pop 4 → [5, 6]. `heap[0]` = 5. ✓

**Complexity.** O(n log k) time, O(k) space. When k is small this is nearly linear.

**Insight, second improvement: quickselect.** Pick a pivot, partition so that larger
elements go left and smaller go right (like one round of quicksort). If the pivot lands at
index k-1, it is the answer. Otherwise recurse into only the side that contains index k-1.
Average O(n) because each round discards a constant fraction; worst case O(n²) with bad
pivots, which a random pivot makes vanishingly unlikely. `solutions.py` shows both; mention
quickselect and let the interviewer choose.

**What to say out loud.** "Sorting is O(n log n). I only need the top k, so a min-heap of size
k gives O(n log k): every element is pushed, and whenever the heap exceeds k, I pop the
smallest, which cannot be in the top k. The root is the answer. If you want average O(n),
quickselect partitions around a random pivot and recurses into one side only."

## 3. Patterns and templates in this chapter

### Min-heap of size k for "k largest"

The anchor. Counterintuitive the first time: to keep the largest, you use a *min*-heap, so
that the element you can evict in O(1) is the smallest survivor. For "k smallest," use a
max-heap of size k (negate). For "k closest to a point," the priority is the distance.

```python
heap = []
for x in items:
    heapq.heappush(heap, (priority(x), x))
    if len(heap) > k:
        heapq.heappop(heap)
```

`heapq.nlargest(k, items, key=...)` does the same thing in one line. Know it, and know that
it is O(n log k) inside.

### Negate for a max-heap

`heapq` is min-only. Push `-x`, pop and negate back. For tuples, negate the first field.

```python
heap = [-x for x in nums]
heapq.heapify(heap)                    # O(n), not O(n log n)
largest = -heapq.heappop(heap)
```

`heapify` on a whole list is O(n). Pushing one at a time is O(n log n). If you already have
all the elements, heapify.

### Tuple priorities with tie-breakers

Python compares tuples left to right. `(count, char)` sorts by count, then by char. When the
payload is not comparable (a list, a node), put a unique integer in the middle as a tie-breaker
so the comparison never reaches it:

```python
heapq.heappush(heap, (value, list_index, element_index))    # never compares the list itself
```

This is exactly what merging k sorted lists needs: the value to order by, and enough indices to
know where to fetch the next element.

### Two heaps for a running median

Keep the smaller half in a max-heap (`low`, negated) and the larger half in a min-heap
(`high`). The median is the top of `low` (odd count) or the average of both tops (even).
Rebalance so that `len(low) == len(high)` or `len(low) == len(high) + 1`.

```python
def add(x):
    heapq.heappush(low, -x)                          # 1. into low
    heapq.heappush(high, -heapq.heappop(low))        # 2. low's max moves to high
    if len(high) > len(low):                         # 3. keep low at least as big
        heapq.heappush(low, -heapq.heappop(high))
```

Three lines, always in this order, and the invariant `max(low) <= min(high)` holds without
any comparisons of your own.

### Heap as "what is available right now"

Scheduling problems: sort events by start, walk them in order, keep a heap of things that are
busy keyed by when they free up. Before handling an event, pop everything that has finished.
Meeting Rooms II is "heap of end times": a room is free if its end ≤ the next start. The heap
size at its peak is the answer.

For "greedy with cooldown" (task scheduler), the heap holds counts of the tasks still
remaining; each round you pull up to `n + 1` distinct tasks, run them, and push back what has
count left. A round with fewer than `n + 1` tasks is padded with idle time unless it is the last
round.

## 4. Recognition cues

| You see | Think |
|---------|-------|
| "k largest", "k most frequent", "k closest" | min-heap of size k, O(n log k) |
| "kth largest" once, on an array | heap of size k, or quickselect for average O(n) |
| "stream", "add one at a time, query the top" | keep the heap alive between calls |
| "median of a stream" | two heaps, low max-heap and high min-heap |
| "merge k sorted ..." | heap of one head per list, tuple with indices as tie-breakers |
| "smallest in a sorted matrix" | same as merge k sorted: one head per row |
| "minimum rooms / machines / platforms" | sort by start, heap of end times |
| "no two adjacent the same", "cooldown between repeats" | max-heap of counts; hold back the one you just used |
| "repeatedly combine the two largest" | max-heap, pop two, push the result |
| "range covering all lists" | heap of one pointer per list, track the max as you go |

## 5. Pitfalls

- **`heapq` is a min-heap.** Forgetting to negate is the most common bug in this chapter.
  Negate on push and on pop, both times.
- **Pushing a tuple whose payload is not comparable.** `(3, [1, 2])` and `(3, [1, 5])` compare
  fine, but `(3, node)` crashes on a tie. Add an integer tie-breaker.
- **Using a heap when you need sorted order.** Popping everything is O(n log n), same as sort,
  with worse constants and more code.
- **`heap[0]` is the only element you may read.** `heap[1]` is not the second smallest.
- **Rebuilding the heap for each query.** In a stream, the heap persists. Rebuilding is
  O(n) per query and defeats the purpose.
- **Off by one in two-heap rebalancing.** Always push to `low`, move `low`'s top to `high`,
  then move back if `high` is bigger. Never skip step 2 even when `x` "obviously" belongs in
  `low`.
- **Task scheduler with a heap when the formula works.** The closed form
  `max(len(tasks), (max_count - 1) * (n + 1) + number_of_maxes)` is O(n) and correct. Know both,
  but the heap version generalizes and shows the pattern.

## 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|---------|-----------|----------|----------|
| 1 | `KthLargest` | Easy | Amazon | The anchor as a class. Keep the heap at size k between calls. |
| 2 | `kth_largest` | Medium | Amazon, Google | Min-heap of size k. Then read quickselect in solutions.py. |
| 3 | `last_stone_weight` | Easy | Amazon | Max-heap. Pop two, push the difference if non-zero. |
| 4 | `k_closest_points` | Medium | Amazon, Google | Max-heap of size k on squared distance (negate). No `sqrt` needed. |
| 5 | `top_k_frequent_heap` | Medium | Amazon, Google | `Counter`, then min-heap of `(count, value)` size k. |
| 6 | `task_scheduler` | Medium | Amazon, Google | Max-heap of counts. Each round pulls up to `n + 1` tasks; pad with idle unless it is the last round. |
| 7 | `MedianFinder` | Hard | Amazon, Google | Two heaps. Push to low, move top to high, rebalance. |
| 8 | `merge_k_sorted` | Medium | Amazon, Google | Heap of `(val, list_idx, elem_idx)`. Pop one, push that list's next. |
| 9 | `reorganize_string` | Medium | Amazon, Google | Max-heap of counts. Pop the most frequent that is not the char you just placed. |
| 10 | `meeting_rooms_ii` | Medium | Amazon, Google | Sort by start. Heap of end times. Pop if `end <= start`. Peak heap size. |
| 11 | `kth_smallest_in_sorted_matrix` | Medium | Amazon, Google | Row heads in a heap: `(val, row, col)`. Pop k times. |
| 12 | `smallest_range_covering_k_lists` | Hard | Google | One pointer per list in a min-heap; track the current max. Range is `[heap min, max]`; advance the min. |

Solve 1–5 in order, then 8 and 10. 6, 7, 9 are the next tier. 11 and 12 are the stretch set;
11 is exercise 8 in disguise.
