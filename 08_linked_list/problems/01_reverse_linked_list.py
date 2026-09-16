"""
Problem: Reverse Linked List
Difficulty: Easy | Pattern: Pointer reversal
Source: LeetCode 206

Given the head of a singly linked list, reverse the list and return the new head.
Implement it twice: iteratively in reverse_list and recursively in reverse_list_recursive.

Example 1:
  Input: head = [1,2,3,4,5]
  Output: [5,4,3,2,1]

Example 2:
  Input: head = []
  Output: []

Constraints:
  0 <= number of nodes <= 5000
  -5000 <= Node.val <= 5000

Hints:
1. Keep three pointers: prev, cur, and the saved next. Flip cur.next to prev, then advance.
2. Recursively: reverse the rest of the list first, then make head.next point back to head.
3. Do not forget to set the old head's next to None or you create a cycle.

Expected: O(n) time, O(1) space iterative; O(n) space recursive.
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


def reverse_list(head: ListNode | None) -> ListNode | None:
    raise NotImplementedError


def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    raise NotImplementedError


if __name__ == "__main__":
    for f in (reverse_list, reverse_list_recursive):
        assert to_list(f(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1], 'Check: to_list(f(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]'
        assert to_list(f(from_list([1, 2]))) == [2, 1], 'Check: to_list(f(from_list([1, 2]))) == [2, 1]'
        assert to_list(f(from_list([1]))) == [1], 'Check: to_list(f(from_list([1]))) == [1]'
        assert f(None) is None, 'Check: f(None) is None'
        assert to_list(f(from_list([-1, 0, 1]))) == [1, 0, -1], 'Check: to_list(f(from_list([-1, 0, 1]))) == [1, 0, -1]'
    # old head must become the tail (no cycle)
    h = reverse_list(from_list([1, 2, 3]))
    assert h.next.next.next is None, 'Check: h.next.next.next is None'
    # Boundary and misconception checks: predict each result before running.
    for reverse in (reverse_list, reverse_list_recursive):
        first = from_list([5, 5])
        second = first.next
        result = reverse(first)
        assert result is second and result.next is first and first.next is None, 'Check: result is second and result.next is first and first.next is None'
    print("ok")
