# 12 · Tries, Union-Find & Bits

**In one sentence.** A trie is a dictionary where words that start the same share the same pages.
Union-find tracks friend groups by remembering one leader per group. Bits are a row of light
switches you can flip all at once.

**Why you care.** Type "how to" into Google and the suggestions are a trie walk. Union-find is how
Amazon merges duplicate accounts that share an email. Bits are the permission flags on every file.
Interview frequency is medium. Each one is a short template you memorize once.

## The idea, with a story

**Trie: the paper dictionary.** You want every word starting with "ca." You do not read the whole
book. You open to C, then to CA, and everything you want is right there. A trie is that idea built
as a tree, one branch per letter. "Starts with ca" is a two-step walk from the root. A plain set
knows whether "cat" is a word. It cannot list what starts with "ca" without reading everything.

**Union-find: the party.** Sixty people in little clusters. Each cluster has agreed on one leader.
When two people from different clusters shake hands, their clusters merge, and one leader steps
down and points at the other. Now "are you two in the same group?" is cheap: each of you names
your leader. After a few merges the chain "my leader is Priya, whose leader is Sam..." gets long.
So the first time you trace it, you save the final leader's name. That is **path compression**.
Next time, one lookup.

**Bits: the light switches.** A row of switches, each on or off. The rightmost is worth 1, the next
2, then 4, then 8, doubling every step left. The row's value is the sum of the switches that are
on: `0110` is 2 + 4 = 6. Every integer in your computer is such a row, and the machine can compare
two rows switch by switch in a single step.

## The same story with numbers

**Trie.** Insert "cat" and "car."

```
root
 └ c
   └ a
     ├ t*        * = a word ends here
     └ r*
```

Search "ca": walk c, a. The node exists but has no star. So `search` says no while `starts_with`
says yes. That star is the whole difference between the two questions.

**Union-find.** Five people numbered 0 to 4, each their own leader: `parent = [0, 1, 2, 3, 4]`.
Handshake 0–1: point 1 at 0. Handshake 3–4: point 4 at 3. Handshake 1–4: leader of 1 is 0, leader
of 4 is 3, so point 3 at 0. Now `parent = [0, 0, 2, 0, 3]`.

**Bits.** Take `x = 0110` (6) and `x − 1 = 0101` (5). AND them: a switch stays on only where both
are on. `0110 & 0101 = 0100`. The lowest lit switch went off and nothing else changed. Again:
`0100 & 0011 = 0000`. Two rounds to reach zero, so 6 has two lit switches.

Pause and predict: are 1 and 4 now in the same group? How many groups remain?

<details><summary>Answer</summary>
Yes. Leader of 1 is 0. Leader of 4 is 4 → 3 → 0. Same leader. Started at 5 groups, three real
merges, so 5 − 3 = 2 groups: {0,1,3,4} and {2}. After path compression, 4 points straight at 0.
</details>

## The anchor problem: Implement Trie

Build a class with `insert(word)`, `search(word)` for "is this exact word here?", and
`starts_with(prefix)` for "does any word begin with this?"

**Brute force.** A Python set. Insert and search are O(1), but `starts_with` scans every word.

**Insight.** Store one node per prefix. All three operations are the same walk down the tree. They
differ only in what they check at the bottom.

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())   # create the path as needed
        node.is_end = True                        # the star

    def _walk(self, s):                           # node at the end of s, or None
        node = self.root
        for c in s:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_end   # needs the star

    def starts_with(self, prefix):
        return self._walk(prefix) is not None     # star not needed
```

**Complexity.** Every operation is O(L), where L is the length of the word. Space is O(total
characters).

**What to say.** "A set gives O(1) exact lookup but prefix queries would scan everything. A trie
stores one node per prefix, so all three operations are a walk of length L. Search and starts_with
differ only in whether I require the end flag at the last node."

## Templates you memorize

**The trie node.** Already written for you in `exercises.py`.
```python
class TrieNode:
    def __init__(self):
        self.children = {}        # letter -> next TrieNode
        self.is_end = False       # a stored word finishes here
```

**Union-find with path compression.** Groups equals n minus the number of successful unions.
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))              # everyone is their own leader
        self.groups = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)       # find BOTH leaders first
        if ra == rb:
            return False                          # already together
        self.parent[rb] = ra                      # one leader points at the other
        self.groups -= 1
        return True
```

**The bit operations.** Six moves cover almost every interview question.

| Operation | Code | What it does | Example |
|-----------|------|--------------|---------|
| AND | `a & b` | 1 where both are 1 | `1100 & 1010 = 1000` |
| OR | `a \| b` | 1 where either is 1 | `1100 \| 1010 = 1110` |
| XOR | `a ^ b` | 1 where they differ | `1100 ^ 1010 = 0110` |
| Shift left | `a << k` | multiply by 2, k times | `0011 << 2 = 1100` |
| Shift right | `a >> k` | divide by 2, k times | `1100 >> 2 = 0011` |
| Lowest bit | `x & 1` | is x odd? | `0101 & 1 = 1` |

**XOR cancels pairs.** `a ^ b ^ a = b`. XOR a list where everything appears twice except one
value, and the pairs vanish. `[4, 7, 4, 9, 7]` XORs to 9.
```python
x = 0
for v in nums:
    x ^= v                    # each pair cancels to 0; x is the loner
```

**Count set bits with `x & (x - 1)`.** Each round turns off one 1. Power of two means
`n > 0 and n & (n - 1) == 0`.
```python
count = 0
while n:
    n &= n - 1                # clear the lowest set bit
    count += 1
```

## When you see X, think Y

| You see | Think |
|---------|-------|
| "prefix", "autocomplete", "starts with" | trie |
| "find all words in a grid" | one trie for all words, DFS the grid and trie together |
| "wildcard `.`" in a word lookup | trie, try every child at `.` |
| "connected components", "groups", "friends of friends" | union-find |
| "merge accounts that share an email" | union-find over indices, group by leader |
| "every element appears twice except one", "missing number" | XOR everything |
| "count 1 bits", "power of two" | `x & (x - 1)` |

## Words you will hear

- **Trie (say "try").** A tree where each edge is one letter and each path spells a prefix.
- **End-of-word flag (`is_end`).** The star. A real word stops here, not just a prefix.
- **Union-find / Disjoint Set Union (DSU).** Tracks which items share a group.
- **Representative / root / leader.** The one member the whole group is named by.
- **Path compression.** Saving the leader directly so later lookups are one step.
- **Set bit / Hamming weight.** A switch that is on, and how many are on.
- **Mask.** A row you AND with to keep only some switches. `0xFFFFFFFF` keeps 32.

## Mistakes everyone makes once

- **Trie `search` without the end flag** says True for "app" after inserting only "apple".
- **Union-find with `parent[a] = b`** links two people, not two groups. Find both leaders first.
- **`x & (x - 1) == 0` for `x = 0`.** Zero passes but is not a power of two. Check `n > 0` first.
- **Negative numbers in Python bit code.** Python ints never overflow. Mask with `0xFFFFFFFF`
  when the problem says 32-bit.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO. `TrieNode` is provided; use it in 1 to 3.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `Trie` | Medium | The anchor. One `_walk`. `search` also needs `is_end`. |
| 2 | `WordDictionary` | Medium | Recursive match. On `.`, try every child. |
| 3 | `find_words` | Hard | One trie for all words. DFS the grid and trie together. |
| 4 | `longest_common_prefix` | Easy | Compare `min(strs)` and `max(strs)` letter by letter. |
| 5 | `UnionFind` | Medium | Path compression in `find`. `union` returns True only on a real merge. |
| 6 | `num_provinces` | Medium | Union `i, j` for every 1 above the diagonal. Answer is `count()`. |
| 7 | `accounts_merge` | Medium | Index each email. Union account indices. Group emails by leader. |
| 8 | `num_islands_ii` | Hard | Cell index is `r * cols + c`. Add 1 per new land, subtract 1 per merge. |
| 9 | `single_number` | Easy | XOR everything. |
| 10 | `count_bits_in_int` | Easy | `n &= n - 1` until zero. |
| 11 | `counting_bits` | Easy | `bits[i] = bits[i >> 1] + (i & 1)`. |
| 12 | `reverse_bits` | Easy | 32 rounds: shift the lowest bit out of `n` into the answer. |
| 13 | `missing_number` | Easy | XOR all indices 0..n and all values. |
| 14 | `get_sum_no_plus` | Medium | XOR for the sum, `(a & b) << 1` for the carry, mask to 32 bits. |
| 15 | `power_of_two` | Easy | `n > 0 and n & (n - 1) == 0`. |
| 16 | `max_xor_of_two_numbers` | Medium | Trie of 31-bit paths. At each level prefer the opposite bit. |

Start with 1 and 9 today, then 5 and 10. Do 2, 4, 6, 11 to 13, and 15 over the week. The rest are
for when those pass cold.
