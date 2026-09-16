# Python: values, decisions, and repetition

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** No previous Python knowledge.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A program transforms input into output. A variable is a name for a value. `=` stores a value; `==` asks whether two values are equal. An `int` stores a whole number, a `float` a decimal approximation, a `str` text, and a `bool` either `True` or `False`.

A **function** is a named operation. Parameters are its inputs. `return` sends its result to the caller and ends that call. `print` only displays a value. Tests call your function and inspect the returned value.

```python
# A tiny language example, separate from the practice questions.
def add_delivery_fee(price):
    return price + 20

bill = add_delivery_fee(80)
print(bill)  # 100
```

Python uses indentation to group statements. `if` chooses a branch. A `for` loop visits items; a `while` loop repeats while a condition remains true. Every `while` needs a way to make progress toward stopping. `range(3)` produces 0, 1, 2. `break` leaves the loop; `continue` skips to its next iteration.

`/` divides, `//` rounds division down, `%` gives the remainder, and `**` raises to a power. For example, 17 items packed into boxes of 5 gives 3 full boxes and 2 left over. Expressions do not update variables automatically: `x + 1` computes a value; `x = x + 1` stores it.

A **list** is an ordered, changeable sequence. Index 0 is the first item; index -1 is the last. `[start:stop]` excludes stop and makes a new list. A **string** is a sequence of characters that cannot be edited in place. `split()` separates whitespace-delimited words; `join()` combines pieces with a separator. A **tuple** is a fixed sequence; it is usable as a dictionary key only when all its elements are hashable.

A **dictionary** associates unique keys with values, such as a username with a score. A **set** keeps distinct values and supports membership questions. A list remembers order and duplicates; a set is not an ordered output format. Dictionary/set lookup is average O(1), not a promise for every possible input.

Lists can be shared: after `b = a`, both names refer to the same list. Changing an item through `b` changes what `a` sees. `sorted(a)` returns a new list; `a.sort()` changes `a` and returns `None`. A sorting `key` chooses the property to compare. Equal keys retain their original order.

Use `None` for “no value.” Default function arguments are created once when the function is defined. A mutable default list can therefore leak data between calls. A lambda is a small unnamed function. A function can accept another function as an input.

## Walk through a small example

Track a shopping basket total by hand, without coding a practice answer:

| Step | Item | Total before | Total after |
|---|---:|---:|---:|
| Start | — | — | 0 |
| Visit | 30 | 0 | 30 |
| Visit | 12 | 30 | 42 |

The changing state is `total`; the loop visits each item once. Empty input visits nothing and leaves the initial value unchanged.

## Watch for

Printing instead of returning; reading nums[0] before checking whether nums is empty; a while loop whose variable never changes; confusing a new list with a shared list.

## Your next small step

Open [hello math](problems/01_hello_math.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 00/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Basic arithmetic](problems/01_hello_math.py)
- [String basics](problems/02_strings.py)
- [List basics](problems/03_lists.py)
- [Dict and set basics](problems/04_dicts_sets.py)
- [Loops and conditions](problems/05_control_flow.py)
- [Functions, defaults, multiple returns, mutation](problems/06_functions.py)
- [Sorting with keys](problems/07_sorting_builtin.py)
- [Word count report (mini project)](problems/08_mini_project_wordcount.py)

</details>
