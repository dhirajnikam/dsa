# 00 · Foundations

> "If you can't solve a problem, then there is an easier problem you can solve: find it." — George Pólya

This chapter gives you three things you will use in every single interview: fluent Python,
an honest sense of Big-O, and a protocol for attacking any problem. None of it is glamorous.
All of it is graded.

## 1. The protocol: how to attack any problem

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

## 2. Python you must be fluent in

You do not need all of Python. You need this page, cold.

### Lists

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

### Dicts and sets

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

### Strings

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

### The three structures you import

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

### Control flow you will actually type

```python
for i, x in enumerate(nums): ...
for a, b in zip(list1, list2): ...
for i in range(len(nums) - 1, -1, -1): ...    # backwards
squares = [x * x for x in nums if x % 2 == 0]
lo, hi = 0, len(nums) - 1                     # tuple unpacking
a, b = b, a + b                               # swap / simultaneous assignment
INF = float("inf")
```

### Integer math traps

```python
7 // 2 == 3;  -7 // 2 == -4      # floor division rounds toward -infinity
-7 % 3 == 2                       # modulo takes sign of the divisor
int(-7 / 2) == -3                 # truncation toward zero, if that is what you need
mid = (lo + hi) // 2              # no overflow in Python, but say it anyway
```

### Recursion traps

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

## 3. Big-O without hand-waving

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

### How to count

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

## 4. Recursion: trust the function

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

## 5. Worked example: the protocol in action

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

## 6. Exercises

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
