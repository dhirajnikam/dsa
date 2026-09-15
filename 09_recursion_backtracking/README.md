# Phase 09: Recursion & Backtracking

**Goal:** generate every subset, permutation, or combination with one template, then prune.

## Key idea
Recursion is a function that calls itself on a smaller input, with a base case that stops it.
Backtracking builds an answer one choice at a time. Make a choice, recurse, then undo the choice.
Every problem here is the same loop with a different set of choices and a different "is this done?" check.

## Cheat sheet
```python
def backtrack(path, start):
    if is_solution(path):
        res.append(path[:])            # copy! path keeps changing after this
        return
    for i in range(start, len(nums)):  # the choices from here
        if not ok(nums[i]): continue   # prune early
        path.append(nums[i])           # choose
        backtrack(path, i + 1)         # explore (use i, not i + 1, if reuse is allowed)
        path.pop()                     # un-choose

# subsets: record path at every call, no is_solution check
# permutations: loop over all i, skip if used[i], set used[i] before and after
# grid search: mark board[r][c] = "#", recurse to 4 neighbours, restore the letter
```

## When you see... use...
- "return all subsets / combinations" -> start-index loop, recurse with i + 1
- "return all permutations" -> used array, recurse over every unused item
- "numbers can be reused" -> recurse with i instead of i + 1
- "input has duplicates" -> sort, skip `nums[i] == nums[i-1]` at the same depth
- "n is small (under about 15) and you must list every answer" -> backtracking

## Common mistakes
- Appending `path` without copying. You end up with many copies of the same list.
- Forgetting to undo the choice after the recursive call.
- Using `i + 1` when reuse is allowed, or `i` when it is not.
- Pruning with `continue` when a `break` would skip the rest of a sorted list.

## Problems
- `01_subsets.py` — record at every call
- `02_permutations.py` — used array
- `03_combinations.py` — stop at length k
- `04_combination_sum.py` — reuse allowed, sort and break when too big
- `05_letter_combinations_phone.py` — one digit per level
- `06_generate_parentheses.py` — only add ")" if more "(" are open
- `07_word_search.py` — grid search, mark and restore cells
- `08_palindrome_partitioning.py` — choose where to cut next
- `09_n_queens.py` — hard: sets for columns and both diagonals
