# 12 · Tries, Union-Find & Bits, explained from zero

Read this first if "trie" looks like a typo, "union-find" sounds like a labor dispute, and
"XOR" sounds like a villain. When the three stories below make sense, move to `LESSON.md`, the
dense reference. This is the friendly conversation before it.

## In one sentence

A trie is a dictionary where words that start the same share the same pages; union-find tracks
friend groups by remembering one leader per group; and bits are a row of light switches you
can flip all at once.

## Start with something you already do

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

## Now the same thing with numbers

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

## The words people use

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

## Why the fast way is fast

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

## Try it in your head

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

## Common confusions, cleared

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

## What to do next

Open `LESSON.md` and read §2, the `Trie` walkthrough, then draw the c-a-t / c-a-r picture
yourself with "card" added. Then read the `UnionFind` class in §3 and trace the five-person
party on paper. Then do `Trie` and `single_number` in `exercises.py`: the first is the anchor,
the second is the XOR trick in one line. Follow with `UnionFind` and `count_bits_in_int`. Save
`find_words` and `num_islands_ii` for a later sitting.
