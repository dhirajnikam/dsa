# Phase 06: Two Pointers & Sliding Window

**Goal:** replace nested loops over pairs or substrings with two indices that only move forward.

## Key idea
Two pointers are two indices into the same array. Each moves at most n times, so the whole thing is O(n).
Opposite pointers start at both ends and walk inward (sorted input or symmetry checks).
A sliding window is two same-direction pointers: the right one grows the window, the left one shrinks it.

## Cheat sheet
```python
l, r = 0, len(a) - 1                   # opposite pointers on sorted input
while l < r:
    s = a[l] + a[r]
    if s == target: return [l, r]
    if s < target: l += 1              # need bigger
    else: r -= 1                       # need smaller
w = 0                                  # read/write: keep some items in place
for x in a:
    if keep(x): a[w] = x; w += 1
l = best = 0                           # variable window: longest valid
for r, ch in enumerate(s):
    add(ch)                            # grow
    while not valid(): remove(s[l]); l += 1   # shrink until valid again
    best = max(best, r - l + 1)
```

## When you see... use...
- "sorted array, pair with sum" or "palindrome" -> opposite pointers
- "remove / compress in place, return new length" -> read/write pointers
- "subarray of size k" -> fixed window: add one, drop one
- "longest substring such that ..." -> grow, shrink while invalid, record
- "shortest subarray such that ..." -> grow, record and shrink while valid

## Common mistakes
- Window length is `r - l + 1`, not `r - l`.
- Shrinking with `if` instead of `while`. One removal is often not enough.
- Negatives in the array break the window trick. Use prefix sum + dict (Phase 05).

## Problems
- `01_valid_palindrome_two_pointers.py` — opposite pointers, skip non-letters
- `02_two_sum_sorted.py` — opposite pointers on sorted input
- `03_three_sum.py` — sort, fix one, two-pointer the rest
- `04_container_most_water.py` — move the shorter side inward
- `05_remove_duplicates_sorted.py` — read/write pointers
- `06_max_sum_subarray_size_k.py` — fixed-size window
- `07_longest_substring_no_repeat.py` — grow, shrink while a repeat exists
- `08_min_size_subarray_sum.py` — grow, shrink while sum still big enough
- `09_longest_repeating_char_replacement.py` — window valid if len - max_count <= k
- `10_minimum_window_substring.py` — hard: window with need/have counters
