# Arrays and strings: keep just enough state

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Chapter 00 lists and chapter 03 operation counting.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

An **array/list** stores an ordered sequence addressable by index. Python lists offer constant-time indexing but inserting in the middle shifts elements. **Contiguous** means neighboring positions; a subsequence may skip positions.

Instead of rereading earlier items, maintain a small summary. A running minimum summarizes the cheapest value so far. A **prefix sum** stores totals before each position. Removing the earlier total from a later total isolates a range. Use an initial zero so ranges starting at index zero follow the same rule.

For a best contiguous segment, consider whether an earlier partial segment helps or harms a new segment. All-negative input is a real case: an empty result is allowed only if the question says so. Prefix and suffix summaries can also capture contributions before and after an item without using that item itself.

**In place** means changing the input rather than returning a replacement. A read index visits candidates; a write index marks where a kept item belongs. A matrix is a list of rows: distinguish row count from column count. Spiral traversal tracks boundaries, and every boundary can become empty. Rotation and zeroing have explicit mutation requirements.

## Walk through a small example

Daily distances [4, 7, 2] give totals-before-position [0, 4, 11, 13]. The distance for days at indices 1 through 2 is 13 − 4 = 9. Trace why the right boundary uses the total after the last included item. Precomputation takes O(n) time and space; each range query then takes O(1).

## Watch for

Off-by-one range endpoints; initializing an all-negative maximum to zero; modifying a matrix marker before recording what it meant; returning a copy for an in-place task.

## Your next small step

Open [best time buy sell stock](problems/01_best_time_buy_sell_stock.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 04/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Best Time to Buy and Sell Stock](problems/01_best_time_buy_sell_stock.py)
- [Maximum Subarray](problems/02_max_subarray_kadane.py)
- [Product of Array Except Self](problems/03_product_except_self.py)
- [Range Sum Query - Immutable](problems/04_prefix_sum_range_queries.py)
- [Rotate Image](problems/05_rotate_matrix.py)
- [Spiral Matrix](problems/06_spiral_matrix.py)
- [Merge Sorted Array](problems/07_merge_sorted_arrays_in_place.py)
- [Set Matrix Zeroes](problems/08_set_matrix_zeroes.py)
- [Longest Common Prefix](problems/09_longest_common_prefix.py)
- [String Compression](problems/10_string_compression.py)

</details>
