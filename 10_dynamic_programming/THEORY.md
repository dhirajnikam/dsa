# 10 · Dynamic Programming, explained from zero

Read this first if "dynamic programming" sounds like it needs a maths degree. It does not.
When the staircase below makes sense, move to `LESSON.md`, the dense reference. This file is
the conversation with a patient friend before you open the reference.

## In one sentence

Dynamic programming is ordinary recursion where you write down each answer the first time you
find it, so you never work it out twice.

## Start with something you already do

A staircase with 5 steps. Each move you climb 1 step or 2. How many different ways can you
reach the top?

Think about the *last* move. You either stepped up 1 from step 4 or up 2 from step 3. So the
ways to reach step 5 is the ways to reach step 4 plus the ways to reach step 3. To answer
"step 5," you ask two smaller versions of the same question. That is the whole idea.

Now the friend. Every few minutes a friend asks "how many ways to reach step 3?" You work it
out. Five minutes later they ask again. Eventually you write the answer on a sticky note and
slap it on the wall. Next time, you point at the note.

Memoization is sticky notes. That is the entire secret. A table is sticky notes arranged in
order, filled in left to right before anyone asks.

## Now the same thing with numbers

Ask for step 5 the naive way, where every question spawns two smaller ones until you hit
steps 0 and 1, which each have one way.

```
                    ways(5)
                  /         \
            ways(4)          ways(3)*
           /      \         /      \
      ways(3)*  ways(2)#  ways(2)#  ways(1)
      /     \    /    \    /    \
  ways(2)# ways(1) ...  ...
```

Circle the repeats. `ways(3)` is asked twice, `ways(2)` three times. Step 5 costs 15
questions. Step 40 costs over two billion, most of them repeats.

With sticky notes, each step is answered once. Same thing as a row of boxes, left to right:

| Step | 0 | 1 | 2 | 3 | 4 | 5 |
|------|---|---|---|---|---|---|
| Ways | 1 | 1 | 2 | 3 | 5 | 8 |

Each box is the sum of the two to its left. Six boxes, six additions. The tree with sticky
notes and the row of boxes are the *same* method. The row is just the notes in order. Both
are dynamic programming.

Pause and predict: what goes in box 6, and which two boxes did you use?

<details><summary>Answer</summary>
13, from boxes 5 and 4: 8 + 5. You never looked at boxes 0 to 3 again.
</details>

The one sentence that matters, for every DP problem you will ever meet: **"dp[i] means
___."** Here: "dp[i] means the number of ways to reach step i." If you cannot finish that
sentence in plain words, you do not have a solution yet. Once you can, ask four questions:

1. **What is the state?** What does one box represent? A step number.
2. **What is the base case?** Which boxes can you fill without looking at others? Steps 0 and 1.
3. **How does a box depend on smaller ones?** Box i is box i−1 plus box i−2.
4. **Where is the answer?** The last box.

**Two strings.** Now the boxes form a grid. Longest common subsequence of `ab` and `ba`: the
longest run of letters in both, in order, gaps allowed. Box (i, j) means "the LCS of the
first i letters of one string and the first j of the other."

```
        ""   b    a
   ""    0   0    0
   a     0   0    1
   b     0   1    1
```

Row 0 and column 0 are 0: an empty string shares nothing. If the two letters match, take the
box diagonally up-left and add 1. If not, take the larger of the box above and the box to the
left. Bottom-right says 1. Same four questions, just a 2-D state.

**The bag.** Knapsack is packing a bag with a weight limit. For each item: take it or leave
it. "dp[w] means: can I fill the bag to exactly weight w with the items seen so far." The
take-or-skip fork from chapter 9, with the answers written down.

## The words people use

- **Dynamic programming (DP).** Recursion plus a notebook. Nothing more.
- **Subproblem.** A smaller version of the same question. "Ways to reach step 3" is a
  subproblem of "ways to reach step 5."
- **Overlapping subproblems.** The same small question appears many times in the tree. The
  signal that DP will help.
- **State.** What identifies one subproblem: a step number, a pair of indices, a remaining
  budget. The label on a sticky note.
- **dp[i], dp[i][j].** The box for state i, or (i, j). Its value is that subproblem's answer.
- **Transition.** The rule for filling a box from smaller boxes.
- **Base case.** The boxes you fill by hand, with no rule.
- **Memoization.** Sticky notes. Cache each answer the first time recursion computes it.
- **`@lru_cache`.** Python's built-in sticky notes. One line above a function makes it
  remember its answers.
- **Top-down.** Start at the big question and recurse downward, memoizing. The tree picture.
- **Bottom-up / tabulation.** Fill boxes from the base cases toward the answer with a loop.
  The row picture.
- **Space compression.** If each box only looks at the two before it, keep two variables
  instead of the whole row.
- **Take or skip.** The fork in House Robber and knapsack: use this item, or do not.
- **0/1 knapsack.** Each item at most once. Fill sums from high to low.
- **Unbounded knapsack.** Each item any number of times. Coin change. Fill sums low to high.
- **Subsequence.** Letters picked from a string in order, gaps allowed. `ac` is a subsequence
  of `abc`.
- **Prefix.** The first i characters of a string. Two-string tables are indexed by prefixes.
- **Edit distance.** Fewest inserts, deletes, or replacements to turn one string into another.
  The LCS grid with three options on a mismatch.
- **Interval DP.** The state is a range (l, r). You decide what happens *last* inside it.
- **State machine.** Several boxes per position, one per "mode," such as holding stock or
  not. Each mode has its own transition.
- **LIS.** Longest increasing subsequence. An n² table first, then sped up with binary search.

## Why the fast way is fast

The naive tree roughly doubles with every extra step. The row of boxes adds one box.

| Steps (n) | Naive recursion, about | Sticky notes or boxes |
|-----------|------------------------|-----------------------|
| 10 | 177 calls | 11 boxes |
| 30 | 2,700,000 calls | 31 boxes |
| 1,000 | never finishes | 1,001 boxes |
| 100,000 | never finishes | 100,001 boxes |

At a hundred million steps a second, naive n = 50 takes minutes. Boxes for n = 100,000 take a
millisecond.

The trade-off is memory: one answer per state. Two strings of length 1,000 means a million
boxes, fine. Two strings of 100,000 means ten billion, not fine, and you need a smarter state
or space compression. Spend memory to save time, and know how much you spent.

## Try it in your head

1. Steps cost money, `[10, 15, 20]`, and you may start on step 0 or 1. You pay when you stand
   on a step. Finish "dp[i] means ___."

<details><summary>Answer</summary>
"dp[i] means the cheapest total to be standing on step i." dp[0] = 10, dp[1] = 15, dp[2] = 20
+ min(10, 15) = 30. The top is past the last step, so the answer is min(dp[1], dp[2]) = 15.
</details>

2. Houses with cash `[2, 7, 9, 3]`, no robbing two neighbours. At the 9, what two options are
   you choosing between?

<details><summary>Answer</summary>
Skip it and keep the best from the first two houses, 7. Or take it plus the best from two
houses back, 9 + 2 = 11. Take wins. Then the last house: max(11, 3 + 7) = 11.
</details>

3. Coins `[1, 2]`, amount 3, count the ways. Coins on the outer loop, amounts inside. Are
   `1+2` and `2+1` one way or two?

<details><summary>Answer</summary>
One. With coins outside, you settle "how many 1s" before ever considering 2s, so each *set*
of coins is counted once. Ways: `1+1+1` and `1+2`. Answer 2. Swap the loops and you count
sequences: 3.
</details>

## Common confusions, cleared

- **"Do I have to build a table? The cached recursion already works."** No. Memoized
  recursion is dynamic programming, full stop. The table is the same thing as a loop.
  Write the recursion first; convert only if asked or if recursion depth is a worry.
- **"How do I even find the recursion?"** Ask what the *last* decision was. Last step was 1
  or 2. Last house was taken or skipped. Last letters matched or did not. The last decision
  splits the problem into smaller copies of itself.
- **"Why do I keep getting zeros everywhere?"** A missing base case. Ways to make amount 0 is
  1, not 0. If the seed boxes are wrong, every box that depends on them is wrong too.
- **"Knapsack: why does loop direction matter?"** Filling sums high to low reads boxes not yet
  touched by the current item, so it counts once. Low to high reads boxes already updated by
  this item, so it can be reused. Trace one coin over amounts 0 to 4 and you will see it.

## What to do next

Open `LESSON.md` and read §1, especially the four-question table, then §2, Climbing Stairs in
five stages. Stages 1 to 3 are the tree with sticky notes; stage 4 is the row of boxes. Then
open `exercises.py` and do `climbing_stairs` and `house_robber` with a timer. Before writing
either, say out loud what dp[i] means. When they pass, read the knapsack templates in §3 and
try `coin_change`.
