# Phase 16: Tries & Advanced

**Goal:** know a few "design a data structure" templates well enough to type them from memory.

## Key idea
A trie is a tree of letters: each node is a dict of children plus an end marker. Walking a word takes O(length) no matter how many words are stored, so it is perfect for prefix queries.
A monotonic deque keeps only values that could still be the window max, so sliding-window max is O(n).

## Cheat sheet
```python
class Trie:
    def __init__(self): self.root = {}
    def insert(self, word):
        node = self.root
        for c in word: node = node.setdefault(c, {})
        node["$"] = True                       # end-of-word marker
    def search(self, word):
        node = self.root
        for c in word: node = node.get(c, {})  # missing letter -> empty dict
        return "$" in node
# sliding window max: deque of indices, values decreasing front to back
dq, out = deque(), []
for i, x in enumerate(nums):
    while dq and nums[dq[-1]] <= x: dq.pop()   # smaller ones can never win
    dq.append(i)
    if dq[0] <= i - k: dq.popleft()            # front left the window
    if i >= k - 1: out.append(nums[dq[0]])
```

## When you see... use...
- "many words, prefix / starts with / autocomplete" -> trie
- "wildcard `.` in search" -> trie, branch over all children at `.`
- "max of every window of size k" -> monotonic deque of indices
- "range sum with updates" -> Fenwick tree (prefix sums in O(log n), see the solution file)

## Common mistakes
- Trie `search` needs the end marker. `startsWith` does not.
- Deque must store indices, not values, or you cannot tell when the front expires.
- Fenwick tree is 1-indexed inside. Test the first element before anything else.

## Problems
- `01_implement_trie.py` — insert, search, startsWith
- `02_word_search_ii.py` — trie + grid DFS, prune by prefix
- `03_design_add_search_words.py` — trie with `.` wildcard
- `04_sliding_window_maximum.py` — monotonic deque of indices
- `05_range_sum_query_mutable.py` — Fenwick tree
- `06_maximum_xor_two_numbers.py` — bit trie, prefer opposite bit
- `07_counting_bits.py` — bits[i] = bits[i >> 1] + (i & 1)
- `08_lfu_cache.py` — freq buckets of OrderedDict, track min_freq
