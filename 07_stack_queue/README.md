# Phase 07: Stack & Queue

**Goal:** spot "last in, first out" and "first in, first out" in a problem, and learn the monotonic stack.

## Key idea
A stack gives you back the most recent item first (a pile of plates). Use a Python list.
A queue gives you back the oldest item first (a line at a shop). Use `collections.deque`.
A monotonic stack keeps its items sorted. It answers "next greater / smaller element" for every index in one pass.

## Cheat sheet
```python
stack = []
stack.append(x); stack.pop(); stack[-1]   # push, pop, peek
if stack: ...                             # always check before pop/peek
from collections import deque
q = deque(); q.append(x); q.popleft()     # enqueue, dequeue, both O(1)
def next_greater(nums):                   # monotonic stack template
    res = [-1] * len(nums)
    stack = []                            # indices, values decreasing from bottom to top
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:   # x is the answer for smaller items
            res[stack.pop()] = i
        stack.append(i)
    return res
```

## When you see... use...
- "brackets / nesting / matching" -> stack of open items
- "next greater / warmer / smaller element" -> monotonic stack of indices
- "evaluate expression / decode nested string" -> stack of partial results
- "process in arrival order" -> deque
- "newest item can destroy earlier ones" -> stack simulation

## Common mistakes
- `list.pop(0)` is O(n). Use `deque.popleft()`.
- Popping an empty stack. Check `if stack` first.
- Postfix math: pop `b` first, then `a`, compute `a op b`. Use `int(a / b)` to truncate toward zero.
- Storing values instead of indices in a monotonic stack when you need distances.

## Problems
- `01_valid_parentheses.py` — stack of open brackets
- `02_min_stack.py` — store (value, min so far) pairs
- `03_evaluate_rpn.py` — number stack, operator pops two
- `04_daily_temperatures.py` — monotonic stack of indices
- `05_next_greater_element.py` — monotonic stack + dict
- `06_queue_using_stacks.py` — two stacks, pour when out is empty
- `07_decode_string.py` — stack of (text so far, repeat count)
- `08_asteroid_collision.py` — stack simulation
- `09_largest_rectangle_histogram.py` — hard: increasing stack, add a 0 at the end
