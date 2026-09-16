# Recursion and backtracking: explore choices

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Functions, lists, call-stack space, and a small recursive trace.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A recursive call solves a smaller instance. Its **base case** stops, and every path must move toward it. Each active call has its own local variables, although referenced lists may still be shared.

**Backtracking** explores a decision tree: choose an option, explore the consequences, then undo that choice before trying a sibling. A subset makes include/exclude choices. A permutation chooses an order and needs to remember which items are already used. A combination ignores order, so moving a starting boundary prevents duplicates.

A valid pruning rule stops a branch that cannot possibly work. It must follow from the input assumptions. For example, stopping after a sum becomes too large needs care if negative choices exist. Grid searches often mark a cell during one path and restore it for other paths.

Returning results requires snapshots of the current path. Otherwise several results can all reference one mutable list. Output size itself can be exponential: n independent binary decisions have 2^n leaves; copying each result can add another factor of n.

## Walk through a small example

Choose a drink (tea or coffee), then a size (small or large). The four leaves are tea-small, tea-large, coffee-small, coffee-large. After exploring tea’s sizes, undo the tea choice before exploring coffee. The current path is one choice sequence, not the entire answer list.

## Watch for

No shrinking measure; forgetting to undo shared state; appending the same mutable path repeatedly; pruning without proving it is safe.

## Your next small step

Open [subsets](problems/01_subsets.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 09/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Subsets](problems/01_subsets.py)
- [Permutations](problems/02_permutations.py)
- [Combinations](problems/03_combinations.py)
- [Combination Sum](problems/04_combination_sum.py)
- [Letter Combinations of a Phone Number](problems/05_letter_combinations_phone.py)
- [Generate Parentheses](problems/06_generate_parentheses.py)
- [Word Search](problems/07_word_search.py)
- [Palindrome Partitioning](problems/08_palindrome_partitioning.py)
- [N-Queens](problems/09_n_queens.py)

</details>
