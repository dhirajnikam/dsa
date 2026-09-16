# 10 · Dynamic Programming

**In one sentence.** Dynamic programming is ordinary recursion where you write down each
answer the first time you find it, so you never work it out twice.

**Why you care.** Autocorrect computes edit distance. `git diff` runs longest common
subsequence over two files. Google asks DP as the second problem after a warm-up. Amazon
leans on the easier families: climbing stairs, house robber, coin change. Both love to hear
you say "memoize" before you say "table."

## The idea, with a story

A staircase with 5 steps. Each move you climb 1 step or 2. How many different ways can you
reach the top?

Think about the *last* move. You either stepped up 1 from step 4 or up 2 from step 3. So the
ways to reach step 5 is the ways to reach step 4 plus the ways to reach step 3. To answer
"step 5," you ask two smaller versions of the same question. That is the whole idea.

Now the friend. Every few minutes a friend asks "how many ways to reach step 3?" You work it
out. Five minutes later they ask again. Eventually you write the answer on a sticky note and
slap it on the wall. Next time, you point at the note.

Memoization is sticky notes. That is the entire secret. A table is sticky notes arranged in
order, filled in left to right before anyone asks.

## The same story with numbers

Ask for step 5 the naive way. Every question spawns two smaller ones until you hit steps 0
and 1, which each have one way.

```
                    ways(5)
                  /         \
            ways(4)          ways(3)*
           /      \         /      \
      ways(3)*  ways(2)#  ways(2)#  ways(1)
      /     \    /    \    /    \
  ways(2)# ways(1) ...  ...

  * asked 2 times    # asked 3 times
```

Step 5 costs 15 questions. Step 40 costs over two billion, most of them repeats.

With sticky notes, each step is answered once. Same thing as a row of boxes, left to right:

| Step | 0 | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|---|
| Ways | 1 | 1 | 2 | 3 | 5 | 8 |

Each box is the sum of the two to its left. Six boxes, six additions. Sticky notes and the
row of boxes are the *same* method.

Pause and predict: what goes in box 6, and which two boxes did you use?

<details><summary>Answer</summary>
13, from boxes 5 and 4: 8 + 5. You never looked at boxes 0 to 3 again.
</details>

## The anchor problem: Climbing Stairs

You climb `n` steps. Each move goes up 1 or 2. Count the distinct sequences of moves that
reach the top. `2` gives 2, `3` gives 3, `5` gives 8.

**Brute force.** The last move was 1 step from `n-1` or 2 from `n-2`. O(2ⁿ) because the tree
above re-solves the same steps.

```python
def ways(n):                          # stage 1: honest recursion
    if n <= 1:
        return 1
    return ways(n - 1) + ways(n - 2)
```

**Insight.** The only thing that identifies a subproblem is `n`. There are `n + 1` values. If
I never solve the same `n` twice, I do O(n) work. Stage 2 is the tree above with the repeats
circled. Stage 3 adds sticky notes:

```python
from functools import lru_cache

def climbing_stairs(n):               # stage 3: memoized
    @lru_cache(maxsize=None)
    def ways(i):
        if i <= 1:
            return 1
        return ways(i - 1) + ways(i - 2)
    return ways(n)
```

Stage 4 is the row of boxes, filled from the base cases upward:

```python
def climbing_stairs(n):               # stage 4: bottom-up
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

Stage 5 notices each box only looks back two, so two variables suffice:

```python
def climbing_stairs(n):               # stage 5: two variables
    a, b = 1, 1                       # ways(i-2), ways(i-1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

Stages 1 to 3 get full marks at almost every company. Stages 4 and 5 are the follow-ups.

**Complexity.** O(n) time. Space O(n) memoized or tabulated, O(1) with two variables.

**What to say.** "The last move is 1 or 2 steps, so ways(n) = ways(n-1) + ways(n-2). Naively
that is exponential because subproblems repeat. There are only n+1 distinct subproblems, so
memoizing makes it O(n). Each cell depends on the previous two, so two variables give O(1)
space."

## Templates you memorize

**The sentence and the four questions.** Write these before any code. If you cannot finish
the sentence in plain words, you do not have a solution yet.

| Question | Climbing Stairs answer |
|----------|------------------------|
| **State.** "dp[i] means ___." | dp[i] means the number of ways to reach step i. |
| **Base case.** Which boxes fill by hand? | dp[0] = 1, dp[1] = 1. |
| **Transition.** How does a box come from smaller ones? | dp[i] = dp[i-1] + dp[i-2]. |
| **Answer.** Which box holds the result? | dp[n]. |

**Memoized recursion.** Write this every time, then decide whether to convert it.
```python
from functools import lru_cache

def solve(inputs):
    @lru_cache(maxsize=None)
    def f(state):                  # state must be hashable: ints, tuples, strings
        if base_case(state):
            return base_value
        return combine(f(smaller) for smaller in choices(state))
    return f(start_state)
```

**1-D table: take or skip.** House Robber. `dp[i]` is the best using houses `0..i`. Skip
house `i`, or take it plus the best up to `i-2`.
```python
def rob(nums):
    prev2 = prev1 = 0               # best up to i-2, best up to i-1
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
```
Coin Change is the same shape over amounts: `dp[a] = min(dp[a - c] + 1 for c in coins)`.

**2-D table: two strings.** `dp[i][j]` is the answer for prefixes `s[:i]` and `t[:j]`. Row 0
and column 0 are the base cases. The transition asks: do the last letters match?
```python
def lcs(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1          # match: diagonal + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # else: best of up, left
    return dp[m][n]
```
Edit distance is the same table with `1 + min(up, left, diagonal)` on a mismatch.

## When you see X, think Y

| You see | Think |
|---------|-------|
| "number of ways", "minimum cost", "is it possible" | DP candidate; write the recursion first |
| "adjacent cannot both be chosen" | take or skip, two variables |
| "pick each item once", "subset with sum" | 0/1 knapsack; fill sums downward |
| "unlimited coins", "fewest coins" | unbounded knapsack; fill sums upward |
| "two strings", "subsequence", "edit" | 2-D table over prefixes `(i, j)` |
| "grid, move right or down" | `dp[r][c] = dp[r-1][c] + dp[r][c-1]` |
| "split a string into words / digits" | `dp[i]` over prefixes, look back over the last piece |
| "palindrome" | expand around each centre |
| "buy / sell / cooldown" | state machine, one variable per mode |

## Words you will hear

- **Subproblem.** A smaller version of the same question. Step 3 is a subproblem of step 5.
- **Overlapping subproblems.** The same small question appears many times. The signal for DP.
- **State.** What identifies one subproblem. The label on a sticky note.
- **Transition.** The rule for filling a box from smaller boxes.
- **Base case.** The boxes you fill by hand.
- **Memoization / top-down.** Sticky notes on the recursion. `@lru_cache` does it in one line.
- **Tabulation / bottom-up.** Fill boxes from the base cases toward the answer with a loop.
- **0/1 versus unbounded knapsack.** Each item once, or as many times as you like.

## Mistakes everyone makes once

- **Starting with the table.** The table is a transcription of the recursion. Write the
  recursion, draw the tree for a small input, circle the repeats.
- **Forgetting the empty base case.** Ways to make amount 0 is 1, not 0. A wrong seed zeros
  the whole table.
- **Wrong loop direction in knapsack.** Downward for each-item-once, upward for reuse. Trace
  one coin over amounts 0 to 4 to see why.
- **Off-by-one in two-string tables.** `dp[i][j]` covers `s[:i]`, so compare `s[i-1]`. Size
  the table `(m+1) × (n+1)`.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `climbing_stairs` | Easy | The anchor. All five stages, then keep the two-variable one. |
| 2 | `min_cost_climbing_stairs` | Easy | `dp[i]` is the cheapest way to stand on step `i`. Answer is the min of the last two. |
| 3 | `house_robber` | Medium | Take `x + prev2` or skip and keep `prev1`. |
| 4 | `house_robber_ii` | Medium | Circular: rob `nums[1:]` and `nums[:-1]`, take the max. Handle one house first. |
| 5 | `longest_palindromic_substring` | Medium | Expand around each of the `2n-1` centres. |
| 6 | `count_palindromic_substrings` | Medium | Same expansion; count every successful step outward. |
| 7 | `decode_ways` | Medium | `dp[i]` over prefixes. One digit if not `'0'`; two digits if `10..26`. |
| 8 | `coin_change` | Medium | Unbounded knapsack with `min`. Fill amounts upward. |
| 9 | `coin_change_ii` | Medium | Coins outside, amounts inside, `+=`. That order counts each set once. |
| 10 | `max_product_subarray` | Medium | Track running max and running min; a negative swaps them. |
| 11 | `word_break` | Medium | `dp[i]`: prefix of length `i` is breakable. Look back over all `j < i`. |
| 12 | `length_of_lis` | Medium | Write O(n²) first, then `bisect_left` on a tails list. |
| 13 | `can_partition` | Medium | Odd total is `False`. Then subset sum for `total // 2`, sums downward. |
| 14 | `unique_paths` | Medium | One row: `row[c] += row[c-1]`, once per row. |
| 15 | `longest_common_subsequence` | Medium | The 2-D template above. |
| 16 | `edit_distance` | Medium | Same table; row 0 and column 0 are `i` and `j`; mismatch is `1 + min` of three. |
| 17 | `max_profit_with_cooldown` | Medium | Three states: `hold`, `sold`, `rest`. Write the transitions before coding. |
| 18 | `target_sum_ways` | Medium | The plus-set `P` satisfies `2P = target + total`. Count subsets summing to `P`. |
| 19 | `interleaving_string` | Medium-Hard | `dp[i][j]`: `s1[:i]` and `s2[:j]` interleave into `s3[:i+j]`. |
| 20 | `burst_balloons` | Hard | Pad with 1s. `dp[l][r]` over open intervals; choose the balloon that pops last. |
| 21 | `regex_match` | Hard | `dp[i][j]` over prefixes. On `*`, use zero of the preceding char or consume one from `s`. |

Start with 1 and 3 today. Say what `dp[i]` means out loud before writing either. Then 2 to
18 in order. 19 to 21 are for when those pass cold.
