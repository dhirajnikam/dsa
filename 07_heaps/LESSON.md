# 07 · Heaps

> A heap answers one question fast: "what is the smallest thing I have right now?" It does not
> sort. It does not search. It gives you the minimum in O(1) and lets you insert or remove in
> O(log n). When a problem repeatedly asks for the current smallest, largest, earliest, or
> closest, that is the whole hint.

**Interview frequency:** medium, but concentrated. Amazon asks Top-K and "merge k sorted"
constantly. Google likes the two-heap median and scheduling problems where a heap holds
"what is available right now."

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

A heap is a container that always knows which item is smallest (or largest) without keeping
everything sorted, so you can add items and pull out the top one very quickly.

### Start with something you already do

Picture a hospital emergency room. Patients arrive all day. The sickest patient is seen next,
no matter when they walked in. When a new patient arrives, the nurse does not re-sort the whole
waiting room. They rank the newcomer against a few people and slot them in. When the doctor is
free, the nurse asks one question: "who is the sickest right now?" One glance at the top of
the list answers it.

That is the key insight of the whole chapter: **you do not need everyone sorted. You only need
the top one to be correct.** Sorting the whole waiting room after every arrival is wasted
effort, because the doctor only ever asks for one person.

A second picture shows how the heap keeps the top correct cheaply. A tournament bracket. The
champion sits at the top, the two finalists below, the four semi-finalists below those. To
know the champion you look at one spot. Now a new player joins. You do not replay the
tournament. The newcomer starts at the bottom and plays upward along one path, beating whoever
they are better than, until they lose. Everyone on the other paths is untouched. For a million
players that path is about twenty matches.

### Now the same thing with numbers

A **min-heap** is a bracket where the smallest number wins each match, so the smallest sits on
top. The only rule: every parent is smaller than its two children. Nothing else is promised.

Start with `[2, 5, 4]` and add `1`. It goes at the bottom, then climbs one path.

```
      2              2              2              1
     / \    add 1   / \    swap    / \    swap    / \
    5   4   --->   5   4   --->   1   4   --->   2   4
                  /              /              /
                 1              5              5
```

The 1 beat 5, then beat 2, and stopped at the top. The 4 was never asked to play. The lesson
stores the heap as a plain list where the children of position `i` sit at positions `2i + 1`
and `2i + 2`, so the same thing as a table:

| Step | List | What happened |
|------|------|---------------|
| start | `[2, 5, 4]` | 2 on top, 5 and 4 below it |
| add 1 | `[2, 5, 4, 1]` | 1 goes to the end, under 5 |
| swap | `[2, 1, 4, 5]` | 1 is smaller than its parent 5, so they swap |
| swap | `[1, 2, 4, 5]` | 1 is smaller than its parent 2, so they swap. Top. |

Now the doctor calls the next patient: remove the top. Move the last item to the top, then let
it sink down past whichever child is smaller.

Pause and predict: after removing 1 from `[1, 2, 4, 5]`, what does the list look like?

<details><summary>Answer</summary>
Move 5 to the top: `[5, 2, 4]`. 5 is bigger than its smaller child 2, so swap: `[2, 5, 4]`.
5 has no children now, so stop. The new top is 2, the correct next-smallest.
</details>

### The words people use

- **Heap.** The bracket. A list arranged so every parent beats its children. Python's is `heapq`.
- **Min-heap.** Smallest on top. What `heapq` gives you.
- **Max-heap.** Largest on top. Python does not ship one, so you fake it by flipping signs.
- **Priority queue.** The general name for "always give me the most important item next." A
  heap is the usual way to build one.
- **Root / top.** Position 0 in the list. The only item you may read directly.
- **Push, `heappush`.** Add an item at the bottom and let it climb. Also called bubble up.
- **Pop, `heappop`.** Remove the top, move the last item up, let it sink. Also called sift down.
- **`heapify`.** Turn an existing list into a heap all at once. Faster than pushing one by one.
- **Heap property / invariant.** "Every parent is smaller than its children." The second
  smallest can be at position 1 or 2; the heap does not care.
- **Negate.** Push `-x` instead of `x` so a min-heap acts like a max-heap. Like flipping the
  sign on a scoreboard so the biggest score reads as the smallest. Flip it back when you pop.
- **Tuple priority, tie-breaker.** Pushing `(count, item)` orders by count first, since Python
  compares tuples left to right. A plain counter in the middle stops the heap ever comparing two
  things it cannot compare, like tree nodes.
- **k largest / kth largest / Top-K.** The top k items, or the single item at rank k. The
  heap's home turf.
- **Two heaps.** A max-heap for the small half and a min-heap for the large half, so the middle
  value is always on top of one of them. The running median trick.
- **Quickselect.** Another way to find the kth largest, average O(n), by partitioning like
  quicksort. Mentioned in the lesson, not required here.

### Why the fast way is fast

You want the 10 largest numbers out of a list.

| Items | Sort everything | Heap that holds only 10 |
|-------|-----------------|-------------------------|
| 10 | about 33 steps | about 33 steps |
| 1,000 | about 10,000 | about 3,300 |
| 100,000 | about 1,700,000 | about 330,000 |

Sorting pays for ordering all 100,000; the heap only ever orders 10. The **VIP room** picture
makes it obvious: the room holds k people. When someone new arrives, let them in, and if the
room is now over capacity, kick out the smallest person. Whoever is left at the end is the k
largest, and the smallest person in the room is the kth largest. The room is a *min*-heap even
though you want the *largest*, because the person you must find quickly is the smallest
survivor, the one to evict.

The trade-off: a heap gives you the top and nothing else. If you need the full sorted order,
popping everything costs the same as sorting, with more code. Use a heap for repeated "what is
the top right now," not "show me everything in order."

### Try it in your head

1. You need the 3 largest from `[7, 2, 9, 4, 8]` using a VIP room of size 3. Walk through it.

<details><summary>Answer</summary>
Add 7: {7}. Add 2: {2, 7}. Add 9: {2, 7, 9}. Add 4: {2, 4, 7, 9}, over capacity, kick out 2:
{4, 7, 9}. Add 8: {4, 7, 8, 9}, kick out 4: {7, 8, 9}. The room holds the 3 largest; the
smallest in it, 7, is the 3rd largest.
</details>

2. You want the largest stone each time, but `heapq` only gives the smallest. Stones are
   `[3, 8, 5]`. What do you push, and what comes out first?

<details><summary>Answer</summary>
Push `-3`, `-8`, `-5`. The top is `-8`, the smallest number. Pop it and flip the sign: 8, the
largest stone. Forget the second flip and you will hand back a negative stone.
</details>

3. Three sorted lists: `[1, 4]`, `[2, 3]`, `[0, 5]`. You want them merged. What sits in the
   heap at the start, and what pops first?

<details><summary>Answer</summary>
The first item of each list: 1, 2, 0. Pop 0, the smallest. Then push the next item from the
list 0 came from, which is 5. The heap never holds more than three items no matter how long
the lists are.
</details>

### Common confusions, cleared

- **"Isn't a heap just a sorted list?"** No. Only the top is guaranteed. `heap[1]` is not the
  second smallest; it is just one of the top item's two children. If you need everything in
  order, sort.
- **"Why a min-heap for the k largest? That sounds backwards."** Because the operation you do
  constantly is *evict the weakest survivor*, and a min-heap makes the weakest survivor the one
  item you can reach instantly. The heap guards the door; it does not display the winner.
- **"Doesn't adding an item mean re-sorting everything?"** That is the whole reason heaps
  exist. A new item climbs one path of the bracket, about log n swaps, and nothing else moves.
- **"Can I put anything in a heap?"** Only things Python can compare. Two tuples with equal
  first values compare their second values, and if those are tree nodes, it crashes. Put a
  counter in the middle as a tie-breaker.

### What to do next

Scroll down to Part 2 and read §2, the fully worked `kth_largest`, and check its trace against your
VIP-room answer above. Then read the first two templates in Part 2 §3, "Min-heap of size k" and
"Negate for a max-heap." Then open `exercises.py` and do `KthLargest` and `last_stone_weight`
with a 30-minute timer; the first is the VIP room as a class, the second is the scoreboard
flip. When they pass, `merge_k_sorted` is the one that makes tuple priorities click.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

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

### 1. The core idea

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

### 2. Anchor problem: Kth Largest Element in an Array, fully worked

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

### 3. Patterns and templates in this chapter

#### Min-heap of size k for "k largest"

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

#### Negate for a max-heap

`heapq` is min-only. Push `-x`, pop and negate back. For tuples, negate the first field.

```python
heap = [-x for x in nums]
heapq.heapify(heap)                    # O(n), not O(n log n)
largest = -heapq.heappop(heap)
```

`heapify` on a whole list is O(n). Pushing one at a time is O(n log n). If you already have
all the elements, heapify.

#### Tuple priorities with tie-breakers

Python compares tuples left to right. `(count, char)` sorts by count, then by char. When the
payload is not comparable (a list, a node), put a unique integer in the middle as a tie-breaker
so the comparison never reaches it:

```python
heapq.heappush(heap, (value, list_index, element_index))    # never compares the list itself
```

This is exactly what merging k sorted lists needs: the value to order by, and enough indices to
know where to fetch the next element.

#### Two heaps for a running median

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

#### Heap as "what is available right now"

Scheduling problems: sort events by start, walk them in order, keep a heap of things that are
busy keyed by when they free up. Before handling an event, pop everything that has finished.
Meeting Rooms II is "heap of end times": a room is free if its end ≤ the next start. The heap
size at its peak is the answer.

For "greedy with cooldown" (task scheduler), the heap holds counts of the tasks still
remaining; each round you pull up to `n + 1` distinct tasks, run them, and push back what has
count left. A round with fewer than `n + 1` tasks is padded with idle time unless it is the last
round.

### 4. Recognition cues

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

### 5. Pitfalls

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

### 6. Exercises

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
