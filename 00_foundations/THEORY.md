# 00 · Foundations, explained from zero

Read this first if "Big-O" and "recursion" make your eyes glaze. When it clicks, open
`LESSON.md`, which is the dense reference. This file is the friendly conversation before it.

## In one sentence

Big-O is a way of saying "how much slower does this get when the input gets bigger," and
recursion is "solve a big problem by solving a slightly smaller copy of it."

## Start with something you already do

**Big-O.** You are looking for a friend's name in a phone book.

- If the book is sorted, you open it in the middle, see you are too far, open the middle of
  the first half, and so on. A book with 1,000 pages takes about 10 opens. A book with
  1,000,000 pages takes about 20. Doubling the book adds *one* open. That is O(log n).
- If someone shuffled the pages, you must flip through one by one. 1,000 pages, up to 1,000
  flips. Doubling the book doubles the flips. That is O(n).
- If you have to compare every person in the book with every other person (say, to find two
  with the same birthday the slow way), 1,000 people means about 1,000,000 comparisons.
  Doubling the book *quadruples* the work. That is O(n²).

Big-O does not care whether a flip takes one second or one millisecond. It only cares about
the *shape* of the growth: flat, logarithmic, linear, quadratic. That shape decides whether
your code finishes in a blink or never.

**Recursion.** You are the CEO and want to know how many people work in the company. You do
not count. You ask each of your two VPs: "how many people report to you, including you?"
Each VP asks their managers the same question. Each manager asks their leads. At the bottom,
an employee with no reports answers "1." Answers flow back up, each person adding 1 for
themself. You add the two VP numbers plus one and you are done. You never counted anyone
yourself. You trusted the smaller version of the same question.

## Now the same thing with numbers

**Counting steps.** How many times does `hello` print?

```python
for i in range(4):          # i = 0, 1, 2, 3
    for j in range(4):      # j = 0, 1, 2, 3
        print("hello")
```

The outer loop runs 4 times; each time, the inner loop runs 4 times. 4 × 4 = 16. With
`range(n)` in both, it is n × n = n². Pause and predict: what if the inner loop were
`range(i)` instead of `range(4)`?

<details><summary>Answer</summary>
0 + 1 + 2 + 3 = 6 prints. In general, n(n−1)/2, which still grows like n². Half of a square
is still a square shape. Big-O drops the ½: O(n²).
</details>

**Recursion.** Add up a list by trusting a smaller list.

```python
def total(nums):
    if not nums:                    # empty list: the answer is 0. This is the base case.
        return 0
    return nums[0] + total(nums[1:])   # first item + (trust this to sum the rest)
```

Trace `total([5, 2, 9])`:

```
total([5, 2, 9]) = 5 + total([2, 9])
                       total([2, 9]) = 2 + total([9])
                                           total([9]) = 9 + total([])
                                                            total([]) = 0
                                           total([9]) = 9 + 0 = 9
                       total([2, 9]) = 2 + 9 = 11
total([5, 2, 9]) = 5 + 11 = 16
```

Notice you go *down* to the base case, then answers come back *up*. That staircase picture is
every recursive function you will ever write.

## The words people use

- **n.** The size of the input. Ten numbers, n = 10. A million, n = 1,000,000.
- **O(1), "constant."** Same work no matter how big n is. Opening box 7 in an array.
- **O(log n), "logarithmic."** Each step cuts the problem in half. Phone book, sorted.
- **O(n), "linear."** Touch every item once. One pass through a list.
- **O(n log n).** Sorting. A little worse than one pass, much better than a square.
- **O(n²), "quadratic."** Every item against every other item. Two nested loops.
- **O(2ⁿ), "exponential."** Doubles with every extra item. Trying every subset. Fine for
  n ≤ 20, hopeless past that.
- **Time complexity.** Big-O of how long it runs.
- **Space complexity.** Big-O of how much *extra* memory you use. A notepad of n things is O(n).
- **Base case.** The smallest input a recursive function answers directly, with no further calls.
  An empty list. A tree with no nodes. n = 0.
- **Recursive case.** The line where the function calls itself on something smaller.
- **Call stack.** The pile of unfinished function calls waiting for their answers. In the trace
  above, it was four deep. Python gives up around 1,000 deep unless you raise the limit.
- **Memoization.** Writing down the answer to each recursive call so you never compute it twice.
  A fancy word for a notepad. It is the seed of Chapter 10.
- **Constraints.** The line in the problem that says `n ≤ 100,000`. It tells you which Big-O
  will pass. Read it first, always.

## Why this matters more than it looks

A computer does roughly 100,000,000 simple steps per second. Now read a constraint.

| Constraint says | O(n²) steps | O(n log n) steps | Verdict |
|-----------------|-------------|------------------|---------|
| n ≤ 1,000 | 1,000,000 | 10,000 | either is fine |
| n ≤ 100,000 | 10,000,000,000 | 1,700,000 | O(n²) takes 100 seconds; you need better |
| n ≤ 20 | 400 | 86 | anything works, even trying all 2²⁰ ≈ 1,000,000 subsets |

So `n ≤ 100,000` means "do not write two nested loops" and `n ≤ 20` means "the brute force
is the answer, they want you to enumerate." Reading that line saves you ten minutes of
wandering in the interview.

## Try it in your head

1. A loop that halves `n` each time until it hits 1. `n = 64`. How many times does it run?
   What is the Big-O?

<details><summary>Answer</summary>
64 → 32 → 16 → 8 → 4 → 2 → 1: six halvings. 2⁶ = 64, so log₂(64) = 6. O(log n).
</details>

2. `factorial(4)` is defined as `4 × factorial(3)`, with `factorial(1) = 1`. Write the staircase.

<details><summary>Answer</summary>
factorial(4) = 4 × factorial(3) = 4 × (3 × factorial(2)) = 4 × (3 × (2 × factorial(1)))
= 4 × 3 × 2 × 1 = 24. Depth of the call stack: 4.
</details>

3. You sort a list (O(n log n)) and then loop over it once (O(n)). Total Big-O?

<details><summary>Answer</summary>
O(n log n). When steps happen one after another, the biggest one wins. You only multiply
when one loop is *inside* another.
</details>

## Common confusions, cleared

- **"Isn't O(2n) worse than O(n)?"** No. Big-O drops constant multipliers. Two passes over the
  list is still O(n). What matters is the shape, not the count of passes.
- **"How can a function call itself? Doesn't it loop forever?"** Only if you forget the base
  case or fail to make the input smaller. Every recursive call must move toward the base case.
  Check those two things and it always terminates.
- **"I have to trace the whole recursion to trust it."** You do not, and trying to is what makes
  recursion feel impossible. Check the base case is right. Check that *if* the smaller call is
  right, your one line combining it is right. That is the entire proof. Then stop tracing.
- **"Python is slow, so Big-O matters less."** The opposite. Python is about 50× slower than C,
  so a bad Big-O hurts you sooner. That is why 10⁸ steps per second is a generous estimate here.

## What to do next

Open `LESSON.md` and read §2, the Python page, with a terminal open. Type each line. Then read
§3 on Big-O and check that the table there now looks obvious. Then do `word_frequencies` and
`merge_sorted` in `exercises.py`. Save `fast_pow` and `flatten` for a second sitting: they are
recursion, and recursion is better learned after a night's sleep on the staircase picture.
