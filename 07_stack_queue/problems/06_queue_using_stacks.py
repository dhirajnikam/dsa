"""
Problem: Implement Queue using Stacks
Difficulty: Easy | Pattern: two stacks, lazy transfer (amortised O(1))
Source: LeetCode 232

Implement a FIFO queue using only two stacks. Allowed stack operations: push to top, pop from
top, peek top, size, is empty. (In Python: list.append, list.pop(), list[-1], len.)

  MyQueue()           : initialise
  push(x)             : add x to the back
  pop() -> int        : remove and return the front (queue is non-empty)
  peek() -> int       : return the front
  empty() -> bool     : True if the queue is empty

Example:
  q = MyQueue()
  q.push(1); q.push(2)
  q.peek() -> 1
  q.pop() -> 1
  q.empty() -> False

Constraints:
  1 <= x <= 9
  up to 100 calls; pop/peek only on non-empty queues

Follow-up: make every operation amortised O(1).

Hints:
1. Stack `inbox` receives pushes. Stack `outbox` serves pops; its top is the queue front.
2. When `outbox` is empty and you need the front, move ALL of `inbox` into `outbox` (this reverses the order).
3. Each element is moved at most once, so total work over n operations is O(n): amortised O(1).

Expected: amortised O(1) per operation, O(n) space
"""


class MyQueue:
    def __init__(self):
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError

    def peek(self) -> int:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    q = MyQueue()
    assert q.empty() is True, 'Check: q.empty() is True'
    q.push(1); q.push(2)
    assert q.peek() == 1, 'Check: q.peek() == 1'
    assert q.pop() == 1, 'Check: q.pop() == 1'
    assert q.empty() is False, 'Check: q.empty() is False'
    assert q.pop() == 2, 'Check: q.pop() == 2'
    assert q.empty() is True, 'Check: q.empty() is True'
    q = MyQueue()
    q.push(1); q.push(2); q.push(3)
    assert q.pop() == 1, 'Check: q.pop() == 1'
    q.push(4)
    assert q.pop() == 2 and q.pop() == 3 and q.pop() == 4, 'Check: q.pop() == 2 and q.pop() == 3 and q.pop() == 4'
    assert q.empty() is True, 'Check: q.empty() is True'
    q = MyQueue()
    q.push(7)
    assert q.peek() == 7 and q.peek() == 7, 'Check: q.peek() == 7 and q.peek() == 7'
    assert q.pop() == 7, 'Check: q.pop() == 7'
    q.push(8); q.push(9)
    assert q.peek() == 8, 'Check: q.peek() == 8'
    q.push(1)
    assert q.pop() == 8 and q.pop() == 9 and q.pop() == 1, 'Check: q.pop() == 8 and q.pop() == 9 and q.pop() == 1'
    print("ok")
