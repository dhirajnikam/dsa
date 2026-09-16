# 12 · Tries, Union-Find & Bits

> Three small tools, each with one job. A trie answers "what starts with this?" A union-find
> answers "are these two in the same group?" Bit tricks answer "can I do this in O(1) with no
> extra memory?" None of them is deep. All of them show up, and an interviewer can tell in ten
> seconds whether you have written one before.

**Interview frequency:** medium. Tries appear at Google (autocomplete, word search, prefix
counting) and at Amazon in search-related teams. Union-find appears whenever a graph problem
is really about connectivity (accounts merge, islands, provinces). Bit manipulation is a
short-problem favorite at both, often as a warm-up or a "do it without extra space" follow-up.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

A trie is a dictionary where words that start the same share the same pages; union-find tracks
friend groups by remembering one leader per group; and bits are a row of light switches you
can flip all at once.

### Start with something you already do

**Trie: the paper dictionary.** You want every word starting with "ca." You do not read the
whole book. You open to C, then to CA, and everything you want is sitting right there. Words
sharing a beginning share the same pages. A trie is that idea built as a tree, one branch per
letter, so "starts with ca" is a two-step walk from the root and everything below that spot is
your answer. A plain set can tell you whether "cat" is a word. It cannot tell you what starts
with "ca" without checking every entry.

**Union-find: the party.** Sixty people in little clusters, and each cluster has quietly agreed
on one leader. When two people from different clusters shake hands, their clusters merge, and
one leader steps down and points at the other. Now "are you two in the same group?" is cheap:
each of you names your leader, and if it is the same person, yes. After a few merges the chain
"my leader is Priya, whose leader is Sam, whose leader is..." gets long, so the first time you
trace it, you save the final leader's number in your phone. That is **path compression**. Next
time, one lookup.

**Bits: the light switches.** A row of switches, each on or off. The rightmost is worth 1, the
next 2, then 4, then 8, doubling every step left. The number the row represents is the sum of
the switches that are on: `0110` means 2 + 4 = 6. Every integer in your computer is already
such a row, and there are moves that act on the whole row at once: combine two rows switch by
switch, or slide every switch one place left. The machine does all 64 switches in one step.

### Now the same thing with numbers

**Trie.** Insert "cat" and "car."

```
root
 └ c
   └ a
     ├ t*        * = a word ends here
     └ r*
```

Insert "card": walk c, a, r, then hang a new `d*` under r. Search "ca": walk c, a, the node
exists but has no star, so `search` says no while `starts_with` says yes. That star is the
whole difference between the two questions, and forgetting it is the classic bug.

**Union-find.** Five people numbered 0 to 4, each their own leader: `parent = [0, 1, 2, 3, 4]`.
Handshake 0–1: leaders are 0 and 1, different, so point 1 at 0. Handshake 3–4: point 4 at 3.
Handshake 1–4: leader of 1 is 0, leader of 4 is 3, so point 3 at 0. Now
`parent = [0, 0, 2, 0, 3]`. Pause and predict: are 1 and 4 in the same group, and how many
groups are there?

<details><summary>Answer</summary>
Yes. Leader of 1 is 0. Leader of 4: 4 → 3 → 0. Same leader. Groups: started at 5, and three
handshakes each merged two different groups, so 5 − 3 = 2 groups: {0,1,3,4} and {2}. After path
compression, 4 points straight at 0.
</details>

**Bits.** Take `x = 0110` (6) and `x − 1 = 0101` (5). AND them: a switch stays on only where
both are on. `0110 & 0101 = 0100` (4). The lowest lit switch went off and nothing else changed.
Again: `0100 & 0011 = 0000`. Two rounds to reach zero, so 6 has two lit switches. That is how
you count 1-bits.

### The words people use

- **Trie (say "try").** A tree where each edge is one letter and each root-to-node path spells
  a prefix.
- **Node / child.** A spot in the tree, and the spots one letter below it, stored as a small
  dictionary from letter to child.
- **Prefix.** The beginning of a word. "ca" is a prefix of "cat."
- **End-of-word flag (`is_end`).** The star. A real word stops here, not just a prefix.
- **`search` vs `starts_with`.** Same walk. `search` also demands the star at the bottom.
- **DFS with pruning.** Exploring a grid and the trie together, deleting trie branches once
  they are empty so you never re-enter them.
- **Union-find / Disjoint Set Union (DSU).** The party. Tracks which items share a group.
- **Representative / root / leader.** The one member the whole group is identified by.
- **`find(x)`.** Follow the chain of parents to the leader.
- **`union(a, b)`.** Merge the groups of a and b. Returns whether anything actually merged.
- **Path compression.** Saving the leader directly so later lookups are one step.
- **Union by rank.** Hang the shorter tree under the taller one, so chains stay short.
- **Amortized O(α(n)).** "Effectively constant." α is at most 4 for any real input.
- **Connected components.** Groups, in graph language.
- **Bit.** One switch, 0 or 1. A **set bit** is one that is on; **Hamming weight** is how many.
- **AND (`&`).** On only where both rows are on. Tests a switch.
- **OR (`|`).** On where either row is on. Turns a switch on.
- **XOR (`^`).** On where the two rows differ. A row XOR itself is all zeros.
- **NOT (`~`).** Flip every switch. In Python, `~x` equals `-x - 1`.
- **Shift (`<<`, `>>`).** Slide every switch left (doubling) or right (halving).
- **Mask.** A row you AND with to keep only certain switches. `0xFFFFFFFF` keeps 32.
- **Two's complement.** How negatives are stored in 32 bits. Matters only when a problem says
  "32-bit."

### Why the fast way is fast

Three tools, three comparisons. `n` is the number of words, people, or numbers.

| n | "starts with": scan a set vs walk a trie | "same group?": re-walk links vs union-find | "the loner": check pairs vs XOR |
|---|---|---|---|
| 10 | 10 vs 2 | up to 10 vs about 1 | 100 vs 10 |
| 1,000 | 1,000 vs 2 | up to 1,000 vs about 1 | 1,000,000 vs 1,000 |
| 100,000 | 100,000 vs 2 | up to 100,000 vs about 1 | 10,000,000,000 vs 100,000 |

The trie walk costs the length of the prefix, not the number of words. Union-find costs "about
1" after compression, however many people. XOR uses zero extra memory. The trade-offs: a trie
eats memory when words share little; union-find cannot *un*-merge groups; bit tricks only work
when the problem really is about pairs, powers of two, or fixed-width integers.

### Try it in your head

1. The trie holds "app" and "apple." What do `search("app")`, `search("appl")`, and
   `starts_with("appl")` return?

<details><summary>Answer</summary>
True (star at the second p). False (node exists, no star). True (node exists).
</details>

2. Numbers `[4, 7, 4, 9, 7]`. XOR them all. What comes out, and why?

<details><summary>Answer</summary>
9. The two 4s cancel to 0, the two 7s cancel to 0, and 0 XOR 9 is 9. Order does not matter,
so the pairs vanish wherever they sit.
</details>

3. `x = 1000` (8). Is `x & (x − 1)` zero? What does that tell you?

<details><summary>Answer</summary>
Yes. 1000 & 0111 = 0000. Only one switch was lit, so 8 is a power of two. Check `x > 0` first,
because 0 also passes and is not a power of two.
</details>

### Common confusions, cleared

- **"Isn't a trie just a set of strings?"** A set answers "is this exact word here?" in one
  step but "what starts with this?" only by reading everything. A trie answers both by walking
  a few letters.
- **"Why not just set `parent[a] = b` to connect them?"** That links two *people*, not two
  *groups*. If a already had a leader, a now has two. Always find both leaders first, then
  point one leader at the other.
- **"XOR feels like magic. Why does it cancel?"** XOR asks "are these switches different?" A
  row compared with an identical row differs nowhere, so every switch reads 0. Order does not
  matter, so any pair anywhere in a list cancels.
- **"Why does `x & (x − 1)` kill exactly the lowest 1?"** Subtracting 1 flips the lowest lit
  switch off and every switch to its right on. The two rows agree above that switch and disagree
  at and below it, so AND keeps the top and darkens the rest.

### What to do next

Scroll down to Part 2 and read §2, the `Trie` walkthrough, then draw the c-a-t / c-a-r picture
yourself with "card" added. Then read the `UnionFind` class in Part 2 §3 and trace the five-person
party on paper. Then do `Trie` and `single_number` in `exercises.py`: the first is the anchor,
the second is the XOR trick in one line. Follow with `UnionFind` and `count_bits_in_int`. Save
`find_words` and `num_islands_ii` for a later sitting.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** Type "how to" into Google and the suggestions that
appear before you finish are a trie walk: every keystroke moves one node deeper, and that
node's children are the completions. Amazon's search-as-you-type and the routing table in
every internet router are the same structure. Union-find is how a network monitor knows
whether two machines are still connected as links fail, how Amazon merges duplicate accounts
that share an email, and the engine inside Kruskal's minimum spanning tree. Bits are the
permission flags on every file, the feature flags in every large codebase, and the
compression in every image you load.

**The analogy.** A trie is a paper dictionary where words sharing a prefix share pages:
"app," "apple," and "apt" start on the same page, and turning to "ap" reaches all of them at
once. Union-find is friend groups at a party. When two people shake hands their groups merge,
and each group remembers one representative, so "same group?" is answered by asking each
person who their representative is. Bits are a row of light switches: each is on or off, and
an integer is the pattern of the whole row read at a glance.

**How it works, in plain words.** A trie node is a dictionary of children plus a flag saying
"a word ends here." Insert walks down, creating nodes as needed; `search` and `starts_with` do
the same walk and differ only in whether they demand the flag at the bottom. Union-find keeps
an array where each item points to a parent; follow the pointers to the representative, and
merging two groups is one pointer assignment. Path compression points every node you touch
straight at the root, so later lookups are nearly instant. Bit operations act on all the
switches at once: AND to test, OR to set, XOR to flip.

**What learning this will feel like.** This chapter looks like three unrelated topics stapled
together, and the bit tricks feel like party tricks. Both feelings are accurate and neither
matters. The aha is realizing that each of the three is one short template you memorize once:
the `Trie` class in section 2, the `UnionFind` class in section 3, and the bit table in
section 1. The one idea to hold in your head is that XOR cancels pairs: XOR a list where
everything appears twice except one, and the pairs vanish, leaving the answer. The memorable
trap is `search` returning `True` for `"app"` after inserting only `"apple"`, because you
skipped the end-of-word flag. Everyone does it once.

**You will know you have it when** "starts with" makes you draw a tree, "are these connected"
makes you type `parent = list(range(n))`, and "appears exactly once" makes you reach for XOR.

### 1. The core idea

**Trie.** A hash set tells you whether a whole word exists. It cannot tell you whether any word
*starts with* `"app"` without scanning everything. A trie stores words character by character
along shared paths, so every prefix is a node and the question becomes a walk.

```
hash set: {"app", "apple", "apt", "bat"}      trie:
                                                     (root)
starts_with("ap")?                                   /    \
  scan all 4 words, compare prefixes                a      b
  O(total characters)                               |      |
                                                    p      a
                                                   / \     |
                                                  p*  t*   t*
                                                  |
                                                  l
                                                  |
                                                  e*           * = end of a word
starts_with("ap") = walk a -> p, node exists: yes. O(len(prefix)).
```

**Union-Find (Disjoint Set Union).** Maintain a partition of `n` items into groups. `find(x)`
returns the group's representative; `union(a, b)` merges two groups. With path compression
and union by rank both are effectively O(1) (amortized O(α(n)), where α grows so slowly it
is at most 4 for any input that fits in the universe). Use it when edges arrive one at a
time and you keep asking "connected yet?" or "how many groups?"

The trick to remember: **number of groups = n − (number of successful unions).** Make
`union` return `True` only when it actually merged two different groups, and the count falls
out for free.

**Bits.** Integers are arrays of booleans you can operate on 64 at a time. Eight operations
cover every interview question:

| Operation | Code | What it does | Example (8-bit) |
|-----------|------|--------------|-----------------|
| AND | `a & b` | 1 where both are 1 | `1100 & 1010 = 1000` |
| OR | `a \| b` | 1 where either is 1 | `1100 \| 1010 = 1110` |
| XOR | `a ^ b` | 1 where they differ; `x ^ x = 0`, `x ^ 0 = x` | `1100 ^ 1010 = 0110` |
| NOT | `~a` | flips every bit; `~a == -a - 1` in Python | `~0000 1100 = ...1111 0011` |
| Shift left | `a << k` | multiply by 2ᵏ | `0011 << 2 = 1100` |
| Shift right | `a >> k` | floor-divide by 2ᵏ | `1100 >> 2 = 0011` |
| Lowest bit | `x & 1` | is x odd? (`x >> 1` drops it) | `0101 & 1 = 1` |
| Clear lowest set bit | `x & (x - 1)` | removes the rightmost 1 | `0110 & 0101 = 0100` |
| Isolate lowest set bit | `x & -x` | keeps only the rightmost 1 | `0110 & 1010 = 0010` |

XOR cancels pairs: `a ^ b ^ a = b`. That single fact solves Single Number and Missing Number.
`x & (x - 1) == 0` means x has at most one bit set, which is the power-of-two test.

**Python's caveat.** Python ints are arbitrary precision, so `~x` and left shifts never
overflow, and negative numbers have infinitely many leading 1s. For any problem that says
"32-bit," mask with `0xFFFFFFFF` after every operation and convert back to a signed value at
the end: `x if x <= 0x7FFFFFFF else ~(x ^ 0xFFFFFFFF)`.

### 2. Anchor problem: Implement Trie, fully worked

**Problem.** Build a class with `insert(word)`, `search(word)` (is this exact word present?),
and `starts_with(prefix)` (is any stored word prefixed by this?). Lowercase letters only.

**Understand.** `search("app")` after inserting only `"apple"` is `False`; `starts_with("app")`
is `True`. Inserting the same word twice is harmless. The empty prefix matches everything.

**Examples.** insert `"apple"`; search `"apple"` → True; search `"app"` → False; starts_with
`"app"` → True; insert `"app"`; search `"app"` → True.

**Brute force.** Keep a Python set. `insert` and `search` are O(1). `starts_with` scans every
word: O(total length). Fine if prefix queries are rare; the trie is for when they are not.

**Insight.** Store one node per prefix. Each node holds a dict of children keyed by the next
character, plus a flag "a word ends here." Then all three operations are the same walk down
the tree, differing only in what they check at the bottom.

**Code.**

```python
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())   # create the path as needed
        node.is_end = True

    def _walk(self, s):                          # node at the end of s, or None
        node = self.root
        for c in s:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._walk(prefix) is not None
```

**Test trace.** insert `"app"`: root → `a` (new) → `p` (new) → `p` (new), mark end. insert
`"apple"`: root → `a` (exists) → `p` → `p` (exists, already an end) → `l` (new) → `e` (new),
mark end. search `"app"`: walk a,p,p → node exists and `is_end` → True. search `"ap"`: walk
a,p → exists but not `is_end` → False. starts_with `"ap"` → node exists → True. starts_with
`"b"` → `root.children.get("b")` is None → False. ✓

**Complexity.** Every operation is O(L) where L is the length of the word or prefix. Space is
O(total characters) in the worst case, less when words share prefixes.

**What to say out loud.** "A set gives O(1) exact lookup but prefix queries would scan
everything. A trie stores one node per prefix, so insert, search, and prefix check are all a
walk of length L. The only difference between search and starts_with is whether I require
the end-of-word flag at the final node."

### 3. Patterns and templates in this chapter

#### Trie + DFS (Word Search II)

Searching the grid for each word separately is O(words × cells × 4^L). Instead, put all
words in one trie and walk the grid and the trie **together**: at each cell, only continue if
the current character is a child of the current trie node. One DFS from each cell finds every
word at once.

```python
def find_words(board, words):
    root = TrieNode()
    for w in words:                                   # build the trie
        node = root
        for c in w:
            node = node.children.setdefault(c, TrieNode())
        node.word = w                                 # store the word at its end node

    rows, cols, found = len(board), len(board[0]), []

    def dfs(r, c, parent):
        ch = board[r][c]
        node = parent.children.get(ch)
        if node is None:
            return
        if node.word:
            found.append(node.word)
            node.word = None                          # report each word once
        board[r][c] = "#"                             # mark visited
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, node)
        board[r][c] = ch                              # unmark
        if not node.children:                         # prune dead leaves
            del parent.children[ch]

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    return found
```

The pruning line is what makes this fast enough in practice: once a word is found and its
branch is empty, later DFS calls never enter it.

#### Trie with a wildcard (`WordDictionary`)

`search` with `'.'` means "any child." On a `'.'`, recurse into every child; on a letter,
follow one. Return `True` as soon as any branch succeeds.

```python
def _match(node, word, i):
    if i == len(word):
        return node.is_end
    c = word[i]
    if c == ".":
        return any(_match(child, word, i + 1) for child in node.children.values())
    child = node.children.get(c)
    return child is not None and _match(child, word, i + 1)
```

#### Union-Find, the class

Memorize this. Four lines matter: the two `find` lines (path compression), the rank swap, and
the `return True`.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.groups = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression: point at the root
        return self.parent[x]

    def union(self, a, b) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                                  # already connected
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra                               # union by rank: attach the shorter tree
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.groups -= 1
        return True

    def count(self):
        return self.groups
```

With union by rank the trees have height O(log n), so the recursive `find` never goes deep.
Without it, use the iterative form or you can hit Python's recursion limit on a long chain.

#### Union-find over non-integer items (Accounts Merge)

Map each item to an index first: `idx = {}` then `idx.setdefault(email, len(idx))`. Union the
indices, then group by `find(idx[item])` with a `defaultdict(list)`.

#### Union-find on a grid (Number of Islands II)

Cell `(r, c)` is index `r * cols + c`. When a cell becomes land, `count += 1`, then for each
land neighbor `count -= uf.union(cell, neighbor)`. Watch for a position added twice.

#### Bit templates

```python
def hamming_weight(n):                 # count set bits
    count = 0
    while n:
        n &= n - 1                     # clear lowest set bit
        count += 1
    return count

def counting_bits(n):                  # bits[i] for i in 0..n, O(n)
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)   # drop the lowest bit, add it back as 0 or 1
    return bits

def reverse_bits(n):                   # 32-bit
    out = 0
    for _ in range(32):
        out = (out << 1) | (n & 1)
        n >>= 1
    return out

def missing_number(nums):              # 0..n with one missing
    x = len(nums)                      # include index n, which has no partner
    for i, v in enumerate(nums):
        x ^= i ^ v                     # pairs of equal index/value cancel
    return x

def get_sum(a, b):                     # add without + or -, 32-bit two's complement
    MASK, MAX = 0xFFFFFFFF, 0x7FFFFFFF
    a, b = a & MASK, b & MASK
    while b:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK   # sum without carry, carry
    return a if a <= MAX else ~(a ^ MASK)              # back to a signed Python int
```

`a ^ b` is the sum ignoring carries; `(a & b) << 1` is the carries. Repeat until there are
none. The mask keeps Python from growing the carry forever on negative inputs.

#### Bitwise trie (Maximum XOR of Two Numbers)

Insert every number as a 31-bit path (most significant bit first). For each number, walk the
trie greedily preferring the **opposite** bit at every level; every time you get it, that bit
is 1 in the XOR. O(n × 31).

### 4. Recognition cues

| You see | Think |
|---------|-------|
| "prefix", "autocomplete", "starts with", "dictionary of words" | trie |
| "find all words in a grid / stream" | one trie for all words, DFS with pruning |
| "wildcard `.`" in a word lookup | trie, branch on every child at `.` |
| "longest common prefix" | trie walk while one child, or compare `min(strs)` and `max(strs)` |
| "connected components", "groups", "friends of friends", edges arriving over time | union-find |
| "merge accounts / emails / sets that share an element" | union-find over indices, group by root |
| "count islands as cells are added" | union-find on a grid, `count -= union(...)` |
| "every element appears twice except one" | XOR everything |
| "missing number in 0..n" | XOR indices and values, or sum formula |
| "count 1 bits", "Hamming weight" | `x & (x - 1)` loop |
| "bits for every number up to n" | `bits[i >> 1] + (i & 1)` |
| "without using + or -" | XOR for sum, AND shifted for carry, mask for 32-bit |
| "power of two" | `n > 0 and n & (n - 1) == 0` |
| "maximum XOR of a pair" | bitwise trie, prefer the opposite bit |

### 5. Pitfalls

- **Trie `search` without the end flag** returns `True` for prefixes. `search` checks `is_end`,
  `starts_with` does not. Say the difference before you write it.
- **Word Search II without pruning or de-duplication** is correct but slow, and returns a word
  once per path. Clear the word at its node when found.
- **Forgetting to unmark the cell** in grid DFS. Restore `board[r][c]` after the recursive
  calls.
- **Union-find without `find` on both sides.** `parent[a] = b` connects the *nodes*, not the
  groups. Always union roots.
- **Counting groups by scanning `parent`.** Wrong after path compression is skipped on some
  nodes. Count with the `n − successful unions` trick, or call `find` on every node.
- **Recursive `find` on a long chain** without union by rank can exceed the recursion limit.
  Keep the rank, or write `find` iteratively.
- **Negative numbers in Python bit code.** `~x` is `-x - 1`, and `x >> 1` on a negative never
  reaches 0. Mask with `0xFFFFFFFF` for 32-bit problems and convert back at the end.
- **`counting_bits` with `bin(i).count("1")`** is O(n log n). Fine as a first answer; the DP is
  the follow-up they want.
- **`x & (x - 1) == 0` for `x = 0`.** Zero passes the test but is not a power of two. Check
  `n > 0` first.

### 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|----------|-----------|----------|----------|
| 1 | `Trie` | Medium | Amazon, Google | The anchor. `_walk` once; `search` also needs `is_end`. |
| 2 | `WordDictionary` | Medium | Google, Amazon | Recursive match; on `'.'`, try every child. |
| 3 | `find_words` | Hard | Amazon, Google | One trie for all words; DFS grid and trie together; clear a found word; prune empty nodes. |
| 4 | `longest_common_prefix` | Easy | Google, Amazon | Compare `min(strs)` and `max(strs)` character by character. |
| 5 | `UnionFind` | Medium | Google, Amazon | Path compression in `find`; `union` returns `True` only on a real merge. |
| 6 | `num_provinces` | Medium | Amazon, Google | Union `i, j` for every 1 above the diagonal; answer is `count()`. |
| 7 | `accounts_merge` | Medium | Amazon, Google | Index each email; union the account indices; group emails by root. |
| 8 | `num_islands_ii` | Hard | Google | Grid index `r * cols + c`; `count += 1` per new land, `-= 1` per successful union. |
| 9 | `single_number` | Easy | Amazon, Google | XOR everything. |
| 10 | `count_bits_in_int` | Easy | Amazon, Google | `n &= n - 1` until zero. |
| 11 | `counting_bits` | Easy | Amazon, Google | `bits[i] = bits[i >> 1] + (i & 1)`. |
| 12 | `reverse_bits` | Easy | Amazon, Google | 32 iterations: shift out into shift in. |
| 13 | `missing_number` | Easy | Amazon, Google | XOR indices 0..n and all values. |
| 14 | `get_sum_no_plus` | Medium | Amazon, Google | XOR is sum-without-carry; `(a & b) << 1` is the carry; mask to 32 bits. |
| 15 | `power_of_two` | Easy | Amazon, Google | `n > 0 and n & (n - 1) == 0`. |
| 16 | `max_xor_of_two_numbers` | Medium | Google | Bitwise trie of 31-bit paths; walk preferring the opposite bit. |

Solve 1, 2, 4, 5, 6, 9–13, 15 in order. Then 7, 14. 3, 8, and 16 are the stretch set; do them when
the rest pass cold.
