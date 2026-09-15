"""
Problem: Gas Station
Difficulty: Medium | Pattern: Greedy (running total with reset)
Source: LeetCode 134

There are n gas stations on a circle. gas[i] is the fuel at station i and cost[i] is the
fuel needed to travel from station i to i+1. You start with an empty tank at one station.
Return the starting index from which you can complete the circuit once clockwise, or -1
if impossible. The answer is guaranteed unique when it exists.

Example 1: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2] -> 3
Example 2: gas = [2, 3, 4], cost = [3, 4, 3] -> -1

Hints:
1. If sum(gas) < sum(cost) the answer is -1. Otherwise an answer exists.
2. Scan with tank += gas[i] - cost[i]. If tank drops below 0, no start in [start, i] works;
   set start = i + 1 and tank = 0.
3. Exchange argument: if you cannot get from start to i, then starting anywhere between
   them gives you even less fuel when you reach i.

Expected: O(n) time, O(1) space
"""


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1
    assert can_complete_circuit([5], [4]) == 0
    assert can_complete_circuit([1], [2]) == -1
    assert can_complete_circuit([3, 3], [3, 3]) == 0
    assert can_complete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4
    assert can_complete_circuit([0, 0, 10], [1, 1, 1]) == 2
    print("ok")
