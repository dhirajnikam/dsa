# Phase 14: Dynamic Programming

**Goal:** turn a slow recursion into a fast one by remembering answers you already computed.

## Key idea
Every DP problem is a recursion that solves the same small subproblem many times.
Write the brute-force recursion first, then cache it (top-down) or fill a table (bottom-up).
To find the recursion, ask: "what is the last choice I make, and what does the rest look like?"

## Cheat sheet
```python
from functools import lru_cache
@lru_cache(maxsize=None)          # top-down: recursion + cache, easiest to write
def f(i):
    if i < 2: return i            # base case
    return f(i - 1) + f(i - 2)    # recurrence

dp = [0, 1] + [0] * (n - 1)       # bottom-up 1D: dp[i] = answer for first i items
for i in range(2, n + 1): dp[i] = dp[i - 1] + dp[i - 2]

for x in nums:                    # 0/1 knapsack (each item once): right to left
    for c in range(target, x - 1, -1): dp[c] = dp[c] or dp[c - x]
for coin in coins:                # unbounded knapsack (reuse items): left to right
    for a in range(coin, amount + 1): dp[a] += dp[a - coin]
```

## When you see... use...
- "count the ways to reach n" or "min cost to reach the end" -> 1D dp[i]
- "subset with sum / pick items at most once" -> 0/1 knapsack, loop right to left
- "coins reusable / min count / count combinations" -> unbounded knapsack, left to right
- "two strings, common / transform" -> 2D table dp[i][j] over prefixes a[:i], b[:j]
- "best over subarray i..j, order of removal matters" -> interval DP, fill by length

## Common mistakes
- `[[0] * m] * n` shares one row. Use a list comprehension.
- Off-by-one in string DP. Table size `(n+1) x (m+1)`, read chars as `a[i-1]`.
- Wrong knapsack loop direction. 0/1 right to left, unbounded left to right.

## Problems
- `01_climbing_stairs.py` — dp[i] = dp[i-1] + dp[i-2]
- `02_house_robber.py` — skip or take, no adjacent
- `03_house_robber_ii.py` — circular, run robber twice
- `04_coin_change.py` — unbounded knapsack, min count
- `05_coin_change_ii.py` — count combinations, coins outer loop
- `06_longest_increasing_subsequence.py` — dp[i] ending at i, then bisect
- `07_partition_equal_subset_sum.py` — boolean 0/1 knapsack
- `08_unique_paths.py` — grid, count paths from top and left
- `09_min_path_sum.py` — grid, min of top and left
- `10_longest_common_subsequence.py` — 2D two strings
- `11_edit_distance.py` — 2D, insert / delete / replace
- `12_word_break.py` — 1D over string positions
- `13_decode_ways.py` — 1D, one or two digit steps
- `14_longest_palindromic_substring.py` — expand around center
- `15_burst_balloons.py` — interval DP, pick last balloon
- `16_house_robber_iii_tree_dp.py` — (rob, skip) per subtree
