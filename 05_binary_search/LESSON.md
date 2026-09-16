# 05 · Binary Search

> Binary search is not "find a number in a sorted list." It is "find the boundary where a
> yes/no question flips." Once you see it that way, half the problems in this chapter stop
> being about sorted arrays at all, and you stop writing off-by-one bugs.

**Interview frequency:** high. Google loves the "search on the answer" variant because it
looks nothing like binary search until you notice the monotonicity. Amazon asks the rotated
array and 2D matrix versions as phone screens.

## 1. The core idea

If you can ask one question and eliminate half of what remains, you need only log₂(n)
questions. For a million items that is 20 questions instead of a million.

The thing you eliminate half of does not have to be an array. It can be a range of possible
*answers*: "could Koko finish at speed 7?" If yes, every speed above 7 also works, so the
answer is at most 7 and you can throw away the top half.

```
linear scan                          binary search
for i in range(n):                   lo, hi = 0, n - 1
    if nums[i] == target:            while lo <= hi:
        return i                         mid = (lo + hi) // 2
                                         if nums[mid] == target: return mid
                                         if nums[mid] < target: lo = mid + 1
                                         else:                  hi = mid - 1
O(n) time                            O(log n) time
```

The recognition cue: **sorted input, or a yes/no question whose answer is monotonic in
some parameter.** "Monotonic" means: once it flips from no to yes, it never flips back.

## 2. Anchor problem: Binary Search, fully worked

**Problem.** Given a sorted array of distinct integers `nums` and a `target`, return the
index of `target`, or `-1` if it is absent. O(log n).

**Understand.** Sorted ascending? Yes. Distinct, so at most one valid index. Empty array
allowed? Yes, return -1. Can target be smaller than everything or larger than everything?
Yes, both must return -1.

**Examples.** `[-1, 0, 3, 5, 9, 12], 9 → 4`. `[-1, 0, 3, 5, 9, 12], 2 → -1`. `[5], 5 → 0`.
`[], 1 → -1`.

**Brute force.** Scan every element. O(n). Say it and move on; the problem asks for O(log n).

**Insight.** Look at the middle. If it equals the target, done. If it is smaller, the target
can only live to the right, so throw away the left half including the middle. Otherwise throw
away the right half. Each step halves the live range.

**Code.**

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1          # closed interval [lo, hi] of live indices
    while lo <= hi:                    # live range is non-empty
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1               # mid is ruled out; skip past it
        else:
            hi = mid - 1
    return -1
```

**Test.** `[-1, 0, 3, 5, 9, 12], 9`: lo=0 hi=5 mid=2 nums[2]=3 < 9 → lo=3. lo=3 hi=5 mid=4
nums[4]=9 → return 4. ✓
`[-1, 0, 3, 5, 9, 12], 2`: mid=2 nums[2]=3 > 2 → hi=1. mid=0 nums[0]=-1 < 2 → lo=1. mid=1
nums[1]=0 < 2 → lo=2. Now lo=2 > hi=1, loop ends → -1. ✓

**Complexity.** O(log n) time, O(1) space.

**What to say out loud.** "The array is sorted, so comparing the target with the middle
element tells me which half it must be in. I keep a closed interval of live indices, move
`lo` or `hi` past the middle each step, and stop when the interval is empty. Log n steps,
constant space."

## 3. Patterns and templates in this chapter

### The one template: first index where the predicate is True

Every binary search in this chapter is this one search in disguise. Imagine a boolean array
that is all `False` then all `True`, like `FFFFTTT`. Find the first `T`.

```python
def first_true(lo, hi, pred):
    """Smallest i in [lo, hi) with pred(i) True. Returns hi if none is."""
    while lo < hi:                     # half-open [lo, hi); live range has hi - lo elements
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid                   # mid might be the answer; keep it in range
        else:
            lo = mid + 1               # mid is False; the answer is strictly right of it
    return lo                          # lo == hi: the boundary
```

Why this never goes off by one:
- The range is half-open, so `hi` is one past the last candidate. `hi = mid` keeps `mid` as
  a candidate because `mid` might be the first `True`.
- `lo = mid + 1` is safe because `mid` was `False` and can never be the answer.
- `mid = (lo + hi) // 2` is strictly less than `hi` when `lo < hi`, so `hi = mid` always
  shrinks the range. The loop terminates.
- When `lo == hi`, every index below `lo` was proven `False` and every index at or above
  `hi` is `True` (or `hi` is the sentinel "none"). That is exactly the boundary.

Examples of the predicate, with the answer it gives:

| Question | `pred(i)` | Result |
|----------|-----------|--------|
| search insert position | `nums[i] >= target` | first index ≥ target |
| first occurrence of target | `nums[i] >= target` | then check `nums[i] == target` |
| last occurrence of target | `nums[i] > target` | answer minus 1 |
| minimum in a rotated array | `nums[i] <= nums[-1]` | first element of the "second" sorted run |
| a peak | `nums[i] > nums[i + 1]` | first index where we start descending |

Memorize this template and derive everything else. When a problem says "sorted" or
"monotonic," your first job is to write down the predicate, not the loop.

### Closed vs. half-open: pick one and know it

The anchor used a closed interval `[lo, hi]` with `while lo <= hi`. The template uses a
half-open `[lo, hi)` with `while lo < hi`. Both are correct. Mixing them is the entire source
of off-by-one bugs. The safe rule:

```
closed [lo, hi]:    while lo <= hi;  lo = mid + 1;  hi = mid - 1;  answer found inside loop
half-open [lo, hi): while lo <  hi;  lo = mid + 1;  hi = mid;      answer is lo after loop
```

Use closed when you return as soon as you find an exact match. Use half-open when you are
looking for a boundary.

### Binary search on the answer

When the question is "what is the minimum k such that something is possible," and being
possible at `k` implies being possible at every larger `k`, then `feasible(k)` is a
`FFFFTTT` predicate over the range of possible answers. Search it.

```python
def min_feasible(lo, hi, feasible):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

The work is in three places: pick the range `[lo, hi]` (smallest and largest possible
answers), write `feasible` (usually a greedy O(n) simulation), and prove monotonicity out
loud in one sentence. Koko's speed, ship capacity, and the largest-subarray-sum split are all
this.

Complexity is O(n log(range)) where `range` is `hi - lo`. Say that, not "O(n log n)."

### Rotated arrays: find which half is sorted

In `[4, 5, 6, 7, 0, 1, 2]` at least one half around `mid` is properly sorted. Check whether
the target falls inside the sorted half; if so, go there; otherwise, go to the other half.

```python
if nums[lo] <= nums[mid]:              # left half is sorted
    if nums[lo] <= target < nums[mid]: hi = mid - 1
    else:                              lo = mid + 1
else:                                  # right half is sorted
    if nums[mid] < target <= nums[hi]: lo = mid + 1
    else:                              hi = mid - 1
```

### Two sorted arrays: partition, do not merge

For the median of two sorted arrays in O(log(min(m, n))), binary search over how many
elements you take from the shorter array to be in the left half. The partition is correct
when every element on the left is ≤ every element on the right. Four numbers to compare.

## 4. Recognition cues

| You see | Think |
|---------|-------|
| "sorted array" | binary search, unless the question is about pairs (then two pointers) |
| "O(log n)" in the requirement | binary search or a heap; on an array it is binary search |
| "first / last position", "insert position" | first index where `nums[i] >= target` (or `>`) |
| "minimum k such that ...", "least capacity", "min speed" | binary search on the answer with a greedy `feasible(k)` |
| "rotated sorted array" | one half around mid is always sorted |
| "peak", "local maximum" | first index where `nums[i] > nums[i+1]` |
| "sorted matrix, rows continue" | treat as one flat array of length m·n |
| "timestamps", "versions", "as of time t" | `bisect_right` on the per-key sorted list |
| "two sorted arrays, log time" | partition the shorter array |

## 5. Pitfalls

- **`while lo < hi` with `hi = mid - 1`**, or `while lo <= hi` with `hi = mid`. You either skip
  the answer or loop forever. Pick closed or half-open and stay there.
- **Infinite loop with `lo = mid`.** If `mid = (lo + hi) // 2` rounds down, `lo = mid` may not
  move when `hi = lo + 1`. Either use `lo = mid + 1` (after proving `mid` is not the answer) or
  round up with `mid = (lo + hi + 1) // 2`.
- **Forgetting the empty array.** `hi = len(nums) - 1 = -1`, the closed loop never runs, you
  return -1. Good. But `nums[0]` before the loop will crash.
- **Non-monotonic predicate.** Binary search on the answer only works if `feasible(k)` is
  `FFFFTTT`. Say why before you code: "more capacity never makes shipping harder."
- **Wrong range for the answer.** For Koko, `lo = 1` not `0` (speed 0 never finishes), and
  `hi = max(piles)` because a faster speed cannot help. Tight ranges shrink the log factor and
  avoid division by zero.
- **Rotated array with duplicates.** The "which half is sorted" test breaks when
  `nums[lo] == nums[mid] == nums[hi]`. The problems here assume distinct values; say so.
- **Integer overflow on `(lo + hi) // 2`.** Not a Python issue, but mention `lo + (hi - lo) // 2`
  if the interviewer writes Java or C++.

## 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|---------|-----------|----------|----------|
| 1 | `binary_search` | Easy | Everyone | The anchor above. Closed interval, `lo <= hi`. |
| 2 | `search_insert_position` | Easy | Amazon, Google | First index where `nums[i] >= target`. Half-open template. |
| 3 | `first_and_last_position` | Medium | Amazon, Google | Two searches: first `>= target`, first `> target` minus one. |
| 4 | `search_2d_matrix` | Medium | Amazon, Google | Index `i` in `[0, m·n)` maps to `matrix[i // n][i % n]`. |
| 5 | `min_eating_speed` | Medium | Google, Amazon | Search speed in `[1, max(piles)]`. Hours at speed k: sum of `ceil(p / k)`. |
| 6 | `find_min_rotated` | Medium | Amazon, Google | First index where `nums[i] <= nums[-1]`. |
| 7 | `search_rotated` | Medium | Amazon, Google | One half is sorted. Check if target is inside it. |
| 8 | `TimeMap` | Medium | Google, Amazon | Per key, a list of `(timestamp, value)`. `bisect_right` on timestamps. |
| 9 | `ship_within_days` | Medium | Amazon | Capacity in `[max(w), sum(w)]`. Greedy: start a new day when the load would overflow. |
| 10 | `split_array_largest_sum` | Hard | Google | Same as 9. Feasible if the greedy needs at most k pieces. |
| 11 | `median_two_sorted` | Hard | Google, Amazon | Binary search the cut in the shorter array. Compare four boundary values. |
| 12 | `peak_element` | Medium | Google, Amazon | First index where `nums[i] > nums[i + 1]`. The last index is a peak if nothing else is. |

Solve 1–7 in order, then 12. 8–11 are the stretch set; 9 and 10 are the same template, so do
them back to back.
