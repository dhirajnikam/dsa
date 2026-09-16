# 07 · Heaps, explained from zero

Read this first if "heap" sounds like a pile of laundry and "priority queue" sounds like
airport boarding. When it clicks, open `LESSON.md`, the dense reference. This file is the
friendly conversation before it.

## In one sentence

A heap is a container that always knows which item is smallest (or largest) without keeping
everything sorted, so you can add items and pull out the top one very quickly.

## Start with something you already do

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

## Now the same thing with numbers

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

## The words people use

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

## Why the fast way is fast

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

## Try it in your head

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

## Common confusions, cleared

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

## What to do next

Open `LESSON.md` and read §2, the fully worked `kth_largest`, and check its trace against your
VIP-room answer above. Then read the first two templates in §3, "Min-heap of size k" and
"Negate for a max-heap." Then open `exercises.py` and do `KthLargest` and `last_stone_weight`
with a 30-minute timer; the first is the VIP room as a class, the second is the scoreboard
flip. When they pass, `merge_k_sorted` is the one that makes tuple priorities click.
