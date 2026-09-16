# 05 · Binary Search

> Binary search is not "find a number in a sorted list." It is "find the boundary where a
> yes/no question flips." Once you see it that way, half the problems in this chapter stop
> being about sorted arrays at all, and you stop writing off-by-one bugs.

**Interview frequency:** high. Google loves the "search on the answer" variant because it
looks nothing like binary search until you notice the monotonicity. Amazon asks the rotated
array and 2D matrix versions as phone screens.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

Binary search is "ask one yes/no question, throw away half of what is left, repeat," and it
works on anything where the answers line up as a run of no's followed by a run of yes's.

### Start with something you already do

A friend picks a secret number between 1 and 100. You guess; they say "higher" or "lower."

Nobody guesses 1, then 2, then 3. You guess 50. "Higher." The secret is now in 51 to 100, and
you never think about 1 to 50 again. You guess 75. "Lower." Now it is 51 to 74. Every guess
halves the range, so 100 numbers fall in seven guesses and a million would take twenty.

Now the twist that makes the chapter click. Forget numbers. A shop is closed early in the day
and open later, and once it opens it stays open. You want the first hour it is open. "Open at
noon?" No. Then every hour before noon is also a no; throw them all away. "Open at 6 pm?" Yes.
Then every later hour is also a yes; you do not need them. Keep halving between noon and 6 pm
and you find the opening hour in three questions.

The pattern is "no, no, no, yes, yes, yes" in a row, and you want the spot where no flips to
yes. That is the whole chapter. "Which is the smallest truck that fits the load?" Same shape:
small trucks fail, and once one fits, every bigger one fits too. Sorted arrays are just one
place the shape shows up.

### Now the same thing with numbers

Sorted list `[1, 3, 5, 7, 9, 11]`, target `7`. Two markers: `lo` is the leftmost position that
could still hold the answer, `hi` the rightmost. Positions start at 0.

| Step | lo | hi | mid = (lo + hi) // 2 | value at mid | verdict | move |
|------|----|----|----------------------|--------------|---------|------|
| 1 | 0 | 5 | 2 | 5 | too small | lo = 3 |
| 2 | 3 | 5 | 4 | 9 | too big | hi = 3 |
| 3 | 3 | 3 | 3 | 7 | found | return 3 |

Three looks for six numbers. When the middle was too small, `lo` jumped to `mid + 1`, not
`mid`. The middle was already ruled out, so there is no reason to keep it.

Pause and predict: same list, target `4`, which is not there. What are `lo` and `hi` when the
loop stops, and why does it stop?

<details><summary>Answer</summary>
Step 1: mid 2, value 5, too big, hi = 1. Step 2: mid 0, value 1, too small, lo = 1. Step 3:
mid 1, value 3, too small, lo = 2. Now lo = 2 is past hi = 1, the range is empty, the loop
stops, return -1. Notice lo ended exactly where 4 would be inserted to keep the list sorted.
That is not a coincidence; it is exercise 2.
</details>

### The words people use

- **lo, hi.** The two markers. Everything outside them has been proven not to matter.
- **mid.** The middle position between the markers, rounded down. The one item you look at.
- **Predicate.** A yes/no question you ask about a position, such as "is this value at least
  the target?" Written `pred(i)` in the lesson.
- **Monotonic.** The predicate's answers go "no, no, yes, yes" and never flip back. This is the
  one property binary search truly needs. Sorted is a special case of it.
- **Boundary.** The spot where no becomes yes. Most problems here are secretly "find the boundary."
- **Closed interval `[lo, hi]`.** Both markers are live candidates. Loop while `lo <= hi`.
- **Half-open interval `[lo, hi)`.** `hi` is one past the last candidate. Loop while `lo < hi`.
  The lesson's `first_true` template uses this.
- **Off-by-one.** Picture a fence between positions. Is `mid` on your side of the fence or the
  other? Being wrong about that skips the answer or loops forever.

  ```
  positions:   0   1   2   3   4   5
  answers:     N   N   N | Y   Y   Y
                         ^ the fence sits between 2 and 3; the answer is 3
  ```

  If `mid` says yes, it might be the first yes, so keep it: `hi = mid`. If `mid` says no, it
  can never be the answer, so step past it: `lo = mid + 1`.
- **Binary search on the answer.** The thing you halve is a range of possible answers, like
  truck capacities from 10 to 500, not an array.
- **Feasible.** The test for one candidate answer. `feasible(k)` means "does k work?"
- **Rotated array.** A sorted list cut and the pieces swapped, like `[4, 5, 6, 1, 2, 3]`.
  One half around the middle is always still sorted.
- **Peak.** An item bigger than both neighbours. "Am I already going downhill?" is monotonic.
- **bisect.** Python's built-in binary search module. `bisect_right` finds the first position
  greater than the target.

### Why the fast way is fast

| Items | Look at each one | Halve each time |
|-------|------------------|-----------------|
| 10 | 10 | 4 |
| 1,000 | 1,000 | 10 |
| 100,000 | 100,000 | 17 |

Doubling the input adds one more look. That is O(log n). For "search on the answer," each test
costs a pass over the data, so the total is about n times log of the answer range. For 100,000
items and a range up to a billion, that is around 3,000,000 steps. Trying every possible answer
would be 100,000 times a billion, which never finishes.

The trade-off: you must have the "no, no, yes, yes" shape. Unsorted data has no fence, and
binary search will confidently return nonsense. Sorting first costs O(n log n), which only pays
off if you will search many times.

### Try it in your head

1. Secret number between 1 and 1,000. Worst case, how many guesses with halving?

<details><summary>Answer</summary>
Ten. 2 to the power 10 is 1,024, which covers 1,000. Guessing one by one could take 1,000.
</details>

2. Koko eats bananas at some speed and must finish within 8 hours. Speed 3 works. Does speed 5
   work? Does speed 2? Do you know either for sure?

<details><summary>Answer</summary>
Speed 5 works for sure; eating faster never makes it harder. Speed 2 is unknown. That
one-directional certainty is the monotonic shape. You want the smallest speed that works, the
first yes.
</details>

3. `[1, 3, 5, 7]`, predicate "value at least 5." Write the row of N and Y and mark the fence.

<details><summary>Answer</summary>
N N Y Y. The fence sits between position 1 and position 2. The answer is position 2, value 5.
</details>

### Common confusions, cleared

- **"Isn't binary search only for sorted arrays?"** The "no, no, yes, yes" shape is the
  requirement, not the array. Truck sizes, eating speeds, and opening hours all have it without
  being an array of anything.
- **"Why does `lo = mid` loop forever sometimes?"** When `lo` and `hi` are one apart, `mid`
  rounds down to `lo`. Setting `lo = mid` moves nothing. Use `lo = mid + 1` after proving `mid`
  is a no.
- **"Should I use `<` or `<=` in the loop?"** Pick one style and stay in it. Closed: `lo <= hi`
  with `hi = mid - 1`. Half-open: `lo < hi` with `hi = mid`. Mixing them is the entire source
  of off-by-one bugs.
- **"What is the answer when the loop ends without finding anything?"** In the fence-finding
  template, `lo` is the boundary. If there is no yes at all, `lo` lands one past the end, a
  useful "not found" signal.

### What to do next

Scroll down to Part 2 and read §2, the fully worked `binary_search`, and trace its test with your
own table like the one above. Then read "The one template" at the top of Part 2 §3 until the fence
picture and `first_true` feel like the same thing. Then open `exercises.py` and do
`binary_search` and `search_insert_position` with a 30-minute timer. When they pass,
`min_eating_speed` is where "search on the answer" stops being a phrase and becomes something
you have done.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** `git bisect` finds the one commit that broke the build
out of a thousand by testing ten of them. Every database index is a B-tree, and each step from
root to leaf is a binary search, which is why a lookup in a billion rows touches a handful of
pages. Amazon's logistics must answer "what is the smallest truck capacity that still ships
everything by Friday?" That is exercise 9 here, `ship_within_days`, at scale. Autocomplete
finds where your prefix would sit in a sorted word list with `bisect`, then reads forward.

**The analogy.** Guessing a number between 1 and 100 when the other person only says "higher"
or "lower." Nobody guesses 1, then 2, then 3. You guess 50, then 25 or 75, and you are done in
seven guesses. Finding a word in a paper dictionary is the same move: open near the middle,
look at one word, throw away half the book. You never read the discarded pages. You have run
this algorithm since childhood.

**How it works, in plain words.** Keep two markers, the lowest and highest positions that could
still hold the answer. Look at the middle. Ask one yes/no question about it. The answer tells
you which side to keep; move one marker past the middle and the range halves. Repeat until the
range is empty. A million items takes twenty questions. The trick of this chapter: the thing
you halve does not have to be an array. It can be a range of candidate answers, like Koko's
eating speed. "Can she finish at speed 7?" If yes, every faster speed also works, so the
answers form a run of no's followed by a run of yes's, and you want the first yes.

**What learning this will feel like.** Most people arrive already disliking binary search,
because it is the algorithm where `<` versus `<=` decides whether you loop forever. Expect to
write one infinite loop and one search that skips the answer. That is not carelessness: closed
and half-open intervals have different rules, and mixing them is the bug. Section 3 gives you
one template, `first_true`, and one rule for staying inside it. The aha comes when
`min_eating_speed` and `find_min_rotated`, which look nothing alike, turn out to be the same
eight lines with a different predicate. It is not about sorted arrays. It is about any question
that flips from no to yes exactly once.

**You will know you have it when** a problem says "minimum k such that ..." and you write the
`feasible(k)` function before you write any loop.

### 1. The core idea

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

### 2. Anchor problem: Binary Search, fully worked

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

### 3. Patterns and templates in this chapter

#### The one template: first index where the predicate is True

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

#### Closed vs. half-open: pick one and know it

The anchor used a closed interval `[lo, hi]` with `while lo <= hi`. The template uses a
half-open `[lo, hi)` with `while lo < hi`. Both are correct. Mixing them is the entire source
of off-by-one bugs. The safe rule:

```
closed [lo, hi]:    while lo <= hi;  lo = mid + 1;  hi = mid - 1;  answer found inside loop
half-open [lo, hi): while lo <  hi;  lo = mid + 1;  hi = mid;      answer is lo after loop
```

Use closed when you return as soon as you find an exact match. Use half-open when you are
looking for a boundary.

#### Binary search on the answer

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

#### Rotated arrays: find which half is sorted

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

#### Two sorted arrays: partition, do not merge

For the median of two sorted arrays in O(log(min(m, n))), binary search over how many
elements you take from the shorter array to be in the left half. The partition is correct
when every element on the left is ≤ every element on the right. Four numbers to compare.

### 4. Recognition cues

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

### 5. Pitfalls

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

### 6. Exercises

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
