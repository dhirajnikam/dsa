# Phase 04: Arrays & Strings

**Goal:** edit arrays in place, precompute prefix sums so range queries are O(1), and walk 2D grids without off-by-one errors.

## Key idea
"In place" means reuse the input array instead of making a new one. A read pointer scans, a write pointer marks where to store.
A prefix sum array stores running totals, so any range sum is one subtraction. Kadane's trick: the best subarray ending here is "just this number" or "extend the previous best".

## Cheat sheet
```python
w = 0                                   # read/write pointers
for r in range(len(a)):
    if keep(a[r]):
        a[w] = a[r]; w += 1             # a[:w] is the answer

from itertools import accumulate
prefix = [0] + list(accumulate(nums))   # prefix[i] = sum(nums[:i])
range_sum = prefix[r + 1] - prefix[l]   # sum of nums[l..r]

cur = best = nums[0]                    # Kadane
for x in nums[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)

t = [list(row) for row in zip(*m)]      # transpose a grid
```

## When you see... use...
- "sum over a range, many queries" -> prefix sums
- "maximum contiguous subarray" -> Kadane
- "O(1) extra space", "in place" -> read/write pointers or swaps
- "rotate / spiral a matrix" -> transpose + reverse, shrinking boundaries

## Common mistakes
- Prefix sums have `n + 1` entries. Range `[l, r]` is `prefix[r + 1] - prefix[l]`.
- Kadane with all negatives: start `best` at `nums[0]`, not `0`.
- `[[0] * cols] * rows` shares one row. Use a comprehension.
- Returning a new list when asked for "in place". The tests check the original.

## Problems
- `01_best_time_buy_sell_stock.py` — track the running minimum
- `02_max_subarray_kadane.py` — Kadane, handle all-negative
- `03_product_except_self.py` — prefix and suffix products
- `04_prefix_sum_range_queries.py` — class with O(1) range sums
- `05_rotate_matrix.py` — transpose, then reverse rows
- `06_spiral_matrix.py` — shrink four boundaries
- `07_merge_sorted_arrays_in_place.py` — merge from the back
- `08_set_matrix_zeroes.py` — first row/column as flags
- `09_longest_common_prefix.py` — vertical scan with zip
- `10_string_compression.py` — read/write pointers, run lengths
