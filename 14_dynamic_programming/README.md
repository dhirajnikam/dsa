# Dynamic programming: name the smaller question

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Recursion, arrays, and operation counting. Start with one-dimensional state.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

**Dynamic programming (DP)** saves answers to overlapping subproblems. It works when a larger answer can be built from suitably chosen smaller answers. Do not start by guessing a memorized formula; define what one state means in a complete sentence.

Write four things: the state, base cases, transitions, and evaluation order. Top-down recursion with memoization computes states on demand. Bottom-up iteration evaluates prerequisites before dependent states. Estimate time as number of states times work per state, and include the table and active call stack in memory.

Different questions require different combinations: count ways adds counts; minimum cost takes a minimum; reachability combines booleans. Impossible states need an appropriate marker rather than accidentally looking like a zero-cost answer.

Order matters in coin problems: counting ordered sequences is different from counting combinations. A subsequence may skip positions; a substring cannot. Two-sequence problems often track one boundary in each sequence. Space compression is a later step that is safe only when overwritten states will never be needed again.

Some chapters’ advanced tasks need intervals or tree states. Finish the one-dimensional reasoning first, then add dimensions when the smaller question truly requires them.

## Walk through a small example

A delivery service may finish a route with either a short or a long final segment. Before calculating anything, label a state “best cost to reach stop i.” Then ask which earlier stops can precede i, what finishing from each costs, and what represents an unreachable stop. The state sentence determines the table meaning.

## Watch for

Memorizing a recurrence without state meaning; wrong base cases; confusing combinations with ordered sequences; overwriting a value before its last use.

## Your next small step

Open [climbing stairs](problems/01_climbing_stairs.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 14/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Climbing Stairs](problems/01_climbing_stairs.py)
- [House Robber](problems/02_house_robber.py)
- [House Robber II](problems/03_house_robber_ii.py)
- [Coin Change](problems/04_coin_change.py)
- [Coin Change II](problems/05_coin_change_ii.py)
- [Longest Increasing Subsequence](problems/06_longest_increasing_subsequence.py)
- [Partition Equal Subset Sum](problems/07_partition_equal_subset_sum.py)
- [Unique Paths](problems/08_unique_paths.py)
- [Minimum Path Sum](problems/09_min_path_sum.py)
- [Longest Common Subsequence](problems/10_longest_common_subsequence.py)
- [Edit Distance](problems/11_edit_distance.py)
- [Word Break](problems/12_word_break.py)
- [Decode Ways](problems/13_decode_ways.py)
- [Longest Palindromic Substring](problems/14_longest_palindromic_substring.py)
- [Burst Balloons](problems/15_burst_balloons.py)
- [House Robber III](problems/16_house_robber_iii_tree_dp.py)

</details>
