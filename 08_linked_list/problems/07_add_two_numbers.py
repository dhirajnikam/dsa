"""
Problem: Add Two Numbers
Difficulty: Medium | Pattern: Parallel traversal with carry
Source: LeetCode 2

You are given two non-empty linked lists representing two non-negative integers. The digits
are stored in reverse order (least significant first), one digit per node. Add the two
numbers and return the sum as a linked list in the same format.

Example 1:
  Input: l1 = [2,4,3], l2 = [5,6,4]      (342 + 465)
  Output: [7,0,8]                         (807)

Example 2:
  Input: l1 = [0], l2 = [0]
  Output: [0]

Example 3:
  Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
  Output: [8,9,9,9,0,0,0,1]

Constraints:
  1 <= number of nodes in each list <= 100
  0 <= Node.val <= 9
  No leading zeros except the number 0 itself.

Hints:
1. Walk both lists together; treat a missing node as digit 0.
2. digit, carry = divmod(a + b + carry, 10).
3. Loop while either list has nodes OR carry is non-zero, so a final carry becomes a node.

Expected: O(max(n, m)) time, O(max(n, m)) space for the output.
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


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    raise NotImplementedError


if __name__ == "__main__":
    assert to_list(add_two_numbers(from_list([2, 4, 3]), from_list([5, 6, 4]))) == [7, 0, 8], 'Check: to_list(add_two_numbers(from_list([2, 4, 3]), from_list([5, 6, 4]))) == [7, 0, 8]'
    assert to_list(add_two_numbers(from_list([0]), from_list([0]))) == [0], 'Check: to_list(add_two_numbers(from_list([0]), from_list([0]))) == [0]'
    assert to_list(add_two_numbers(from_list([9, 9, 9, 9, 9, 9, 9]), from_list([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1], 'Check: to_list(add_two_numbers(from_list([9, 9, 9, 9, 9, 9, 9]), from_list([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1]'
    assert to_list(add_two_numbers(from_list([5]), from_list([5]))) == [0, 1], 'Check: to_list(add_two_numbers(from_list([5]), from_list([5]))) == [0, 1]'
    assert to_list(add_two_numbers(from_list([1, 8]), from_list([0]))) == [1, 8], 'Check: to_list(add_two_numbers(from_list([1, 8]), from_list([0]))) == [1, 8]'
    assert to_list(add_two_numbers(from_list([9]), from_list([1, 9, 9]))) == [0, 0, 0, 1], 'Check: to_list(add_two_numbers(from_list([9]), from_list([1, 9, 9]))) == [0, 0, 0, 1]'
    print("ok")
