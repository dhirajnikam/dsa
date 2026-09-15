# Phase 02: Python Advanced

**Goal:** know the standard library tools that turn 20 lines into 2: `Counter`, `defaultdict`, `deque`, `heapq`, `bisect`, `lru_cache`.

## Key idea
A closure is a function that remembers variables from where it was made. A decorator is a function that wraps another function to add behaviour.
Dunder methods (like `__len__`) let your own class work with `len()`, `+`, `==`, and `in`.
Everything else here is a ready-made container you should reach for instead of writing it yourself.

## Cheat sheet
```python
from collections import Counter, defaultdict, deque
from functools import lru_cache, wraps
import heapq, bisect

Counter("banana").most_common(1)   # [('a', 3)]; missing key -> 0
groups = defaultdict(list)         # missing key -> new list
dq = deque(); dq.appendleft(0); dq.popleft()   # O(1) at both ends

@lru_cache(maxsize=None)           # remember results by argument
def fib(n): return n if n < 2 else fib(n - 1) + fib(n - 2)

def timed(f):                      # decorator: takes f, returns wrapper
    @wraps(f)                      # keep f's name
    def wrapper(*a, **kw): return f(*a, **kw)
    return wrapper

heapq.heappush(h, x); heapq.heappop(h)   # h[0] is always the smallest
bisect.bisect_left(a, x)                 # first index where x fits (a sorted)
```

## Common mistakes
- Changing an outer variable in a closure needs `nonlocal`.
- `groupby` groups only neighbours. Sort first.
- `bisect` on an unsorted list gives garbage silently.
- `if d[k]` on a `defaultdict` creates the key. Use `k in d`.

## Problems
- `01_decorator_timer_retry.py` — count, time, and retry decorators
- `02_closures_counter.py` — counters and the loop-lambda bug
- `03_counter_defaultdict.py` — top-k words, anagram groups
- `04_deque_sliding_max_naive.py` — deque as a window buffer
- `05_lru_cache_memo.py` — memoize recursion
- `06_itertools_combos.py` — combinations, product, groupby
- `07_dunder_vector.py` — Vector class with `+`, `==`, `[]`
- `08_bisect_heapq_intro.py` — sorted insert, k smallest, k-way merge
