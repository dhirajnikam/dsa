# 09 · Recursion & Backtracking

**In one sentence.** Backtracking is trying every option one decision at a time, and whenever
a choice leads nowhere, putting it back and trying the next one.

**Why you care.** Every sudoku solver, chess engine, and regex engine runs on this. Subsets,
permutations, and combination sum are Amazon staples and Google warm-ups. Word Search and
N-Queens are the "show me you can control recursion" problems. It is also the first half of
dynamic programming, so it pays off again in chapter 10.

## The idea, with a story

You want to see *every* outfit you could wear. Three shirts, two trousers, two pairs of shoes.

You do not spread all twelve outfits on the bed. You put on shirt 1, trousers 1, shoes 1.
Look in the mirror, write it down. Take the shoes off, put shoes 2 on. Write it down. Out of
shoes, so take them off, take off trousers 1, put on trousers 2, and start again with shoes 1.
Out of trousers, swap the shirt and repeat the whole thing.

Notice the rhythm. Put something on. Go deeper. Take it off. Try the next thing. "Take it
off" is the backtrack. In code it is `path.pop()`: putting the item back on the shelf so the
next choice starts clean.

Now a rule: the red shirt clashes with the green trousers. You put on the red shirt, reach for
the green trousers, and stop. You skip both pairs of shoes for that combination because you
can already see it fails. That is *pruning*: not entering a corridor you can see is blocked.

## The same story with numbers

Find every subset of `[1, 2]`, including "nothing" and "both." At each number, one decision:
take it or skip it.

```
                     start: []
                   /            \
             take 1              skip 1
              [1]                  []
            /     \              /     \
       take 2    skip 2     take 2    skip 2
       [1, 2]      [1]        [2]        []
```

The bottom row is the four subsets. The walk goes left first, all the way down, then back up
one step, then the next branch.

| Step | Action | `path` now |
|------|--------|------------|
| 1 | take 1 | [1] |
| 2 | take 2 | [1, 2], record |
| 3 | put 2 back | [1] |
| 4 | skip 2 | [1], record |
| 5 | put 1 back | [] |
| 6 | skip 1, take 2 | [2], record |
| 7 | put 2 back | [] |
| 8 | skip 2 | [], record |

Every "take" is matched by a "put back," so `path` is always exactly what it was when control
returns to a fork.

Pause and predict: for `[1, 2, 3]`, how many boxes in the bottom row, and how many rows of
decisions?

<details><summary>Answer</summary>
Eight boxes, three rows. Each number doubles the count: 2 × 2 × 2 = 8. That is 2ⁿ, which is
why the answer is exponential no matter how clever you are.
</details>

## The anchor problem: Subsets

Given distinct integers `nums`, return every subset. Any order. `[1, 2, 3]` gives 8 lists.

**Brute force.** There is nothing smaller than 2ⁿ outputs, so any method that makes each
exactly once is optimal. The question is *how* to make them without missing or repeating.

**Insight.** The current `path` is itself a valid subset, so record it at every node. Then
try appending each element *after* `start`, recurse, and undo. The `start` index is what stops
`[1, 2]` and `[2, 1]` from both appearing.

```python
def subsets(nums):
    out = []
    def backtrack(start, path):
        out.append(path[:])              # every node in this tree is an answer; COPY
        for i in range(start, len(nums)):
            path.append(nums[i])         # choose
            backtrack(i + 1, path)       # explore: only look forward
            path.pop()                   # un-choose
    backtrack(0, [])
    return out
```

**Complexity.** O(n · 2ⁿ) time, since 2ⁿ subsets are each copied in up to O(n). O(n) extra
space for the recursion and path, not counting the output.

**What to say.** "Each element is in or out, so there are 2ⁿ subsets and any solution is at
least that. I backtrack with a start index so each subset is built in one order and never
repeated. Append, recurse, pop. Time is the size of the output."

## Templates you memorize

**The skeleton.** Every problem in this chapter is this with different blanks: goal, choices,
validity, how state advances.
```python
def solve(...):
    out, path = [], []
    def backtrack(state):
        if GOAL(state):
            out.append(path[:])         # copy!
            return
        for choice in CHOICES(state):
            if not VALID(choice, state):
                continue                # prune
            path.append(choice)         # choose
            backtrack(NEXT(state, choice))
            path.pop()                  # un-choose
    backtrack(INITIAL)
    return out
```

**Combinations: a `start` index.** Order inside the answer does not matter, so only look
forward. To allow reusing an element, recurse with `i` instead of `i + 1`.
```python
def combinations(n, k):
    out = []
    def backtrack(start, path):
        if len(path) == k:
            out.append(path[:]); return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    backtrack(1, [])
    return out
```

**Permutations: a `used` list.** Order matters, so every unused element is a candidate at
every level. The tree has `n!` leaves.
```python
def permutations(nums):
    out, used = [], [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            out.append(path[:]); return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True; path.append(nums[i])
            backtrack(path)
            path.pop(); used[i] = False
    backtrack([])
    return out
```

**Duplicates in the input: sort, then skip.** At one level, never start a branch with a value
equal to the one you just finished.
```python
nums.sort()
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue                        # same value already tried at this level
    ...
```
For permutations with duplicates the skip is `nums[i] == nums[i-1] and not used[i-1]`.

**Grid search: mark, recurse, unmark.** The board itself is the `used` set.
```python
def dfs(r, c, k):                       # does word[k:] start at (r, c)?
    if k == len(word): return True
    if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[k]: return False
    saved, board[r][c] = board[r][c], "#"
    found = any(dfs(r + dr, c + dc, k + 1) for dr, dc in DIRS)
    board[r][c] = saved
    return found
```

## When you see X, think Y

| You see | Think |
|---------|-------|
| "all subsets", "power set" | skeleton with `start`, record at every node |
| "all combinations of size k" | `start` index, stop when `len(path) == k` |
| "all permutations", "arrangements" | `used` list, every element a candidate each level |
| "sum to target", "unlimited reuse" | pass `remaining`, recurse with `i` (reuse) or `i + 1` |
| "input has duplicates", "unique results" | sort, then `i > start and nums[i] == nums[i-1]` |
| "generate all valid ..." (parentheses, IPs) | build one piece at a time, prune bad prefixes |
| "does a word exist in the grid" | DFS with mark and unmark |
| "place n things so none conflict" | one row per level, sets for the conflict lines |
| small n (20 or less), "return all" | this whole chapter; complexity is the output size |

## Words you will hear

- **Recursion.** A function that calls itself on a smaller version of the problem.
- **Decision tree.** The picture above. Each fork is a choice, each bottom box a candidate.
- **Path.** The choices made so far. The outfit you currently have on.
- **Choose / explore / un-choose.** Append to path, recurse, pop from path.
- **Pruning.** Skipping a branch you can already see will fail. The red-shirt rule.
- **Permutation.** An ordering. `[1, 3]` and `[3, 1]` are different. There are `n!` of them.
- **Combination.** A subset of a fixed size, order ignored. "Choose 2 of 4."
- **Start index.** Only look at items after the one you just took, so no set is built twice.

## Mistakes everyone makes once

- **Appending `path` instead of `path[:]`.** Every entry in `out` is the same list, and it is
  empty at the end because every append was popped. Copy at the leaf.
- **Forgetting to pop.** The path grows forever and every later branch is polluted.
- **`i > 0` instead of `i > start`** in the duplicate skip. It also skips legitimate branches
  at deeper levels.
- **Word Search without restoring the cell.** Later searches that need that cell break.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `subsets` | Medium | The anchor. Write it without looking. |
| 2 | `subsets_with_dup` | Medium | Sort, then skip `nums[i] == nums[i-1]` when `i > start`. |
| 3 | `permutations` | Medium | `used` list. Goal: `len(path) == n`. |
| 4 | `permutations_unique` | Medium | Sort. Skip if `nums[i] == nums[i-1] and not used[i-1]`. |
| 5 | `combinations` | Medium | `start` index, stop at `len(path) == k`. |
| 6 | `combination_sum` | Medium | Pass `remaining`. Recurse with `i`, not `i + 1`, to allow reuse. |
| 7 | `combination_sum_ii` | Medium | Sort. Recurse with `i + 1`. Duplicate skip. `break` when candidate > remaining. |
| 8 | `letter_combinations` | Medium | One digit per level; choices are that digit's letters. Empty input gives `[]`. |
| 9 | `generate_parentheses` | Medium | Add `(` if `open < n`; add `)` if `close < open`. |
| 10 | `word_search` | Medium | DFS from every cell equal to `word[0]`. Mark `"#"`, recurse, restore. |
| 11 | `palindrome_partition` | Medium | At `start`, try every `end` where `s[start:end]` is a palindrome. |
| 12 | `n_queens` | Hard | Row by row. Sets for `col`, `r + c`, `r - c`. Build the strings at the leaf. |
| 13 | `restore_ip_addresses` | Medium | Four pieces of 1 to 3 chars, value 255 or less, no leading zero unless `"0"`. |
| 14 | `sudoku_solver` | Hard | Find the first `"."`, try `1` to `9` not in that row, column, or box, recurse, undo. |

Start with 1 and 3 today. Do 2 to 9 over the week; they are the skeleton with different
blanks. 10 to 14 are for when the first nine pass cold.
