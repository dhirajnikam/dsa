# Phase 00: Python Basics

**Goal:** write small programs without looking things up.

## Key idea
Python has 5 containers you will use every day: `int/str`, `list`, `tuple`, `dict`, `set`.
Learn what each one is good at and how fast its operations are. That is 80% of this phase.

## Cheat sheet
```python
a = [3, 1, 2]                 # list: ordered, changeable
a.append(4); a.sort(); a[-1]  # add, sort in place, last item
a[1:3]                        # slice -> [1, 2]

d = {"a": 1}                  # dict: key -> value, O(1) lookup
d.get("z", 0)                 # default instead of error
for k, v in d.items(): ...

s = {1, 2}                    # set: unique items, O(1) "in"
s.add(3); 2 in s

t = (1, 2)                    # tuple: like a list but frozen; can be a dict key

for i, x in enumerate(a): ... # index + value
f"{x} costs {price:.2f}"      # f-string formatting
"".join(parts)                # build strings this way, not with += in a loop
```

## Common mistakes
- `7 // 2` is `3` (floor). `-7 // 2` is `-4`, not `-3`.
- `[[0]*3]*2` shares one row. Use `[[0]*3 for _ in range(2)]`.
- `def f(a=[])` shares one list forever. Use `a=None`.
- `range(n)` stops at `n-1`.

## Problems
Do them in order. Run each file until it prints `ok`.
- `01_hello_math.py` — arithmetic, `//` and `%`
- `02_strings.py` — slicing, split, join
- `03_lists.py` — indexing, slicing, sorting
- `04_dicts_sets.py` — counting and membership
- `05_control_flow.py` — loops, if/else, early return
- `06_functions.py` — arguments, return tuples
- `07_sorting_builtin.py` — `sorted` with `key`
- `08_mini_project_wordcount.py` — put it all together
