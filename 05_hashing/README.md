# Hashing: remember what you have seen

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Chapter 00 dictionaries/sets; prefix sums from chapter 04 for the later subarray question.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **hash table** maps a hashable key to a stored location. A dictionary stores associated values; a set stores membership. Average lookup, insertion, and deletion are O(1), while worst-case collisions can be slower. Extra memory buys less repeated searching.

Decide what your key represents before coding. It might be a value already visited, a character frequency, or a normalized description of a group. Equal group descriptions must produce equal keys. A tuple of counts or a sorted representation can be hashable; a mutable list cannot be a dictionary key.

When solving a pair problem, the current item may need information from earlier items. The order of checking and recording matters because a single item may not be reused. For frequency problems, membership alone is insufficient: counts distinguish one occurrence from several.

A **prefix sum plus frequency map** can count earlier boundaries that would form a target sum, including when numbers are negative. Bidirectional mappings matter when a relation must be one-to-one. A randomized collection can combine list indexing with a map of positions, but deletion must keep both structures consistent.

## Walk through a small example

Scan badge IDs ["A", "C", "A"]. Before the first A the seen set is empty. After it, {A}; after C, {A, C}. At the last A, membership tells you it appeared earlier. This teaches the meaning of “seen” without writing the exercise implementation.

## Watch for

Using a set when frequency matters; mutating the mapping before asking about earlier items; assuming a dictionary can use a list as a key.

## Your next small step

Open [contains duplicate](problems/02_contains_duplicate.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 05/02
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Two Sum](problems/01_two_sum.py)
- [Contains Duplicate](problems/02_contains_duplicate.py)
- [Valid Anagram](problems/03_valid_anagram.py)
- [Group Anagrams](problems/04_group_anagrams.py)
- [Top K Frequent Elements](problems/05_top_k_frequent.py)
- [Longest Consecutive Sequence](problems/06_longest_consecutive_sequence.py)
- [Subarray Sum Equals K](problems/07_subarray_sum_equals_k.py)
- [Isomorphic Strings](problems/08_isomorphic_strings.py)
- [Insert Delete GetRandom O(1)](problems/09_insert_delete_getrandom_o1.py)

</details>
