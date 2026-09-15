# Phase 17: Interview Mastery

**Goal:** solve a medium problem in 45 minutes while talking, the way a real interview runs.

## The 6 steps (every question)
1. **Clarify.** Restate the problem. Ask about input size, duplicates, empty input, and what to return when there is no answer. Write one example.
2. **Brute force out loud.** State the obvious approach and its complexity, even if you will not code it.
3. **Name the pattern.** "This is sliding window / two heaps / BFS because..." Use the table below.
4. **Confirm.** "I plan to do X in O(n log n) time and O(n) space. Should I go ahead?"
5. **Code while talking.** Skeleton first, then helpers. Never go silent for more than a minute.
6. **Test by hand.** Trace the smallest example line by line, then the edge cases from step 1. State time and space.

## Pattern cheat sheet
| If the problem says... | Try... |
|---|---|
| sorted array, find a pair or target | two pointers or binary search |
| longest / shortest subarray with a rule | sliding window |
| k-th largest, top k, running median | heap |
| next greater element, valid brackets | stack |
| count or group things | hash map |
| linked list cycle or middle | fast and slow pointers |
| grid or graph, shortest path in steps | BFS |
| all paths, connected regions, tree walk | DFS |
| tasks with prerequisites, ordering | topological sort |
| groups that merge, "connected" accounts | union-find |
| count ways, min cost, longest subsequence | dynamic programming |
| all combinations / permutations / subsets | backtracking |

## Behavioral
- Answer in STAR format: Situation, Task, Action, Result. Keep it under two minutes.
- Prepare 5 stories: a conflict, a failure, a hard technical problem, leading without authority, a tight deadline.
- Every story ends with a number or a concrete outcome, then one thing you learned.
- Ask the interviewer two real questions at the end.

## Problems
Set a 45-minute timer, speak out loud, and ask your clarifying questions before reading the hints.
- `01_mock_encode_decode_strings.py` — length prefix, then the string
- `02_mock_kth_largest_in_stream.py` — min-heap of size k
- `03_mock_valid_sudoku.py` — sets for rows, cols, boxes
- `04_mock_time_based_key_value_store.py` — dict of lists, binary search on time
- `05_mock_min_cost_climbing_stairs.py` — 1D DP, two variables
- `06_mock_accounts_merge.py` — union-find on emails
