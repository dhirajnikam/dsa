"""
Problem: Network Delay Time
Difficulty: Medium | Pattern: Dijkstra
Source: LeetCode 743

You have n nodes labeled 1..n and directed edges times[i] = [u, v, w] meaning a signal
takes w time to go from u to v. A signal is sent from node k. Return the time for all n
nodes to receive it, or -1 if some node never does.

Example 1:
  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2 -> 2
Example 2:
  times = [[1,2,1]], n = 2, k = 1 -> 1
Example 3:
  times = [[1,2,1]], n = 2, k = 2 -> -1

Constraints:
  1 <= k <= n <= 100
  0 <= w <= 100, no duplicate edges

Hints:
1. Single-source shortest path with non-negative weights: Dijkstra with a heap.
2. Answer is the largest shortest distance; -1 if any distance is still infinity.

Expected: O((V + E) log V) time, O(V + E) space
"""
import heapq
from collections import defaultdict


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert network_delay_time([[1, 2, 1]], 2, 1) == 1
    assert network_delay_time([[1, 2, 1]], 2, 2) == -1
    assert network_delay_time([], 1, 1) == 0
    assert network_delay_time([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1) == 3
    assert network_delay_time([[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], 3, 2) == 6
    assert network_delay_time([[1, 2, 0], [2, 3, 0]], 3, 1) == 0
    assert network_delay_time([[1, 2, 5], [1, 3, 5], [2, 4, 1], [3, 4, 10]], 4, 1) == 6
    print("ok")
