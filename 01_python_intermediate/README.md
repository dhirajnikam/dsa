# Phase 01: Python Intermediate

**Goal:** write Python the Python way: classes for state, comprehensions for building lists, generators for lazy data, exceptions for errors.

## Key idea
A class bundles data and the functions that work on it. A comprehension builds a list, dict, or set in one line.
A generator hands out values one at a time instead of building a big list. An exception says "something went wrong" without a magic return value.

## Cheat sheet
```python
[x * x for x in nums if x % 2 == 0]   # list comprehension: for ... if ... collect
{w: len(w) for w in words}            # dict comprehension

class Account:
    def __init__(self, balance=0):    # runs on Account()
        self.balance = balance        # self = this object
    def __repr__(self):               # what print() shows
        return f"Account({self.balance})"

def countdown(n):                     # generator: pauses at each yield
    while n > 0:
        yield n
        n -= 1

try:
    x = int(s)
except ValueError:                    # catch the narrowest error you can
    x = 0

def f(*args, **kwargs): ...           # args = tuple, kwargs = dict
first, *rest = [1, 2, 3]              # first=1, rest=[2, 3]
```

## Common mistakes
- Forgetting `self.` inside a method: `count += 1` makes a new local variable.
- A generator can be used once. `list(g)` a second time gives `[]`.
- `except:` with no type hides bugs. Name the exception.
- `@dataclass` with a list default needs `field(default_factory=list)`.

## Problems
- `01_comprehensions.py` — rewrite loops as comprehensions
- `02_classes_bank_account.py` — class with state and a custom error
- `03_dataclass_point.py` — frozen dataclass, sort and dedupe
- `04_generators_fib.py` — infinite Fibonacci generator, lazy helpers
- `05_exceptions_safe_parse.py` — parse safely, collect failures
- `06_args_kwargs.py` — variadic functions and unpacking
- `07_iter_protocol_range_clone.py` — make your own `range` with dunders
- `08_mini_project_inventory.py` — combine classes, errors, sorting
