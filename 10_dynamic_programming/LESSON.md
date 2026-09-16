# 10 · Dynamic Programming

> Dynamic programming is not a new kind of thinking. It is recursion plus a notebook. You write
> the honest brute-force recursion, notice you keep answering the same question, and start
> writing the answers down. Everything else in this chapter is bookkeeping.

**Interview frequency:** high at Google, medium at Amazon. Google asks DP as a second problem
after a warm-up, usually a 1-D or two-sequence variant. Amazon leans on the easier families
(climbing stairs, house robber, coin change, LCS). Both love to hear you say "memoize" before
you say "table."

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

Dynamic programming is ordinary recursion where you write down each answer the first time you
find it, so you never work it out twice.

### Start with something you already do

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

### Now the same thing with numbers

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

### The words people use

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

### Why the fast way is fast

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

### Try it in your head

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

### Common confusions, cleared

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

### What to do next

Open Part 2 below and read Part 2 §1, especially the four-question table, then Part 2 §2, Climbing Stairs in
five stages. Stages 1 to 3 are the tree with sticky notes; stage 4 is the row of boxes. Then
open `exercises.py` and do `climbing_stairs` and `house_robber` with a timer. Before writing
either, say out loud what dp[i] means. When they pass, read the knapsack templates in Part 2 §3 and
try `coin_change`.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** When your phone autocorrects "teh" to "the," it computes
the edit distance between what you typed and each candidate word. When `git diff` or
`git merge` shows what changed, it runs longest common subsequence over the two files. Word
processors justify text by choosing line breaks that minimize raggedness. Bioinformatics
aligns DNA sequences with the same two-string table as edit distance. Amazon's inventory and
pricing systems optimize over budgets and time steps the way Coin Change optimizes over
amounts, and route planning with a fuel budget is knapsack with a map on top.

**The analogy.** A notebook. You are asked a hard question, and to answer it you need the
answers to two slightly easier ones. Each needs two more, and soon you are asked the same
small question for the fifth time. So you start writing answers in a notebook and check it
before doing any work. That is memoization. The staircase is the notebook made visible: to
know the ways to reach step 5, you only need steps 4 and 3, already written down.

**How it works, in plain words.** Write the honest recursive brute force. It is exponential
because it re-solves the same subproblems. Ask one question: what identifies a subproblem?
For Climbing Stairs it is just `n`. For two strings it is a pair of indices. That identifier
is your state, and the number of distinct states is your running time once you remember
answers. Add `@lru_cache` and you are done; that is dynamic programming. The bottom-up table
is the same recursion written as a loop from the base cases upward, and compressing it to
two variables is tidying. Neither is required to be correct.

**What learning this will feel like.** This is the chapter people fear most, and the fear
comes from one habit: jumping straight to the table. A table is a compressed recursion. If
you have not seen the recursion, the table is a picture you cannot read. So write the
recursion, draw the tree for a small input, and circle the repeated nodes. The aha is that
memoized recursion *is* dynamic programming; everything after stage 3 is optional. The second
aha is that the sentence "dp[i] means ..." is 80% of the work. Finish that sentence and the
transition usually writes itself. The bug you will write once is the wrong loop direction in
knapsack, so each coin gets used many times instead of once.

**You will know you have it when** "number of ways" or "minimum cost" makes you reach for a
recursive function with a cache before you think about a table, and you can say what `dp[i]`
means in one sentence.

### 1. The core idea

Every DP problem is a recursion with **overlapping subproblems**: the same smaller question
gets asked many times. Plain recursion answers it every time. DP answers it once and remembers.

The five stages, in the order you should do them in an interview:

```
1. Brute-force recursion      "the answer for n is built from answers for n-1 and n-2"
2. Spot the repeats            draw the tree; the same node appears many times
3. Memoize                     @lru_cache or a dict keyed by the state -> O(#states)
4. Bottom-up table (optional)  fill dp[] from base cases toward the answer, no recursion
5. Compress space (optional)   if dp[i] depends only on the last k rows, keep k variables
```

Stages 1 to 3 get full marks at almost every company. Stages 4 and 5 are the follow-up
questions. Here is the whole idea on Climbing Stairs, `n = 5`:

```
brute-force tree for ways(5)                       memoized
                 ways(5)                           ways(5)
              /          \                          /     \
        ways(4)          ways(3)*               ways(4)   [3: cached]
       /      \          /     \                /     \
   ways(3)*  ways(2)#  ways(2)# ways(1)     ways(3)  [2: cached]
   /    \    ...        ...                 /    \
ways(2)# ways(1)                        ways(2) ways(1)
 ...                                     /   \
                                     ways(1) ways(0)
* ways(3) computed 2 times    # ways(2) computed 3 times
15 calls                                           9 calls; n=40 -> 2.6 billion vs 81
```

Every `*` and `#` subtree in the left tree is identical work. The right tree does each once.
The number of distinct states is `n + 1`, so the memoized version is O(n).

**The four questions you answer for every DP.** Write them down before you code.

| Question | Climbing Stairs answer |
|----------|------------------------|
| **State.** What does `dp[i]` mean, in one sentence? | `dp[i]` = number of ways to reach step `i`. |
| **Transition.** How is `dp[i]` built from smaller states? | `dp[i] = dp[i-1] + dp[i-2]` (last move was 1 or 2 steps). |
| **Base case.** Where does the recursion stop? | `dp[0] = 1` (one way to stand still), `dp[1] = 1`. |
| **Answer.** Which cell holds the result? | `dp[n]`. |

If you cannot say the state in one sentence, you do not have a DP yet. Keep looking.

### 2. Anchor problem: Climbing Stairs, fully worked

**Problem.** You climb a staircase with `n` steps. Each move goes up 1 or 2 steps. How many
distinct sequences of moves reach the top?

**Understand.** Order matters (`1,2` and `2,1` are different). `n >= 1`. Answer for `n = 1` is 1,
for `n = 2` is 2 (`1+1`, `2`). Can `n` be large? Yes, so exponential is out.

**Examples.** `2 → 2`. `3 → 3` (`1+1+1`, `1+2`, `2+1`). `5 → 8`.

**Brute force (stage 1).** The last move was either 1 step from `n-1` or 2 steps from `n-2`.
So `ways(n) = ways(n-1) + ways(n-2)`. Base: `ways(0) = 1`, `ways(1) = 1`.

```python
def ways(n):
    if n <= 1:
        return 1
    return ways(n - 1) + ways(n - 2)
```

O(2ⁿ) time. Say it, then say why: "the tree above re-solves `ways(3)` twice and `ways(2)` three
times, and it gets exponentially worse."

**Insight (stage 2).** The only thing that identifies a subproblem is `n`. There are `n + 1`
possible values. If I never solve the same `n` twice, I do O(n) work.

**Code (stage 3, memoized).**

```python
from functools import lru_cache

def climbing_stairs(n):
    @lru_cache(maxsize=None)
    def ways(i):
        if i <= 1:
            return 1
        return ways(i - 1) + ways(i - 2)
    return ways(n)
```

**Code (stage 4, bottom-up).** Same transition, filled from the base cases upward.

```python
def climbing_stairs(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

**Code (stage 5, compressed).** `dp[i]` only looks back two cells, so keep two variables.

```python
def climbing_stairs(n):
    a, b = 1, 1                     # ways(i-2), ways(i-1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

**Test trace** (compressed, `n = 5`): start `a=1, b=1`. i=2: `a=1, b=2`. i=3: `a=2, b=3`.
i=4: `a=3, b=5`. i=5: `a=5, b=8`. Return 8. ✓ That is Fibonacci shifted by one, which is
worth saying out loud because the interviewer will be waiting for it.

**Complexity.** O(n) time. Space: O(n) memoized or tabulated, O(1) compressed.

**What to say out loud.** "The last move is 1 or 2 steps, so ways(n) = ways(n-1) + ways(n-2).
Naively that is exponential because subproblems repeat. There are only n+1 distinct
subproblems, so memoizing makes it O(n). Bottom-up it is a loop, and since each cell depends
on the previous two I can keep two variables for O(1) space."

### 3. Patterns and templates in this chapter

#### The memoization template

Write this every time, then decide whether to convert it. Nested function so the cache is
per call, and `maxsize=None` so nothing gets evicted.

```python
from functools import lru_cache

def solve(inputs):
    @lru_cache(maxsize=None)
    def f(state):                  # state must be hashable: ints, tuples, strings
        if base_case(state):
            return base_value
        return combine(f(smaller_state) for smaller_state in choices(state))
    return f(start_state)
```

Python's recursion limit is 1000 by default. If a state can be 10⁴ deep, either convert to
bottom-up or say `sys.setrecursionlimit(10**6)` and mention it.

#### 1-D linear: "take or skip"

House Robber. `dp[i]` = best using houses `0..i`. Either skip house `i` or take it and add
the best up to `i-2`.

```python
def rob(nums):
    prev2 = prev1 = 0               # best up to i-2, best up to i-1
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
```

Circular variant: the first and last house cannot both be taken, so answer is
`max(rob(nums[1:]), rob(nums[:-1]))`.

#### 0/1 knapsack: "can I make this sum using each item at most once?"

Subset sum / Partition Equal Subset Sum. `dp[s]` = can I make sum `s`. Iterate items on the
outside; iterate sums **downward** on the inside so each item is used once.

```python
def can_make(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):   # downward: dp[s - x] is still "before x"
            dp[s] = dp[s] or dp[s - x]
    return dp[target]
```

#### Unbounded knapsack: "each item any number of times"

Coin Change. Same shape, but iterate sums **upward** so an item can be reused.

```python
def coin_change(coins, amount):                 # fewest coins
    INF = float("inf")
    dp = [0] + [INF] * amount                   # dp[a] = fewest coins making a
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != INF else -1

def coin_change_ii(coins, amount):              # number of combinations
    dp = [1] + [0] * amount                     # dp[a] = ways to make a
    for c in coins:                             # coins OUTSIDE: counts combinations
        for a in range(c, amount + 1):          # upward: reuse allowed
            dp[a] += dp[a - c]
    return dp[amount]
```

Coins outside, amounts inside counts each *set* of coins once (`1+2` and `2+1` are the same).
Swap the loops and you count *sequences* instead. Interviewers ask about this on purpose.

#### 2-D grid: "paths through a grid"

Unique Paths. `dp[r][c]` = ways to reach cell `(r, c)` = from above + from the left. One row
suffices because each row depends only on the row above.

```python
def unique_paths(m, n):
    row = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]        # row[c] is still "from above"; row[c-1] is updated "from left"
    return row[-1]
```

#### Two sequences: "align s and t"

LCS, Edit Distance. `dp[i][j]` = answer for prefixes `s[:i]` and `t[:j]`. Row 0 and column 0
are the base cases (one string empty). The transition asks: do the last characters match?

```python
def lcs(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

Edit distance is the same table with three options on mismatch: `1 + min(delete, insert,
replace)` = `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`.

#### Strings: "can I break the prefix?"

Word Break, Decode Ways. `dp[i]` = the prefix `s[:i]` is valid. Look back over every possible
last piece.

```python
def word_break(s, words):
    ws = set(words)
    dp = [True] + [False] * len(s)              # dp[i]: s[:i] can be segmented
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in ws:
                dp[i] = True
                break
    return dp[-1]
```

#### Palindromes: expand from the center, or fill a 2-D table

Longest Palindromic Substring. Each of the `2n - 1` centers (a letter, or a gap between two
letters) expands outward while the ends match. O(n²) time, O(1) space, and easier to write
correctly than the table.

```python
def expand(s, lo, hi):
    while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
        lo -= 1; hi += 1
    return lo + 1, hi                    # the palindrome is s[lo+1:hi]
```

#### Interval DP: "the last thing to happen"

Burst Balloons. The trick is to think about which balloon pops **last** in the range
`(l, r)`, because then its neighbors are fixed. `dp[l][r]` = best score for the open interval.
Fill by increasing interval length. O(n³).

#### LIS: O(n²) then O(n log n)

`dp[i]` = length of the longest increasing subsequence ending at `i`:
`dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])`. O(n²). Every interviewer will then
ask for `O(n log n)`:

```python
from bisect import bisect_left

def length_of_lis(nums):
    tails = []                          # tails[k] = smallest tail of an increasing subseq of length k+1
    for x in nums:
        k = bisect_left(tails, x)       # first tail >= x
        if k == len(tails):
            tails.append(x)             # x extends the longest subsequence
        else:
            tails[k] = x                # x is a better (smaller) tail for length k+1
    return len(tails)
```

`tails` is not the subsequence, only its length is meaningful. Say that before they ask.

#### State machines: "what mode am I in?"

Stock with Cooldown. When one variable is not enough, carry several: `hold` (best while
owning stock), `sold` (just sold), `rest` (no stock, free to buy). Each day, each state moves
to the next by one rule.

### 4. Recognition cues

| You see | Think |
|---------|-------|
| "number of ways", "minimum cost", "maximum value", "is it possible" | DP candidate; write the recursion first |
| "can pick each item once", "subset with sum" | 0/1 knapsack; sums downward |
| "unlimited coins / items", "fewest coins" | unbounded knapsack; sums upward |
| "combinations" vs "sequences / permutations" | items outside vs amounts outside |
| "two strings", "subsequence", "edit", "align" | 2-D table over prefixes `(i, j)` |
| "grid, move right or down" | `dp[r][c] = dp[r-1][c] + dp[r][c-1]` |
| "partition a string into words / digits" | `dp[i]` over prefixes, look back over last piece |
| "palindrome" | expand around centers, or `dp[i][j]` over substrings |
| "longest increasing subsequence" | O(n²) DP, then `bisect` on tails |
| "range, remove last / burst / merge" | interval DP, iterate by length |
| "buy / sell / cooldown / at most k transactions" | state machine, one variable per state |
| "adjacent cannot both be chosen" | house robber |

### 5. Pitfalls

- **Starting with the table.** Start with the recursion. The table is a transcription of it.
  Interviewers see through tables that were memorized without the recursion behind them.
- **Vague state.** "dp[i] is the answer so far" is not a definition. Say what `i` indexes and
  what the cell contains, in one sentence.
- **Wrong loop direction in knapsack.** Downward for 0/1, upward for unbounded. Trace one item
  to check.
- **Off-by-one in two-sequence tables.** `dp[i][j]` covers `s[:i]`, so the character compared
  is `s[i-1]`. Size the table `(m+1) × (n+1)`.
- **Forgetting the empty base case.** `dp[0] = 1` for "ways to make 0" and `dp[0] = True` for
  "empty prefix is valid." Missing it zeros the whole table.
- **Mutable or huge cache keys.** `lru_cache` needs hashable arguments; pass indices, not
  slices. Slicing inside the recursion also silently adds an O(n) factor.
- **Recursion depth.** Python defaults to 1000. Convert to bottom-up when the state can be
  deeper, or raise the limit and say so.
- **Product DP with negatives.** Max Product Subarray needs both the running max and the
  running min, because a negative flips them.
- **Circular house robber.** Two runs, not one. Also handle `len(nums) == 1` before slicing.

### 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|----------|-----------|----------|----------|
| 1 | `climbing_stairs` | Easy | Amazon, Google | The anchor. All five stages, then keep the two-variable one. |
| 2 | `min_cost_climbing_stairs` | Easy | Amazon | `dp[i]` = cheapest way to stand on step `i`. Answer is `min` of the last two. |
| 3 | `house_robber` | Medium | Amazon, Google | Take `x + prev2` or skip and keep `prev1`. |
| 4 | `house_robber_ii` | Medium | Amazon, Google | Circular: rob `nums[1:]` and `nums[:-1]`, take the max. |
| 5 | `longest_palindromic_substring` | Medium | Amazon, Google | Expand around each of the `2n-1` centers. |
| 6 | `count_palindromic_substrings` | Medium | Google | Same expansion; count every successful step outward. |
| 7 | `decode_ways` | Medium | Google, Amazon | `dp[i]` over prefixes. One digit if not '0'; two digits if `10..26`. |
| 8 | `coin_change` | Medium | Amazon, Google | Unbounded knapsack, `min`. Fill amounts upward. |
| 9 | `coin_change_ii` | Medium | Amazon, Google | Coins outside, amounts inside, `+=`. |
| 10 | `max_product_subarray` | Medium | Amazon, Google | Track running max and running min; a negative swaps them. |
| 11 | `word_break` | Medium | Amazon, Google | `dp[i]`: prefix of length `i` is breakable. Look back over all `j < i`. |
| 12 | `length_of_lis` | Medium | Google, Amazon | Write O(n²) first, then `bisect_left` on the tails array. |
| 13 | `can_partition` | Medium | Amazon, Google | Odd total is `False`. Then 0/1 subset sum for `total // 2`, sums downward. |
| 14 | `unique_paths` | Medium | Amazon, Google | `row[c] += row[c-1]`, once per row. |
| 15 | `longest_common_subsequence` | Medium | Google, Amazon | `(m+1) × (n+1)` table; match → diagonal + 1, else max of up and left. |
| 16 | `edit_distance` | Medium | Google, Amazon | Same table; row 0 and column 0 are `i` and `j`; mismatch → `1 + min` of three. |
| 17 | `max_profit_with_cooldown` | Medium | Google, Amazon | Three states: `hold`, `sold`, `rest`. Write the three transitions before coding. |
| 18 | `target_sum_ways` | Medium | Google | Plus-set `P` satisfies `2P = target + total`. Count subsets summing to `P`. |
| 19 | `interleaving_string` | Medium-Hard | Google | `dp[i][j]`: `s1[:i]` and `s2[:j]` interleave into `s3[:i+j]`. |
| 20 | `burst_balloons` | Hard | Google | Pad with 1s. `dp[l][r]` over open intervals, choose the balloon that pops last. |
| 21 | `regex_match` | Hard | Google, Amazon | `dp[i][j]` over prefixes. On `*`, either use zero of the preceding char or consume one from `s`. |

Solve 1–11 in order, then 12–18. 19–21 are the stretch set; do them when 1–18 pass cold.
