# Phase 10: Binary Search

**Goal:** write a binary search that stops and returns the right index on the first try.

## Key idea
Binary search halves a sorted range each step, so it takes O(log n) steps. It works whenever
"is the answer at or after `mid`?" flips from no to yes exactly once. Sometimes the sorted
thing is the array. Sometimes it is the *answer* (a speed, a size). Same loop either way.

## Cheat sheet
```python
lo, hi = 0, len(nums) - 1        # A: exact match in a sorted array
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target: return mid
    if nums[mid] < target: lo = mid + 1
    else: hi = mid - 1
return -1

lo, hi = 0, len(nums)            # B: first index where ok(mid) is true (len(nums) if never)
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid          # mid might be the answer, keep it
    else: lo = mid + 1            # mid is not, skip it
return lo   # ok = nums[mid] >= target  or  ok = feasible(mid) for "smallest X that works"
```

## When you see... use...
- "find target in a sorted array" -> template A
- "first/last position", "insert position" -> template B with `>=` or `>`
- "minimum speed / smallest k / min days so that..." -> template B over the answer range
- "rotated sorted array" -> one half is always sorted; check which and go there
- "sorted matrix, rows continue each other" -> one array: `matrix[i // cols][i % cols]`

## Common mistakes
- `while lo < hi` with `lo = mid` loops forever. Always `lo = mid + 1`.
- Mixing templates: `lo <= hi` goes with `hi = mid - 1`, `lo < hi` with `hi = mid`.
- Template B can return `len(nums)`. Check bounds before indexing.
- Search-on-answer: `hi` must be a value that definitely works (e.g. `max(piles)`).

## Problems
- `01_binary_search.py` — template A, exact match
- `02_first_last_position.py` — two template B searches
- `03_search_insert_position.py` — template B returns the spot
- `04_search_rotated_array.py` — pick the sorted half
- `05_find_min_rotated.py` — compare `nums[mid]` with `nums[hi]`
- `06_koko_eating_bananas.py` — binary search on the answer
- `07_search_2d_matrix.py` — flatten the index
- `08_median_two_sorted_arrays.py` — partition search, hard, do last
