# 09 · Recursion & Backtracking

> Backtracking is brute force with manners. You still try everything, but you build each
> candidate one decision at a time, and the moment a partial candidate cannot possibly work,
> you undo the last decision and try the next. One template generates every subset,
> permutation, combination, and path you will ever be asked for.

**Interview frequency:** high. Subsets, permutations, and combination sum are Amazon staples
and common Google warm-ups. Word Search, N-Queens, and Sudoku are the "show me you can
control recursion" problems. Backtracking is also the first half of dynamic programming, so
everything here pays off again in chapter 10.

## 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** Every sudoku solver fills the grid by trying a value,
moving on, and undoing it when it hits a contradiction. Chess engines explore a tree of moves
the same way, abandoning branches that cannot win. Regex engines backtrack when a match fails
partway, and compilers do it while parsing ambiguous grammar. Amazon's constraint-based
scheduling of shifts and deliveries
searches for an assignment that breaks no rule. Test-case generators and configuration search
enumerate options the same way. Whenever the question is "find every arrangement" or "find
any arrangement that obeys these rules," this is the engine underneath.

**The analogy.** A wardrobe with three drawers: shirts, trousers, shoes. To see every outfit,
pick a shirt, then trousers, then shoes, and write the outfit down. Put the shoes back and
try the next pair. When you run out of shoes, put the trousers back and try the next
trousers. You never lay every outfit on the bed at once. You build one at a time, and
putting an item back is what lets the next choice start clean. That is `path.pop()`.

**How it works, in plain words.** Draw a tree. The root is "nothing decided yet." Each branch
is one decision: take this element or skip it, put this digit in this cell, add an open or a
close paren. A leaf is a complete candidate. The recursion walks the tree: make a choice,
recurse to make the next one, and when that call returns, undo the choice and try the next
branch. The `path` list is the road from the root to where you stand. Pruning means noticing
a branch cannot reach a valid leaf and never walking down it. That is the whole difference
between backtracking and blind enumeration.

**What learning this will feel like.** Two things will bother you. First: "how does
`path.pop()` undo the choice when the recursive call already used it?" The list is shared,
and every call below you appends and pops in matched pairs, so when control comes back,
`path` is exactly as you left it. Trace Subsets on `[1, 2, 3]` once with a pen and the
mystery ends. Second, exponential blow-up: your instinct says O(2ⁿ) must be wrong. Look at
the constraints. When a problem says `n ≤ 20`, the interviewer is telling you
the output itself is exponential and this is the intended approach. The bug you will write
once is appending `path` instead of `path[:]` and getting a list of identical empty lists.

**You will know you have it when** you read "return all combinations" and your hand writes
choose, explore, un-choose before your brain finishes the sentence.

## 1. The core idea

Every backtracking problem is a walk through a **decision tree**. At each level you make one
choice; a leaf is a complete candidate. The recursion explores the tree, and the "backtrack"
is simply returning from a call and undoing what that call added.

```
brute force (enumerate, then filter)      backtracking (build, prune, undo)
for every string of 2n parens:            def go(path, open, close):
    if balanced(s): out.append(s)             if len(path) == 2n: out.append(path); return
                                              if open < n:  go(path + "(", open+1, close)
                                              if close < open: go(path + ")", open, close+1)
2^(2n) candidates, most invalid           only valid prefixes are ever extended
```

Three things define any backtracking solution. Say them out loud when you plan:

1. **The choice at each step.** Include this element or not? Which element goes next? Which
   digit goes in this cell?
2. **The constraint that prunes.** Sum too big, letter already used, queen attacked. Pruning
   is what separates backtracking from blind enumeration.
3. **The goal that ends a branch.** Path is complete, index reached the end, target hit zero.

The recognition cue is the **output**: if the problem asks for *all* solutions, or for *any*
arrangement satisfying constraints, and `n` is small (about 20 or less), it wants backtracking.
Output size is exponential, so the algorithm must be too; do not apologize for the complexity.

## 2. Anchor problem: Subsets, worked three ways

**Problem.** Given distinct integers `nums`, return every subset (the power set). Any order.

**Understand.** Distinct, so no duplicate subsets to worry about. The empty set counts. For
`n` elements there are exactly 2ⁿ subsets, so the answer for `n = 3` has 8 lists.

**Examples.** `[1, 2, 3] → [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]`. `[] → [[]]`.
`[0] → [[], [0]]`.

**Brute force.** There is nothing smaller than 2ⁿ outputs, so any method that produces each
exactly once is optimal. The question is *how* to produce them without missing or repeating.

**Insight, way 1: include / exclude.** Walk the elements left to right. For each one, you make
a binary decision: it is in the subset, or it is not. The recursion tree has depth `n` and 2ⁿ
leaves, one per subset.

```
                          []
                 /                  \
          take 1                     skip 1
           [1]                        []
        /       \                  /       \
   take 2      skip 2         take 2      skip 2
   [1,2]        [1]            [2]          []
   /   \        /   \          /   \        /   \
[1,2,3][1,2] [1,3] [1]      [2,3] [2]     [3]   []      <- 8 leaves = 8 subsets
```

```python
def subsets(nums):
    out = []
    def go(i, path):
        if i == len(nums):            # every element decided: a leaf
            out.append(path[:])       # COPY; path keeps changing
            return
        path.append(nums[i])          # decision A: take nums[i]
        go(i + 1, path)
        path.pop()                    # undo, so decision B starts clean
        go(i + 1, path)               # decision B: skip nums[i]
    go(0, [])
    return out
```

**Insight, way 2: iterative doubling.** Start with `[[]]`. For each number, every existing
subset spawns a copy with that number appended. The list doubles `n` times.

```python
def subsets(nums):
    out = [[]]
    for x in nums:
        out += [s + [x] for s in out]     # [[]] -> [[],[1]] -> [[],[1],[2],[1,2]] -> ...
    return out
```

**Insight, way 3: the general backtracking template.** At each call, the current `path` is
itself a valid subset, so record it. Then try appending each element *after* `start`, recurse,
and undo. The `start` index is what prevents `[1, 2]` and `[2, 1]` from both appearing.

```python
def subsets(nums):
    out = []
    def backtrack(start, path):
        out.append(path[:])              # every node in this tree is an answer
        for i in range(start, len(nums)):
            path.append(nums[i])         # choose
            backtrack(i + 1, path)       # explore
            path.pop()                   # un-choose
    backtrack(0, [])
    return out
```

Way 3 is the one to memorize. Change what you record and what you skip, and it becomes every
other problem in this chapter.

**Test trace, way 3, `[1, 2, 3]`.** `backtrack(0, [])` records `[]`. i=0: path=`[1]` →
`backtrack(1)` records `[1]`; i=1: `[1,2]` → records `[1,2]`; i=2: `[1,2,3]` → records, loop
empty, pop → `[1,2]`; pop → `[1]`; i=2: `[1,3]` → records, pop → `[1]`; pop → `[]`. i=1:
`[2]` → records `[2]`; i=2: `[2,3]` → records; pops. i=2: `[3]` → records; pop. Eight lists,
each once. ✓

**Complexity.** O(n · 2ⁿ) time: 2ⁿ subsets, each copied in up to O(n). O(n) extra space for
the recursion stack and path, not counting the output.

**What to say out loud.** "Each element is either in or out, so there are 2ⁿ subsets and any
solution is at least that. I will backtrack with a start index so each subset is generated in
one canonical order and never repeated. I append, recurse, pop. Time O(n · 2ⁿ), which is the
size of the output."

## 3. Patterns & templates in this chapter

### The universal template

```python
def solve(...):
    out = []
    path = []
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

Fill in five blanks: goal, choices, validity, how state advances, initial state. Every
problem below is this template with different blanks.

### Combinations: a `start` index

When order inside the answer does not matter (`[1, 2]` is the same as `[2, 1]`), only look
forward: `for i in range(start, n)` and recurse with `i + 1`. To allow reusing the same
element (Combination Sum), recurse with `i` instead of `i + 1`.

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

A pruning bonus: if even taking every remaining number cannot fill `k` slots, stop the loop:
`for i in range(start, n - (k - len(path)) + 2)`.

### Permutations: a `used` set

When order matters, every element is a candidate at every level except the ones already on
the path. Track them with a boolean list or a set. The tree has `n!` leaves.

```python
def permutations(nums):
    out = []
    used = [False] * len(nums)
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

### Duplicates in the input: sort, then skip

Sort first so equal values are adjacent. Then, at one level of the tree, never start a
branch with a value equal to the one you just finished a branch with.

```python
nums.sort()
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue                        # same value already tried at this level
    ...
```

For permutations with duplicates the condition is `nums[i] == nums[i-1] and not used[i-1]`:
"do not place this copy if the identical previous copy is still unplaced," which forces
equal values to be placed left to right.

### Target sums: subtract and prune

Pass `remaining` down. Stop when it hits 0 (record) or goes negative (prune). With sorted
candidates you can `break` instead of `continue` when `nums[i] > remaining`, because every
later candidate is bigger too.

### Grid search: mark, recurse, unmark

Word Search: at cell `(r, c)` matching `word[k]`, mark the cell (write `"#"` into the board),
try the four neighbors for `word[k+1]`, then restore the letter. The board itself is the
`used` set, so no extra memory.

```python
def dfs(r, c, k):
    if k == len(word): return True
    if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[k]: return False
    saved, board[r][c] = board[r][c], "#"
    found = any(dfs(r + dr, c + dc, k + 1) for dr, dc in DIRS)
    board[r][c] = saved
    return found
```

### Constraint sets for placement problems

N-Queens: one queen per row, so the choice at row `r` is a column `c`. A placement is valid if
`c`, `r + c`, and `r - c` are all unused. Three sets replace scanning the board. Sudoku: one
set per row, column, and box; the three sets make the validity check O(1).

### Partition problems: choose where to cut

Palindrome Partitioning and Restore IP Addresses: at position `start`, try every `end` such
that `s[start:end]` is a valid piece, recurse from `end`. The goal is `start == len(s)`.

### When backtracking is the intended answer

Look at the constraints. `n ≤ 20`, `n ≤ 9`, `k ≤ 10`, string length ≤ 16: those are
exponential-size hints. If `n` is 10⁵, backtracking is wrong and you need DP, greedy, or a
data structure. State this reasoning; interviewers like hearing that the constraints told you
what to do.

## 4. Recognition cues

| You see | Think |
|---------|-------|
| "all subsets", "power set" | include/exclude, or template with `start` |
| "all combinations of size k", "choose k of n" | `start` index, stop when `len(path) == k` |
| "all permutations", "arrangements" | `used` array, every element a candidate each level |
| "sum to target", "unlimited reuse" | subtract target, recurse with `i` (reuse) or `i + 1` |
| "input has duplicates", "unique results" | sort, then `i > start and nums[i] == nums[i-1]: continue` |
| "generate all valid ..." (parentheses, IPs) | build one char/piece at a time, prune invalid prefixes |
| "does a word exist in the grid" | DFS with mark/unmark, board as the visited set |
| "place n things so none conflict" | one row per level, sets for the conflict lines |
| "fill the grid", "solve the puzzle" | find next empty cell, try each value, recurse, undo |
| "split the string into valid parts" | choose the end of the next piece, recurse from there |
| small n (≤ 20), "return all" | the whole chapter; complexity is the output size |

## 5. Pitfalls

- **Appending `path` instead of `path[:]`.** Every entry in `out` ends up the same (empty)
  list. Copy at the leaf.
- **Forgetting to pop.** The path grows forever and every later branch is polluted. Choose,
  explore, un-choose: always three lines.
- **`i + 1` vs `i`.** Recursing with `i + 1` means each element is used at most once; `i`
  allows reuse. Combination Sum I wants `i`, Combination Sum II wants `i + 1`.
- **`i > start` vs `i > 0`** in the duplicate skip. `i > 0` also skips legitimate branches at
  deeper levels; the skip must be relative to the current level's `start`.
- **Not sorting before the duplicate skip.** The skip relies on equal values being adjacent.
- **Word Search without unmarking** breaks later searches that need that cell. And marking
  with a letter that could appear in the word is a bug; use `"#"`.
- **N-Queens checking the board** in O(n) per placement instead of O(1) with sets. It works but
  costs a factor of `n` and shows less insight.
- **Sudoku with `"."` counted as a digit.** Only add real digits to the row/col/box sets.
- **Recursion limit.** Depth here is at most `n` or the string length, so it is rarely an
  issue, but say so if asked.
- **Claiming polynomial time.** The output is exponential; the algorithm is too. Say
  "O(n · 2ⁿ)" or "O(n · n!)" without flinching, and note that pruning cuts the constant.

## 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|----------|-----------|----------|----------|
| 1 | `subsets` | Medium | Amazon, Google | The anchor. Write all three ways; keep way 3. |
| 2 | `subsets_with_dup` | Medium | Amazon | Sort, then skip `nums[i] == nums[i-1]` when `i > start`. |
| 3 | `permutations` | Medium | Amazon, Google | `used` array. Goal: `len(path) == n`. |
| 4 | `permutations_unique` | Medium | Amazon, Google | Sort. Skip if `nums[i] == nums[i-1] and not used[i-1]`. |
| 5 | `combinations` | Medium | Google | `start` index, stop at `len(path) == k`. Prune when too few numbers remain. |
| 6 | `combination_sum` | Medium | Amazon, Google | Pass `remaining`. Recurse with `i`, not `i + 1`, to allow reuse. |
| 7 | `combination_sum_ii` | Medium | Amazon | Sort. Recurse with `i + 1`. Duplicate skip at each level. `break` when candidate > remaining. |
| 8 | `letter_combinations` | Medium | Amazon, Google | One digit per level; choices are that digit's letters. Empty input → `[]`. |
| 9 | `generate_parentheses` | Medium | Amazon, Google | Add `(` if `open < n`; add `)` if `close < open`. |
| 10 | `word_search` | Medium | Amazon, Google | DFS from every cell equal to `word[0]`. Mark `"#"`, recurse, restore. |
| 11 | `palindrome_partition` | Medium | Amazon, Google | At `start`, try every `end` where `s[start:end]` is a palindrome. |
| 12 | `n_queens` | Hard | Amazon, Google | Row by row. Sets for `col`, `r + c`, `r - c`. Build the board strings at the leaf. |
| 13 | `restore_ip_addresses` | Medium | Amazon | Four pieces of 1–3 chars, value ≤ 255, no leading zero unless the piece is `"0"`. |
| 14 | `sudoku_solver` | Hard | Google, Amazon | Find the first `"."`; try `1`–`9` not in that row/col/box; recurse; undo. Return `True` up the stack on success. |

Solve 1–9 in order; they are the template with different blanks. 10–14 are the stretch set
and the ones most likely to be a Google "hard" round.
