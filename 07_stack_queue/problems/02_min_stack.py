"""
Problem: Min Stack
Difficulty: Medium | Pattern: auxiliary stack of running minimums
Source: LeetCode 155

Design a stack that supports push, pop, top, and retrieving the minimum element, all in O(1).

  MinStack()          : initialise
  push(val)           : push val
  pop()               : remove the top (stack is non-empty)
  top() -> int        : return the top
  get_min() -> int    : return the minimum element currently in the stack

Example:
  ms = MinStack()
  ms.push(-2); ms.push(0); ms.push(-3)
  ms.get_min() -> -3
  ms.pop()
  ms.top() -> 0
  ms.get_min() -> -2

Constraints:
  -2^31 <= val <= 2^31 - 1
  up to 3 * 10^4 calls; pop/top/get_min only on non-empty stacks

Hints:
1. Scanning for the min on each call is O(n). You need to remember the min at every depth.
2. Store pairs (val, min_so_far) on one stack, or keep a parallel min stack.
3. Popping restores the previous min automatically because it was stored with the element below.

Expected: O(1) per operation, O(n) space
"""


class MinStack:
    def __init__(self):
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def get_min(self) -> int:
        raise NotImplementedError


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2); ms.push(0); ms.push(-3)
    assert ms.get_min() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.get_min() == -2
    ms = MinStack()
    ms.push(5)
    assert ms.top() == 5 and ms.get_min() == 5
    ms.push(5); ms.push(5)
    ms.pop()
    assert ms.get_min() == 5
    ms = MinStack()
    for v in [3, 1, 4, 1, 5]:
        ms.push(v)
    assert ms.get_min() == 1
    ms.pop(); ms.pop()
    assert ms.get_min() == 1
    ms.pop()
    assert ms.get_min() == 1
    ms.pop()
    assert ms.get_min() == 3 and ms.top() == 3
    ms = MinStack()
    ms.push(2); ms.push(0); ms.push(3); ms.push(0)
    assert ms.get_min() == 0
    ms.pop()
    assert ms.get_min() == 0
    ms.pop()
    assert ms.get_min() == 0
    ms.pop()
    assert ms.get_min() == 2
    print("ok")
