# Phase 15: Greedy

**Goal:** spot when the locally best choice is always safe, and say why in one sentence.

## Key idea
Greedy builds the answer one choice at a time and never goes back.
It works only when the best choice now never blocks a better answer later. Check with a tiny counterexample first.
Most greedy problems are "sort by the right key, then one pass". If it breaks, use DP.

## Cheat sheet
```python
# sort then scan: keep the interval that ends earliest
intervals.sort(key=lambda iv: iv[1])
count, last_end = 0, float("-inf")
for s, e in intervals:
    if s >= last_end:          # does not overlap the last one kept
        count, last_end = count + 1, e
# reach / jump: track the farthest index you can get to
farthest = 0
for i, step in enumerate(nums):
    if i > farthest: return False    # gap we can never cross
    farthest = max(farthest, i + step)
# two passes when a rule looks at both neighbours
res = [1] * n
for i in range(1, n):               # satisfy the left neighbour
    if a[i] > a[i-1]: res[i] = res[i-1] + 1
for i in range(n - 2, -1, -1):      # satisfy the right neighbour, keep the max
    if a[i] > a[i+1]: res[i] = max(res[i], res[i+1] + 1)
```

## When you see... use...
- "max number of non-overlapping intervals" -> sort by end, keep if it starts after last end
- "can you reach the end / min jumps" -> track farthest reachable
- "rule depends on both neighbours" -> two passes, left then right
- "find a start index around a circle" -> running total, reset when it goes negative

## Common mistakes
- Sorting by start instead of end for interval problems.
- Mixing up `>=` and `>` at boundaries. Touching intervals may or may not overlap. Read the statement.
- Using greedy when a small counterexample breaks it. Coin change with coins [1, 3, 4] is DP.
- Skipping the feasibility check. Gas station needs total gas >= total cost.

## Problems
- `01_jump_game.py` — track farthest reachable
- `02_jump_game_ii.py` — count levels of reach
- `03_gas_station.py` — running total, reset on negative
- `04_assign_cookies.py` — sort both, two pointers
- `05_partition_labels.py` — extend end to last occurrence
- `06_candy.py` — two passes, left then right
- `07_min_arrows_burst_balloons.py` — sort by end, count groups
