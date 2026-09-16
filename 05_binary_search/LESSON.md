# 05 · Binary Search

**In one sentence.** Ask one yes/no question, throw away half of what is left, repeat. It works
on anything where the answers line up as a run of no's followed by a run of yes's.

**Why you care.** `git bisect` finds the one bad commit out of a thousand by testing ten. Every
database index is a tree of binary searches. Interview frequency is high. Google loves the
"search on the answer" variant. Amazon asks the rotated array version as a phone screen.

## The idea, with a story

A friend picks a secret number between 1 and 100. You guess. They say "higher" or "lower."

Nobody guesses 1, then 2, then 3. You guess 50. "Higher." The secret is now in 51 to 100, and
you never think about 1 to 50 again. You guess 75. "Lower." Now it is 51 to 74. Every guess
halves the range. 100 numbers fall in seven guesses. A million would take twenty.

Now the twist that makes the chapter click. Forget numbers. A shop is closed early in the day
and open later, and once it opens it stays open. You want the first hour it is open. "Open at
noon?" No. Then every hour before noon is also a no. Throw them all away. "Open at 6 pm?" Yes.
Then every later hour is also a yes. You do not need them. Keep halving between noon and 6 pm.

The pattern is "no, no, no, yes, yes, yes" and you want the spot where no flips to yes. That is
the whole chapter. Sorted arrays are just one place the shape shows up.

## The same story with numbers

Sorted list `[1, 3, 5, 7, 9, 11]`, target `7`. Two markers. `lo` is the leftmost position that
could still hold the answer, `hi` the rightmost. Positions start at 0.

| Step | lo | hi | mid = (lo + hi) // 2 | value at mid | verdict | move |
|------|----|----|----------------------|--------------|---------|------|
| 1 | 0 | 5 | 2 | 5 | too small | lo = 3 |
| 2 | 3 | 5 | 4 | 9 | too big | hi = 3 |
| 3 | 3 | 3 | 3 | 7 | found | return 3 |

Three looks for six numbers. When the middle was too small, `lo` jumped to `mid + 1`, not
`mid`. The middle was already ruled out, so there is no reason to keep it.

Pause and predict: same list, target `4`, which is not there. What are `lo` and `hi` when the
loop stops?

<details><summary>Answer</summary>
Step 1: mid 2, value 5, too big, hi = 1. Step 2: mid 0, value 1, too small, lo = 1. Step 3:
mid 1, value 3, too small, lo = 2. Now lo = 2 is past hi = 1. The range is empty, so return -1.
Notice lo ended exactly where 4 would be inserted to keep the list sorted. That is exercise 2.
</details>

## The anchor problem: Binary Search

Given a sorted array of distinct integers and a `target`, return its index, or `-1` if absent.

**Brute force.** Scan every element. O(n). The problem asks for O(log n), so move on.

**Insight.** Look at the middle. Equal means done. Smaller means the target can only live to the
right, so throw away the left half including the middle. Otherwise throw away the right half.

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

**Complexity.** O(log n) time, O(1) space.

**What to say.** "The array is sorted, so comparing the target with the middle tells me which
half it is in. I keep a closed interval of live indices, move one end past the middle each step,
and stop when the interval is empty."

## Templates you memorize

**First index where the predicate is True.** Picture a row that is all False then all True, like
`FFFFTTT`. Find the first `T`. Every search in this chapter is this one in disguise.
```python
def first_true(lo, hi, pred):
    """Smallest i in [lo, hi) with pred(i) True. Returns hi if none is."""
    while lo < hi:                     # half-open [lo, hi)
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid                   # mid might be the answer; keep it
        else:
            lo = mid + 1               # mid is False; answer is to the right
    return lo
```

Change the predicate, get a new problem:

| Question | `pred(i)` |
|----------|-----------|
| insert position | `nums[i] >= target` |
| last occurrence | `nums[i] > target`, then answer minus 1 |
| minimum in a rotated array | `nums[i] <= nums[-1]` |
| a peak | `nums[i] > nums[i + 1]` |

**Binary search on the answer.** The thing you halve is a range of candidate answers, not an
array. "Can Koko finish at speed 7?" If yes, every faster speed also works. So `feasible(k)` is
`FFFFTTT` over speeds, and you want the first yes.
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
The work is in three places: pick the range of possible answers, write `feasible` as a greedy
O(n) pass, and say out loud why it is monotonic. Cost is O(n log(range)).

**Closed versus half-open. Pick one and stay in it.**
```
closed [lo, hi]:    while lo <= hi;  lo = mid + 1;  hi = mid - 1;  answer found inside loop
half-open [lo, hi): while lo <  hi;  lo = mid + 1;  hi = mid;      answer is lo after loop
```

## When you see X, think Y

| You see | Think |
|---------|-------|
| "sorted array" | binary search, unless it is about pairs, then two pointers |
| "O(log n)" required, on an array | binary search |
| "first / last position", "insert position" | first index where `nums[i] >= target` |
| "minimum k such that ...", "least capacity" | search on the answer with a greedy `feasible(k)` |
| "rotated sorted array" | one half around mid is always sorted |
| "peak" | first index where `nums[i] > nums[i + 1]` |
| "sorted matrix, rows continue" | treat as one flat array of length m·n |
| "as of time t", "versions" | `bisect_right` on a sorted list of timestamps |

## Words you will hear

- **lo, hi.** The two markers. Everything outside them has been proven not to matter.
- **mid.** The middle position, rounded down. The one item you look at.
- **Predicate.** A yes/no question about a position, written `pred(i)`.
- **Monotonic.** Answers go "no, no, yes, yes" and never flip back. The one property you need.
- **Boundary.** The spot where no becomes yes. Most problems here are secretly "find the boundary."
- **Feasible.** The test for one candidate answer. `feasible(k)` means "does k work?"
- **bisect.** Python's built-in binary search module.

## Mistakes everyone makes once

- **Mixing the two styles.** `while lo < hi` with `hi = mid - 1` skips the answer. `while lo <= hi`
  with `hi = mid` loops forever. Pick closed or half-open.
- **`lo = mid` loops forever.** When `lo` and `hi` are one apart, `mid` rounds down to `lo` and
  nothing moves. Use `lo = mid + 1` after proving `mid` is a no.
- **Wrong answer range.** For Koko, `lo = 1`, not 0, because speed 0 never finishes. `hi` is
  `max(piles)` because faster cannot help.
- **A predicate that is not monotonic.** Unsorted data has no fence. Binary search will
  confidently return nonsense. Say why it is monotonic before you code.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `binary_search` | Easy | The anchor. Closed interval, `lo <= hi`. |
| 2 | `search_insert_position` | Easy | First index where `nums[i] >= target`. |
| 3 | `first_and_last_position` | Medium | Two searches: first `>= target`, first `> target` minus one. |
| 4 | `search_2d_matrix` | Medium | Index `i` in `[0, m·n)` maps to `matrix[i // n][i % n]`. |
| 5 | `min_eating_speed` | Medium | Speed in `[1, max(piles)]`. Hours at speed k: sum of `ceil(p / k)`. |
| 6 | `find_min_rotated` | Medium | First index where `nums[i] <= nums[-1]`. |
| 7 | `search_rotated` | Medium | One half is sorted. Check if target is inside it. |
| 8 | `TimeMap` | Medium | Per key, a list of `(timestamp, value)`. `bisect_right` on timestamps. |
| 9 | `ship_within_days` | Medium | Capacity in `[max(w), sum(w)]`. Greedy: new day when the load would overflow. |
| 10 | `split_array_largest_sum` | Hard | Same as 9. Feasible if the greedy needs at most k pieces. |
| 11 | `median_two_sorted` | Hard | Binary search the cut in the shorter array. Compare four boundary values. |
| 12 | `peak_element` | Medium | First index where `nums[i] > nums[i + 1]`. The last index is a peak otherwise. |

Do 1 and 2 today with a 30-minute timer. Then 5, where "search on the answer" becomes something
you have done. 3 to 7 and 12 over the week. 8 to 11 are for when those pass cold.
