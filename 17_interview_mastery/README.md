# Interview practice: explain, implement, check

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Comfort with the first lap and relevant chapter checkpoints. Timing is optional until the ideas feel familiar.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

An interview task measures how you turn an ambiguous request into a correct, explainable program. Start by restating inputs, outputs, constraints, and assumptions. Make an example, including a boundary case, before coding.

Describe a straightforward approach first. Count its work. Then identify which repeated work or missing summary a better structure could remove. Name a pattern only after explaining why its assumptions fit. A familiar keyword is not proof that a pattern applies.

Before implementation, state an invariant or state definition. While coding, explain decisions instead of narrating punctuation. When stuck, shrink the example and describe the unknown precisely. Testing should cover ordinary input, boundaries, and a case designed to break your chosen assumption.

A practice session can be 5 minutes of clarification, 10 of reasoning, 20 of coding, and 10 of checking. These are adjustable practice budgets, not scoring rules. Start untimed if time pressure blocks learning. Afterward write one thing to retain and one thing to revisit.

For behavioral questions, use Situation, Task, Action, Result, with your own contribution and an honest concrete outcome. Preparation supports clarity; it should not turn experiences into invented numbers.

## Walk through a small example

Suppose a prompt asks to group duplicate records. Ask whether identity means matching names, IDs, or shared email addresses. Records with matching names but different IDs expose the ambiguity. Clarifying that rule before choosing a dictionary or union-find can prevent an otherwise tidy wrong answer.

## Watch for

Coding before clarifying the contract; naming a pattern without justification; treating time pressure as a prerequisite; rehearsing a solution instead of reasoning about changed assumptions.

## Your next small step

Open [mock encode decode strings](problems/01_mock_encode_decode_strings.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 17/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Mock interview 1 - Encode and Decode Strings](problems/01_mock_encode_decode_strings.py)
- [Mock interview 2 - Kth Largest Element in a Stream](problems/02_mock_kth_largest_in_stream.py)
- [Mock interview 3 - Valid Sudoku](problems/03_mock_valid_sudoku.py)
- [Mock interview 4 - Time Based Key-Value Store](problems/04_mock_time_based_key_value_store.py)
- [Mock interview 5 - Min Cost Climbing Stairs](problems/05_mock_min_cost_climbing_stairs.py)
- [Mock interview 6 - Accounts Merge](problems/06_mock_accounts_merge.py)

</details>
