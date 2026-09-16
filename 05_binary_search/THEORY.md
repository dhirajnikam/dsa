# 05 · Binary Search, explained from zero

Read this first if "binary search" sounds like something only sorted arrays are allowed to do,
or if `lo`, `mid`, and `hi` have ever made you loop forever. When it clicks, open `LESSON.md`,
the dense reference. This file is the friendly conversation before it.

## In one sentence

Binary search is "ask one yes/no question, throw away half of what is left, repeat," and it
works on anything where the answers line up as a run of no's followed by a run of yes's.

## Start with something you already do

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

## Now the same thing with numbers

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

## The words people use

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

## Why the fast way is fast

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

## Try it in your head

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

## Common confusions, cleared

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

## What to do next

Open `LESSON.md` and read §2, the fully worked `binary_search`, and trace its test with your
own table like the one above. Then read "The one template" at the top of §3 until the fence
picture and `first_true` feel like the same thing. Then open `exercises.py` and do
`binary_search` and `search_insert_position` with a 30-minute timer. When they pass,
`min_eating_speed` is where "search on the answer" stops being a phrase and becomes something
you have done.
