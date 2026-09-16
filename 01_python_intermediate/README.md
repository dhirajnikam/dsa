# Objects, errors, and lazy sequences

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Python functions, lists, loops, and dictionaries (chapter 00).

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **class** defines a kind of object. Each instance has its own state; methods operate on that state through `self`. `__init__` initializes an instance. Use a class when several operations share changing data, not just to wrap every function.

A **dataclass** generates routine methods for data records. `frozen=True` prevents field reassignment, but does not make nested mutable objects immutable. Independent list fields need a factory rather than a shared list.

A comprehension expresses “visit, optionally filter, collect.” Write an ordinary loop first if the compact form hides the idea. An **iterable** can provide an iterator; an **iterator** remembers its position. `iter()` requests it and `next()` advances it. Exhaustion raises `StopIteration`.

A **generator** is an iterator made by a function containing `yield`. It pauses rather than completing; its local state survives until the next request. This can save memory, but consuming it twice does not restart it.

An **exception** signals that an operation could not complete. Catch the specific error you can handle; unexpected errors should remain visible. `*args` collects positional inputs into a tuple; `**kwargs` collects named inputs into a dictionary. Unpacking performs the reverse operation.

## Walk through a small example

Imagine a stream yielding temperatures 18, 21, 19. The first request receives 18; the second receives 21. The stream remembers that 19 is next. Turning the remainder into a list gives [19]; doing so again gives []. By contrast, iterating over the original list again can start from its beginning.

## Watch for

Sharing class-level mutable state accidentally; swallowing every exception; expecting an exhausted generator to restart; assuming frozen means deeply immutable.

## Your next small step

Open [comprehensions](problems/01_comprehensions.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 01/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Comprehensions](problems/01_comprehensions.py)
- [Bank account class](problems/02_classes_bank_account.py)
- [Point dataclass](problems/03_dataclass_point.py)
- [Lazy sequences with generators](problems/04_generators_fib.py)
- [Exceptions as control flow done right](problems/05_exceptions_safe_parse.py)
- [Variadic arguments and unpacking](problems/06_args_kwargs.py)
- [Reimplement range](problems/07_iter_protocol_range_clone.py)
- [Inventory manager (mini project)](problems/08_mini_project_inventory.py)

</details>
