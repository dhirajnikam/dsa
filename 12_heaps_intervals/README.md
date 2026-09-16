# Heaps and intervals: keep the important boundary

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Sorting, dictionaries, and Big-O.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **min-heap** keeps the smallest item at its root. It is only partially ordered; its whole backing list is not sorted. Insertion and removal take O(log n), root inspection O(1), and building a heap from a list can take O(n).

A bounded heap can retain the most relevant k candidates while forgetting the rest. Decide whether its root represents the best candidate or the weakest retained candidate. Stream problems update this state as new values arrive. Two heaps can separate lower and upper halves while maintaining size and ordering invariants.

An **interval** describes a start and an end. Decide whether endpoints are inclusive, and whether touching intervals overlap for this task. Sorting by a useful boundary makes neighbors comparable. Merging, selecting non-overlapping intervals, and counting concurrent meetings ask different questions.

For concurrent events, an end-time heap can track work still active. Equal endpoints need consistent handling. Include sorting and heap size in your cost: many interval methods take O(n log n), with memory dependent on active items or returned output.

## Walk through a small example

Meetings [1, 4) and [4, 6) can reuse one room because the first ends exactly when the second starts. Meetings [1, 5) and [4, 6) overlap. That one endpoint rule changes both the comparison and the test expectation.

## Watch for

Assuming heap storage is fully sorted; keeping the wrong heap direction for top-k; treating meeting endpoints like every other interval contract.

## Your next small step

Open [kth largest element](problems/01_kth_largest_element.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 12/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Kth Largest Element in an Array](problems/01_kth_largest_element.py)
- [K Closest Points to Origin](problems/02_k_closest_points.py)
- [Top K Frequent Elements](problems/03_top_k_frequent_heap.py)
- [Merge k Sorted Lists](problems/04_merge_k_sorted_lists.py)
- [Task Scheduler](problems/05_task_scheduler.py)
- [Find Median from Data Stream](problems/06_find_median_data_stream.py)
- [Merge Intervals](problems/07_merge_intervals.py)
- [Non-overlapping Intervals](problems/08_non_overlapping_intervals.py)
- [Meeting Rooms II](problems/09_meeting_rooms_ii.py)

</details>
