"""
Problem: Task Scheduler
Difficulty: Medium | Pattern: max-heap + cooldown queue
Source: LeetCode 621

You are given tasks as uppercase letters, each taking one unit of CPU time. Identical
tasks must be separated by at least n units (the CPU may idle). Return the minimum number
of units the CPU takes to finish all tasks.

Example 1:
  tasks = ["A","A","A","B","B","B"], n = 2 -> 8   (A B idle A B idle A B)
Example 2:
  tasks = ["A","A","A","B","B","B"], n = 0 -> 6
Example 3:
  tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2 -> 16

Constraints:
  1 <= len(tasks) <= 10^4
  0 <= n <= 100

Hints:
1. Greedy: at each tick run the task with the most remaining count that is not cooling down.
2. Max-heap of remaining counts; a deque of (ready_time, count) for tasks cooling down.
   Each tick: pop from heap if any, decrement, push to the cooldown queue with ready_time = t + n.
   If the queue front is ready, move it back to the heap. Idle ticks advance time anyway.
3. Math shortcut: max(len(tasks), (max_count - 1) * (n + 1) + number_of_tasks_with_max_count).

Expected: O(T) time, O(1) space  (26 letters)
"""
import heapq
from collections import Counter, deque


def least_interval(tasks: list[str], n: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8, 'Check: least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8'
    assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6, 'Check: least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6'
    assert least_interval(list("AAAAAABCDEFG"), 2) == 16, 'Check: least_interval(list("AAAAAABCDEFG"), 2) == 16'
    assert least_interval(["A"], 5) == 1, 'Check: least_interval(["A"], 5) == 1'
    assert least_interval(["A", "A"], 3) == 5, 'Check: least_interval(["A", "A"], 3) == 5'
    assert least_interval(list("ABCDE"), 4) == 5, 'Check: least_interval(list("ABCDE"), 4) == 5'
    assert least_interval(list("AAABBBCCC"), 2) == 9, 'Check: least_interval(list("AAABBBCCC"), 2) == 9'
    assert least_interval(list("AAABBBCCCDDD"), 1) == 12, 'Check: least_interval(list("AAABBBCCCDDD"), 1) == 12'
    print("ok")
