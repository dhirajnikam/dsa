# 00 · Foundations

> "If you can't solve a problem, then there is an easier problem you can solve: find it." — George Pólya

This chapter gives you three things you will use in every single interview: fluent Python,
an honest sense of Big-O, and a protocol for attacking any problem. None of it is glamorous.
All of it is graded.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

Big-O is a way of saying "how much slower does this get when the input gets bigger," and
recursion is "solve a big problem by solving a slightly smaller copy of it."

### Start with something you already do

**Big-O.** You are looking for a friend's name in a phone book.

- If the book is sorted, you open it in the middle, see you are too far, open the middle of
  the first half, and so on. A book with 1,000 pages takes about 10 opens. A book with
  1,000,000 pages takes about 20. Doubling the book adds *one* open. That is O(log n).
- If someone shuffled the pages, you must flip through one by one. 1,000 pages, up to 1,000
  flips. Doubling the book doubles the flips. That is O(n).
- If you have to compare every person in the book with every other person (say, to find two
  with the same birthday the slow way), 1,000 people means about 1,000,000 comparisons.
  Doubling the book *quadruples* the work. That is O(n²).

Big-O does not care whether a flip takes one second or one millisecond. It only cares about
the *shape* of the growth: flat, logarithmic, linear, quadratic. That shape decides whether
your code finishes in a blink or never.

**Recursion.** You are the CEO and want to know how many people work in the company. You do
not count. You ask each of your two VPs: "how many people report to you, including you?"
Each VP asks their managers the same question. Each manager asks their leads. At the bottom,
an employee with no reports answers "1." Answers flow back up, each person adding 1 for
themself. You add the two VP numbers plus one and you are done. You never counted anyone
yourself. You trusted the smaller version of the same question.

### Now the same thing with numbers

**Counting steps.** How many times does `hello` print?

```python
for i in range(4):          # i = 0, 1, 2, 3
    for j in range(4):      # j = 0, 1, 2, 3
        print("hello")
```

The outer loop runs 4 times; each time, the inner loop runs 4 times. 4 × 4 = 16. With
`range(n)` in both, it is n × n = n². Pause and predict: what if the inner loop were
`range(i)` instead of `range(4)`?

<details><summary>Answer</summary>
0 + 1 + 2 + 3 = 6 prints. In general, n(n−1)/2, which still grows like n². Half of a square
is still a square shape. Big-O drops the ½: O(n²).
</details>

**Recursion.** Add up a list by trusting a smaller list.

```python
def total(nums):
    if not nums:                    # empty list: the answer is 0. This is the base case.
        return 0
    return nums[0] + total(nums[1:])   # first item + (trust this to sum the rest)
```

Trace `total([5, 2, 9])`:

```
total([5, 2, 9]) = 5 + total([2, 9])
                       total([2, 9]) = 2 + total([9])
                                           total([9]) = 9 + total([])
                                                            total([]) = 0
                                           total([9]) = 9 + 0 = 9
                       total([2, 9]) = 2 + 9 = 11
total([5, 2, 9]) = 5 + 11 = 16
```

Notice you go *down* to the base case, then answers come back *up*. That staircase picture is
every recursive function you will ever write.

### The words people use

- **n.** The size of the input. Ten numbers, n = 10. A million, n = 1,000,000.
- **O(1), "constant."** Same work no matter how big n is. Opening box 7 in an array.
- **O(log n), "logarithmic."** Each step cuts the problem in half. Phone book, sorted.
- **O(n), "linear."** Touch every item once. One pass through a list.
- **O(n log n).** Sorting. A little worse than one pass, much better than a square.
- **O(n²), "quadratic."** Every item against every other item. Two nested loops.
- **O(2ⁿ), "exponential."** Doubles with every extra item. Trying every subset. Fine for
  n ≤ 20, hopeless past that.
- **Time complexity.** Big-O of how long it runs.
- **Space complexity.** Big-O of how much *extra* memory you use. A notepad of n things is O(n).
- **Base case.** The smallest input a recursive function answers directly, with no further calls.
  An empty list. A tree with no nodes. n = 0.
- **Recursive case.** The line where the function calls itself on something smaller.
- **Call stack.** The pile of unfinished function calls waiting for their answers. In the trace
  above, it was four deep. Python gives up around 1,000 deep unless you raise the limit.
- **Memoization.** Writing down the answer to each recursive call so you never compute it twice.
  A fancy word for a notepad. It is the seed of Chapter 10.
- **Constraints.** The line in the problem that says `n ≤ 100,000`. It tells you which Big-O
  will pass. Read it first, always.

### Why this matters more than it looks

A computer does roughly 100,000,000 simple steps per second. Now read a constraint.

| Constraint says | O(n²) steps | O(n log n) steps | Verdict |
|-----------------|-------------|------------------|---------|
| n ≤ 1,000 | 1,000,000 | 10,000 | either is fine |
| n ≤ 100,000 | 10,000,000,000 | 1,700,000 | O(n²) takes 100 seconds; you need better |
| n ≤ 20 | 400 | 86 | anything works, even trying all 2²⁰ ≈ 1,000,000 subsets |

So `n ≤ 100,000` means "do not write two nested loops" and `n ≤ 20` means "the brute force
is the answer, they want you to enumerate." Reading that line saves you ten minutes of
wandering in the interview.

### Try it in your head

1. A loop that halves `n` each time until it hits 1. `n = 64`. How many times does it run?
   What is the Big-O?

<details><summary>Answer</summary>
64 → 32 → 16 → 8 → 4 → 2 → 1: six halvings. 2⁶ = 64, so log₂(64) = 6. O(log n).
</details>

2. `factorial(4)` is defined as `4 × factorial(3)`, with `factorial(1) = 1`. Write the staircase.

<details><summary>Answer</summary>
factorial(4) = 4 × factorial(3) = 4 × (3 × factorial(2)) = 4 × (3 × (2 × factorial(1)))
= 4 × 3 × 2 × 1 = 24. Depth of the call stack: 4.
</details>

3. You sort a list (O(n log n)) and then loop over it once (O(n)). Total Big-O?

<details><summary>Answer</summary>
O(n log n). When steps happen one after another, the biggest one wins. You only multiply
when one loop is *inside* another.
</details>

### Common confusions, cleared

- **"Isn't O(2n) worse than O(n)?"** No. Big-O drops constant multipliers. Two passes over the
  list is still O(n). What matters is the shape, not the count of passes.
- **"How can a function call itself? Doesn't it loop forever?"** Only if you forget the base
  case or fail to make the input smaller. Every recursive call must move toward the base case.
  Check those two things and it always terminates.
- **"I have to trace the whole recursion to trust it."** You do not, and trying to is what makes
  recursion feel impossible. Check the base case is right. Check that *if* the smaller call is
  right, your one line combining it is right. That is the entire proof. Then stop tracing.
- **"Python is slow, so Big-O matters less."** The opposite. Python is about 50× slower than C,
  so a bad Big-O hurts you sooner. That is why 10⁸ steps per second is a generous estimate here.

### What to do next

Scroll down to Part 2 and read §2, the Python page, with a terminal open. Type each line. Then read
Part 2 §3 on Big-O and check that the table there now looks obvious. Then do `word_frequencies` and
`merge_sorted` in `exercises.py`. Save `fast_pow` and `flatten` for a second sitting: they are
recursion, and recursion is better learned after a night's sleep on the staircase picture.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** Every service you have used today was built by someone
who could look at a loop and say "that will not survive a million users." Google returns a
search across billions of pages in about 200 milliseconds because someone counted the steps.
Amazon's cart survives Prime Day because someone knew a dictionary lookup does not slow down
when the dictionary grows. Big-O is not exam trivia. It is the instinct that separates an
engineer from someone who types code.

**The analogy.** Think of your working memory as a kitchen counter with room for about four
items. In an interview, the problem itself takes two of those slots. If Python syntax and
"how does a for loop over a dict work again" take the other two, there is no room left to
think. This chapter moves Python and Big-O off the counter and into your hands, the way a
chef never thinks about how to hold a knife.

**How it works, in plain words.** Big-O asks one question: if I double the input, what happens
to the work? Stays the same: O(1). Doubles: O(n). Quadruples: O(n²). Goes up by one step:
O(log n). That is the whole idea. Everything else is practice recognizing which one you are
looking at. Recursion is the other half: a function that solves a problem by solving a
smaller copy of itself, and *trusts* that the smaller copy is correct. That trust feels wrong
the first ten times. It becomes the most powerful tool you own by the twentieth.

**What learning this will feel like.** You will be tempted to skip this chapter because it
looks easy. Resist. The trap is the "I already know this" feeling, which is recognition, not
recall. Recognition is knowing a face. Recall is producing the name. Interviews test recall.
Do the eight exercises with the lesson closed. If `fast_pow` or `flatten` makes you
uncomfortable, good: that discomfort is your brain building the recursion muscle, and it
should feel like lifting something slightly too heavy.

**You will know you have it when** you can read a nested loop and say its complexity before
you finish reading it, and when you write a recursive function without tracing it in your head.

### 1. The protocol: how to attack any problem

Interviewers do not grade the answer alone. They grade the *process*. Use the same six steps every
time until they are reflex. In Chapter 15 you will time them.

1. **Understand.** Repeat the problem in your own words. Ask about input size, duplicates,
   negative numbers, empty input, and what to return when there is no answer.
2. **Examples.** Write two small examples by hand and one edge case. Work them with a pencil.
   If you cannot solve a size-4 input by hand, you cannot code it.
3. **Brute force.** Say the obvious solution and its complexity out loud. "I could check every
   pair, that is O(n²)." This proves you can always produce *something*.
4. **Optimize.** Ask: what work is the brute force repeating? Which pattern removes it?
   Sorted input suggests two pointers or binary search. Lookups suggest a hash map. "Top k"
   suggests a heap. Chapters 01 to 12 build this reflex.
5. **Code.** Write clean code with real variable names. Talk while you type.
6. **Test.** Trace your code on your smallest example, line by line, *before* the interviewer asks.
   Then say the final time and space complexity.

### 2. Python you must be fluent in

You do not need all of Python. You need this page, cold.

#### Lists

```python
a = [3, 1, 2]
a.append(4)          # O(1) amortized
a.pop()              # O(1) from the end
a.pop(0)             # O(n)  -- avoid; use collections.deque for a queue
a.insert(0, 9)       # O(n)
a[-1]                # last element
a[1:3]               # slice, copies -> O(k)
a[::-1]              # reversed copy
len(a), sum(a), min(a), max(a)   # O(n) each
sorted(a)            # new list, O(n log n)
a.sort(key=lambda x: -x)   # in place, stable
a.sort(key=lambda p: (p[1], -p[0]))  # sort by 2nd field asc, then 1st desc
x in a               # O(n)  -- if you do this in a loop, you need a set
grid = [[0] * cols for _ in range(rows)]   # correct 2-D init
grid = [[0] * cols] * rows                 # WRONG: rows share one list
```

#### Dicts and sets

```python
d = {}
d["k"] = d.get("k", 0) + 1     # count safely
seen = set(); seen.add(x); x in seen    # O(1) average

from collections import Counter, defaultdict
Counter("banana")               # {'a': 3, 'n': 2, 'b': 1}
Counter(nums).most_common(2)    # top 2 as (value, count) pairs
g = defaultdict(list); g[u].append(v)   # adjacency list without key checks

# tuples are hashable, lists are not
key = tuple(sorted(word))       # canonical key for anagram grouping
```

#### Strings

```python
s = "hello"
s[1:4], s[::-1], len(s)
s.split(), " ".join(words)
s.isalnum(), s.lower(), s.strip()
ord("a") == 97; chr(98) == "b"
ord(c) - ord("a")               # 0..25 index into a 26-slot list
# strings are immutable: building with += in a loop is O(n²). Use a list:
parts = []; parts.append(piece); result = "".join(parts)
```

#### The three structures you import

```python
from collections import deque
q = deque([start]); q.append(x); q.popleft()      # O(1) both ends -> BFS queue

import heapq
h = []; heapq.heappush(h, (priority, item)); heapq.heappop(h)   # min-heap
heapq.heappush(h, -x)           # max-heap trick: negate
heapq.heapify(lst)              # O(n)
heapq.nlargest(k, nums)         # small k only

import bisect
bisect.bisect_left(sorted_list, x)   # first index with value >= x
```

#### Control flow you will actually type

```python
for i, x in enumerate(nums): ...
for a, b in zip(list1, list2): ...
for i in range(len(nums) - 1, -1, -1): ...    # backwards
squares = [x * x for x in nums if x % 2 == 0]
lo, hi = 0, len(nums) - 1                     # tuple unpacking
a, b = b, a + b                               # swap / simultaneous assignment
INF = float("inf")
```

#### Integer math traps

```python
7 // 2 == 3;  -7 // 2 == -4      # floor division rounds toward -infinity
-7 % 3 == 2                       # modulo takes sign of the divisor
int(-7 / 2) == -3                 # truncation toward zero, if that is what you need
mid = (lo + hi) // 2              # no overflow in Python, but say it anyway
```

#### Recursion traps

```python
import sys; sys.setrecursionlimit(10**6)   # default is ~1000; deep DFS will crash without it

def f(x, memo={}): ...       # WRONG: mutable default is shared across calls
def f(x, memo=None):
    if memo is None: memo = {}

from functools import lru_cache
@lru_cache(maxsize=None)     # memoize a pure function of hashable args
def fib(n): ...

def outer():
    count = 0
    def inner():
        nonlocal count      # needed to assign to an enclosing variable
        count += 1
```

### 3. Big-O without hand-waving

Big-O counts how the number of basic steps grows with input size `n`. Drop constants,
keep the fastest-growing term.

| Class | Name | An example | n = 10⁵ takes about |
|-------|------|-----------|---------------------|
| O(1) | constant | dict lookup, array index | nothing |
| O(log n) | logarithmic | binary search | 17 steps |
| O(n) | linear | one pass over the array | 10⁵ |
| O(n log n) | linearithmic | sorting | 1.7 × 10⁶ |
| O(n²) | quadratic | every pair | 10¹⁰ — too slow |
| O(2ⁿ) | exponential | every subset | never finishes past n≈25 |
| O(n!) | factorial | every permutation | never past n≈11 |

**The one number to remember:** a machine does roughly 10⁸ simple operations per second.
When the constraints say `n ≤ 10⁵`, an O(n²) plan is 10¹⁰ operations, so it is wrong before you
write a line. When `n ≤ 20`, exponential is fine and probably intended. Read constraints first.
They tell you the target complexity.

#### How to count

```python
for i in range(n):            # n times
    for j in range(i, n):     # n, n-1, ..., 1  -> sum = n(n+1)/2 -> O(n²)
        ...

while n > 1:                  # halves each time -> O(log n)
    n //= 2

for x in nums:                # n times
    heapq.heappush(h, x)      # log n each  -> O(n log n)
```

**Amortized:** `list.append` sometimes copies the whole array, but averaged over many appends it
is O(1). Say "amortized O(1)" and interviewers nod.

**Space:** count the extra memory you allocate, not the input. A hash map of n entries is O(n).
Recursion depth counts too: a recursion that goes n deep uses O(n) stack.

### 4. Recursion: trust the function

Recursion is a function calling a smaller version of itself. Three rules:

1. **Base case first.** The smallest input you can answer directly.
2. **Make progress.** Every call must move toward the base case.
3. **Trust the call.** Assume `f(smaller)` returns the right answer. Do not trace it mentally;
   just use it. This is the leap that makes trees, graphs, and DP possible.

```python
def factorial(n):
    if n <= 1:                    # base case
        return 1
    return n * factorial(n - 1)   # trust factorial(n-1); make progress
```

Trace of `factorial(3)` on the call stack:

```
factorial(3) -> 3 * factorial(2)
                    factorial(2) -> 2 * factorial(1)
                                       factorial(1) -> 1
                    factorial(2) -> 2 * 1 = 2
factorial(3) -> 3 * 2 = 6
```

Depth of the stack = number of nested calls = O(n) space. Naive `fib(n)` calls itself twice per
level, so it is O(2ⁿ) time. Memoizing it (remembering each answer) makes it O(n). That single
observation is all of Chapter 10.

### 5. Worked example: the protocol in action

**Problem:** given a list of words, return the most frequent one. Ties go to the alphabetically
smaller word.

1. *Understand.* Words are lowercase strings? Can the list be empty? Assume non-empty, lowercase.
2. *Examples.* `["b","a","b","a"]` → `"a"` (tie, alphabetical). `["x"]` → `"x"`.
3. *Brute force.* For each word, count its occurrences by scanning the whole list. O(n²).
4. *Optimize.* The repeated work is recounting. Count once into a dict: O(n). Then pick the best
   key by `(-count, word)`.
5. *Code.*

```python
def most_frequent(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return min(counts, key=lambda w: (-counts[w], w))
```

6. *Test.* Trace `["b","a","b","a"]`: counts = {b:2, a:2}. Keys sorted by (-2,"a") < (-2,"b") → "a". ✓
   Time O(n), space O(k) for k distinct words.

Notice the shape: brute force, name the waste, remove it with a structure. You will do this
150 more times.

### 6. Exercises

Open `exercises.py`. Each function has its problem statement in the docstring. Run
`python exercises.py` to see PASS / FAIL / TODO per problem.

| # | Function | Teaches | One hint |
|---|----------|---------|----------|
| 1 | `is_palindrome_clean` | string filtering, `isalnum`, reversal | Build the cleaned string, compare to its reverse. |
| 2 | `word_frequencies` | dict counting | `d[w] = d.get(w, 0) + 1`. |
| 3 | `merge_sorted` | the two-pointer merge, used by mergesort and many list problems | Two indices, take the smaller, append leftovers. |
| 4 | `fast_pow` | recursion, halving → O(log n) | `x^n = (x^(n//2))² · x^(n%2)`. |
| 5 | `transpose` | 2-D indexing, correct list init | `result[c][r] = grid[r][c]`. |
| 6 | `flatten` | recursion on nested lists | `isinstance(x, list)` decides recurse or append. |
| 7 | `fib` | memoization, the seed of DP | `@lru_cache` or a dict. Must handle n=90 instantly. |
| 8 | `BIG_O` | reading code and naming its complexity | Count loops. Halving is log. Nested independent loops multiply. |

When all eight pass, you are ready for Chapter 01. If `fast_pow` or `flatten` felt hard, redo
them tomorrow before moving on. Recursion is load-bearing for everything after this.
