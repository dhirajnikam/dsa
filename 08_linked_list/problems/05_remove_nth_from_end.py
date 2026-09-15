"""
Problem: Remove Nth Node From End of List
Difficulty: Medium | Pattern: Gap pointers + dummy head
Source: LeetCode 19

Given the head of a linked list, remove the n-th node from the end and return the head.

Example 1:
  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]

Example 2:
  Input: head = [1], n = 1
  Output: []

Example 3:
  Input: head = [1,2], n = 1
  Output: [1]

Constraints:
  1 <= number of nodes <= 30
  0 <= Node.val <= 100
  1 <= n <= number of nodes

Hints:
1. Two-pass: count the length, then walk to length - n - 1. Fine, but do it in one pass.
2. Advance a fast pointer n steps ahead, then move both until fast reaches the last node.
3. Start slow at a dummy before head so removing the first node needs no special case.

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


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    raise NotImplementedError


if __name__ == "__main__":
    assert to_list(remove_nth_from_end(from_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert remove_nth_from_end(from_list([1]), 1) is None
    assert to_list(remove_nth_from_end(from_list([1, 2]), 1)) == [1]
    assert to_list(remove_nth_from_end(from_list([1, 2]), 2)) == [2]
    assert to_list(remove_nth_from_end(from_list([1, 2, 3, 4, 5]), 5)) == [2, 3, 4, 5]
    assert to_list(remove_nth_from_end(from_list([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4]
    print("ok")
