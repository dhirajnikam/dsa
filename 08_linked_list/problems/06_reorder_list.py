"""
Problem: Reorder List
Difficulty: Medium | Pattern: Middle + reverse + merge
Source: LeetCode 143

Given the head of a singly linked list L0 -> L1 -> ... -> Ln-1 -> Ln, reorder it in place to
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
You may not modify node values, only the links. Return nothing.

Example 1:
  Input: head = [1,2,3,4]
  Output: [1,4,2,3]

Example 2:
  Input: head = [1,2,3,4,5]
  Output: [1,5,2,4,3]

Constraints:
  1 <= number of nodes <= 5 * 10^4
  1 <= Node.val <= 1000

Hints:
1. Three building blocks you already have: find middle, reverse a list, merge two lists alternately.
2. Cut the list after the middle (set middle.next = None) before reversing the second half.
3. Interleave: for each pair, save both nexts before rewiring.

Expected: O(n) time, O(1) space.
"""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def from_list(values: list) -> ListNode | None:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node: ListNode | None) -> list:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def reorder_list(head: ListNode | None) -> None:
    raise NotImplementedError


def _reordered(values: list) -> list:
    head = from_list(values)
    reorder_list(head)
    return to_list(head)


if __name__ == "__main__":
    assert _reordered([1, 2, 3, 4]) == [1, 4, 2, 3], 'Check: _reordered([1, 2, 3, 4]) == [1, 4, 2, 3]'
    assert _reordered([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3], 'Check: _reordered([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]'
    assert _reordered([1]) == [1], 'Check: _reordered([1]) == [1]'
    assert _reordered([1, 2]) == [1, 2], 'Check: _reordered([1, 2]) == [1, 2]'
    assert _reordered([1, 2, 3]) == [1, 3, 2], 'Check: _reordered([1, 2, 3]) == [1, 3, 2]'
    assert _reordered(list(range(1, 9))) == [1, 8, 2, 7, 3, 6, 4, 5], 'Check: _reordered(list(range(1, 9))) == [1, 8, 2, 7, 3, 6, 4, 5]'
    assert reorder_list(None) is None, 'Check: reorder_list(None) is None'
    print("ok")
