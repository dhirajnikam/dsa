# Phase 05: Hashing

**Goal:** reach for a dict or set whenever a problem asks "have I seen this?" or "how many of each?".

## Key idea
A dict maps a key to a value. A set only remembers which keys exist.
Both answer "is this here?" in O(1), so one pass over the data replaces a nested loop.
Keys must be unchangeable: use a tuple or string, never a list.

## Cheat sheet
```python
from collections import Counter, defaultdict
seen = {}                              # "have I seen the partner?"
for i, x in enumerate(nums):
    if target - x in seen: return [seen[target - x], i]
    seen[x] = i                        # check first, then insert
counts = Counter(s)                    # how many of each; missing key reads as 0
Counter(s) == Counter(t)               # same letters, same amounts
groups = defaultdict(list)             # group by a shared key
groups["".join(sorted(w))].append(w)   # anagrams share a sorted key
prefix = defaultdict(int); prefix[0] = 1   # count subarrays with sum k
cur = ans = 0
for x in nums:
    cur += x; ans += prefix[cur - k]; prefix[cur] += 1
```

## When you see... use...
- "two numbers that add up to X" -> dict of seen values
- "count / most frequent / anagram" -> Counter
- "group items that are the same in some way" -> defaultdict(list) with a shared key
- "subarray with sum k" (negatives allowed) -> prefix sum + dict
- "O(1) insert, delete, and random pick" -> list + dict, swap with last to delete

## Common mistakes
- Reading `d[key]` on a defaultdict creates the key. Use `key in d` to just check.
- Using a list as a dict key. Convert to a tuple first.
- Two Sum: inserting before checking makes `[3, 3]` pair with itself.
- Forgetting `prefix[0] = 1`, which drops subarrays that start at index 0.

## Problems
- `01_two_sum.py` — dict of seen values, one pass
- `02_contains_duplicate.py` — set membership
- `03_valid_anagram.py` — compare two Counters
- `04_group_anagrams.py` — group by sorted-letters key
- `05_top_k_frequent.py` — Counter, then pick the biggest counts
- `06_longest_consecutive_sequence.py` — set, only count up from a chain start
- `07_subarray_sum_equals_k.py` — prefix sum + dict
- `08_isomorphic_strings.py` — two dicts, one per direction
- `09_insert_delete_getrandom_o1.py` — list + dict, swap with last
