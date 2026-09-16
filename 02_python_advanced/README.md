# Useful Python tools, learned when needed

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Chapter 01 and basic operation counting from chapter 03. This is an optional reference, not a gate before DSA.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **closure** retains access to an enclosing function’s variables. Rebinding one inside a nested function requires `nonlocal`. A **decorator** receives a function and returns a replacement, often to add timing or retry behavior. Preserve metadata with `functools.wraps`; retry only documented failures and always limit attempts.

`Counter` stores frequencies. `defaultdict` constructs a missing value when accessed by indexing. A `deque` supports efficient additions/removals at both ends; removing from the front of a list shifts the remaining items.

**Memoization** caches a function’s answer for an input. It helps when the same subproblem repeats, at the cost of memory. Cached arguments must be hashable; side effects and changing external state can make cached answers wrong.

`itertools` offers lazy iteration tools. Combinations ignore order; permutations distinguish order. A heap keeps the smallest item accessible without sorting every item. `bisect` finds insertion positions in a sorted list; finding the position is logarithmic, inserting into a Python list is still linear.

Special methods such as `__add__` and `__eq__` define how your objects behave with operators. Return `NotImplemented` for unsupported operand types rather than silently inventing behavior.

## Walk through a small example

A cache receives requests for the same expensive report: A, B, A. The first two compute results; the third can reuse A. If A depends on today’s date but the cache key includes only its name, the reused result may be stale. State what the input means before caching.

## Watch for

Confusing binary search cost with insertion cost; unlimited retries; caching stateful functions; choosing advanced syntax before understanding the loop.

## Your next small step

Open [counter defaultdict](problems/03_counter_defaultdict.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 02/03
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Three decorators](problems/01_decorator_timer_retry.py)
- [Closures](problems/02_closures_counter.py)
- [Counting and grouping with collections](problems/03_counter_defaultdict.py)
- [deque basics](problems/04_deque_sliding_max_naive.py)
- [Memoization](problems/05_lru_cache_memo.py)
- [itertools toolbox](problems/06_itertools_combos.py)
- [Vector with dunder methods](problems/07_dunder_vector.py)
- [bisect and heapq warm-up](problems/08_bisect_heapq_intro.py)

</details>
