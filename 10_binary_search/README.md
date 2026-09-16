# Binary search: discard only what you can prove

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Sorted arrays, index boundaries, and Big-O.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

**Binary search** keeps a candidate interval and discards a portion after each comparison. Sorted order makes the discarded region provably impossible. A boolean condition can also be searchable when it changes in only one direction, such as infeasible then feasible.

Choose an interval convention before coding: inclusive [left, right] or half-open [left, right). Its empty condition and update rules differ. Every iteration must shrink the interval, even when only one item remains. A midpoint that is known to be wrong should not remain a candidate.

Finding any match, the first match, the last match, and an insertion position are different contracts. Duplicates expose the difference. Rotated sorted arrays require identifying which region remains ordered. Searching a 2D matrix as a flat range needs the matrix’s row-order guarantee.

“Binary search on the answer” guesses a candidate answer and runs a feasibility check. State the bounds and why feasibility is monotone. Its cost is the number of guesses multiplied by the cost of that check; it is not automatically O(log n) overall.

## Walk through a small example

In sorted [3, 8, 12, 20, 25], search for 20. The middle value 12 is too small, so indices through that middle can be excluded. The remaining candidates contain 20 and 25. Name which endpoints are still candidates before choosing another midpoint.

## Watch for

Mixing interval conventions; retaining a rejected midpoint; returning an arbitrary duplicate when the first is required; ignoring feasibility-check cost.

## Your next small step

Open [binary search](problems/01_binary_search.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 10/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Binary Search](problems/01_binary_search.py)
- [Find First and Last Position of Element in Sorted Array](problems/02_first_last_position.py)
- [Search Insert Position](problems/03_search_insert_position.py)
- [Search in Rotated Sorted Array](problems/04_search_rotated_array.py)
- [Find Minimum in Rotated Sorted Array](problems/05_find_min_rotated.py)
- [Koko Eating Bananas](problems/06_koko_eating_bananas.py)
- [Search a 2D Matrix](problems/07_search_2d_matrix.py)
- [Median of Two Sorted Arrays](problems/08_median_two_sorted_arrays.py)

</details>
