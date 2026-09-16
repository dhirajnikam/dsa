"""
Problem: Middle of the Linked List
Difficulty: Easy | Pattern: Fast/slow pointers
Source: LeetCode 876

Given the head of a singly linked list, return the middle node. If there are two middle
nodes, return the second one.

Example 1:
  Input: head = [1,2,3,4,5]
  Output: node 3 (the returned node's list is [3,4,5])

Example 2:
  Input: head = [1,2,3,4,5,6]
  Output: node 4 (the returned node's list is [4,5,6])

Constraints:
  1 <= number of nodes <= 100
  1 <= Node.val <= 100

Hints:
1. Counting nodes then walking n // 2 steps works but takes two passes.
2. Move one pointer one step and another two steps; when the fast one runs out, slow is in the middle.
3. Loop condition: while fast and fast.next.

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


def middle_node(head: ListNode) -> ListNode:
    raise NotImplementedError


if __name__ == "__main__":
    assert to_list(middle_node(from_list([1, 2, 3, 4, 5]))) == [3, 4, 5], 'Check: to_list(middle_node(from_list([1, 2, 3, 4, 5]))) == [3, 4, 5]'
    assert to_list(middle_node(from_list([1, 2, 3, 4, 5, 6]))) == [4, 5, 6], 'Check: to_list(middle_node(from_list([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]'
    assert to_list(middle_node(from_list([1]))) == [1], 'Check: to_list(middle_node(from_list([1]))) == [1]'
    assert to_list(middle_node(from_list([1, 2]))) == [2], 'Check: to_list(middle_node(from_list([1, 2]))) == [2]'
    assert to_list(middle_node(from_list([1, 2, 3]))) == [2, 3], 'Check: to_list(middle_node(from_list([1, 2, 3]))) == [2, 3]'
    assert middle_node(from_list([7, 7, 7, 7])).val == 7, 'Check: middle_node(from_list([7, 7, 7, 7])).val == 7'
    print("ok")
