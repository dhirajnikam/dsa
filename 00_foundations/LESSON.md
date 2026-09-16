# 00 · Foundations

**In one sentence.** Big-O is "how much slower does this get when the input gets bigger," and
recursion is "solve a big problem by solving a slightly smaller copy of it."

**Why you care.** Every interview problem ends with "what is the complexity?" and half of them
are solved with recursion. This chapter also gives you the Python you need cold, so your brain is
free for the actual problem in the room.

## The idea, with a story

**Big-O.** You are looking up a name in a phone book.

- Sorted book: open the middle, too far, open the middle of the first half, and so on.
  1,000 pages takes about 10 opens. 1,000,000 pages takes about 20. Doubling the book adds one
  open. That is **O(log n)**.
- Shuffled book: flip page by page. Doubling the book doubles the flips. That is **O(n)**.
- Compare every person with every other person: 1,000 people is about 1,000,000 comparisons.
  Doubling the book *quadruples* the work. That is **O(n²)**.

Big-O ignores how long one flip takes. It only cares about the *shape* of the growth.

**Recursion.** You are the CEO and want a headcount. You do not count. You ask your two VPs
"how many people are under you, including you?" They ask their managers. At the bottom, someone
with no reports says "1." Answers flow back up, each person adding one for themself. You never
counted anyone. You trusted the smaller version of the same question.

## The same story with numbers

Add up a list by trusting a smaller list:

```python
def total(nums):
    if not nums:                       # base case: empty list sums to 0
        return 0
    return nums[0] + total(nums[1:])   # first item + (trust this for the rest)
```

```
total([5, 2, 9]) = 5 + total([2, 9])
                       = 5 + (2 + total([9]))
                       = 5 + (2 + (9 + total([])))
                       = 5 + (2 + (9 + 0)) = 16
```

Down to the base case, then answers come back up. Every recursive function is this staircase.

Pause and predict: `factorial(n) = n * factorial(n-1)`, `factorial(1) = 1`. What is the staircase
for `factorial(4)`?

<details><summary>Answer</summary>
4 × factorial(3) = 4 × 3 × factorial(2) = 4 × 3 × 2 × factorial(1) = 4 × 3 × 2 × 1 = 24.
</details>

## The protocol for every problem

Use these six steps every time until they are reflex. Interviewers grade the process.

1. **Understand.** Repeat the problem in your words. Ask about size, duplicates, negatives, empty input.
2. **Examples.** Two small ones and one edge case, worked by hand.
3. **Brute force.** Say the obvious solution and its complexity. "All pairs, O(n²)."
4. **Optimize.** What work is repeated? Which pattern removes it? Chapters 01 to 12 build this.
5. **Code.** Real variable names. Talk while you type.
6. **Test.** Trace your smallest example line by line before they ask. State time and space.

## Reading constraints

A computer does about 100,000,000 simple steps per second. The line `n ≤ 100,000` in a problem
is the interviewer telling you which Big-O will pass.

| Constraint | O(n²) steps | Verdict |
|-----------|-------------|---------|
| n ≤ 1,000 | 1,000,000 | anything works |
| n ≤ 100,000 | 10,000,000,000 | O(n²) takes 100 seconds; you need O(n log n) or better |
| n ≤ 20 | 400 | try everything, even all 2²⁰ ≈ 1,000,000 subsets |

Read this line first. It saves ten minutes of wandering.

## Python you need cold

```python
# lists
a.append(x); a.pop()            # O(1)      a.pop(0), a.insert(0, x)   # O(n): use deque
a[-1]; a[1:3]; a[::-1]          # last, slice (copies), reversed copy
a.sort(key=lambda p: (p[1], -p[0]))   # sort by 2nd field asc, then 1st desc
grid = [[0] * cols for _ in range(rows)]   # NOT [[0]*cols]*rows (rows would be shared)

# dicts and sets
d[k] = d.get(k, 0) + 1          # count safely
from collections import Counter, defaultdict, deque
Counter(words).most_common(2); g = defaultdict(list)
seen = set(); seen.add(x); x in seen         # O(1) average

# strings are immutable: build with a list, then "".join(parts)
ord("a") == 97; chr(98) == "b"; ord(c) - ord("a")   # 0..25

# queues and heaps
q = deque([start]); q.append(x); q.popleft()          # BFS queue
import heapq; heapq.heappush(h, (priority, item)); heapq.heappop(h)   # min-heap; negate for max

# loops
for i, x in enumerate(nums): ...
for i in range(len(nums) - 1, -1, -1): ...            # backwards
lo, hi = 0, len(nums) - 1; a, b = b, a + b            # unpack, swap

# traps
-7 // 2 == -4                   # floor division rounds down, not toward zero
import sys; sys.setrecursionlimit(10**6)              # default ~1000; deep recursion crashes
def f(x, memo=None): memo = {} if memo is None else memo   # never memo={} as a default
from functools import lru_cache                        # @lru_cache(maxsize=None) memoizes
```

## Words you will hear

- **n.** Size of the input.
- **O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ).** Flat, halving, one pass, sorting, all pairs,
  all subsets. Only the biggest term counts. O(2n) is just O(n).
- **Space complexity.** Extra memory you allocate. A dict of n things is O(n). So is recursion n deep.
- **Base case.** The smallest input you answer directly. **Recursive case.** The line that calls itself.
- **Call stack.** The pile of unfinished calls waiting for answers.
- **Memoization.** Writing down each answer so you never compute it twice. The seed of Chapter 10.
- **Amortized.** Averaged over many operations. `append` is amortized O(1).

## Mistakes everyone makes once

- **Nested loops one after another are not O(n²).** Steps in sequence add; only a loop *inside* a
  loop multiplies. Sort then scan is O(n log n).
- **Tracing every recursive call.** Check the base case, check the one combining line, then stop.
  Trusting the smaller call is the skill.
- **`[[0] * cols] * rows`.** Every row is the same list. Change one, change all.
- **Skipping this chapter** because it looks easy. Recognizing is not recalling. Do the exercises
  with the lesson closed.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Teaches | Hint |
|---|----------|---------|------|
| 1 | `is_palindrome_clean` | strings | Keep only `isalnum()` chars, lowercase, compare to reverse. |
| 2 | `word_frequencies` | dict counting | `d[w] = d.get(w, 0) + 1`. |
| 3 | `merge_sorted` | two-pointer merge | Two indices, take the smaller, append leftovers. |
| 4 | `fast_pow` | recursion, halving | `x^n = (x^(n//2))² · x^(n%2)`. |
| 5 | `transpose` | 2-D indexing | `out[c][r] = grid[r][c]`. |
| 6 | `flatten` | recursion on lists | `isinstance(x, list)` decides recurse or append. |
| 7 | `fib` | memoization | `@lru_cache`. Must handle n = 90 instantly. |
| 8 | `BIG_O` | naming complexity | Count loops. Halving is log. Nested independent loops multiply. |

Do 1, 2, 3, 5 today. Do 4, 6, 7 tomorrow: they are recursion, and recursion is better after a
night's sleep on the staircase picture. Then 8.
