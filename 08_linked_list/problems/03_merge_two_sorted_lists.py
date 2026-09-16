"""
Problem: Merge Two Sorted Lists
Difficulty: Easy | Pattern: Dummy head + two pointers
Source: LeetCode 21

You are given the heads of two sorted linked lists list1 and list2. Merge them into one
sorted list by splicing together the existing nodes. Return the head of the merged list.

Example 1:
  Input: list1 = [1,2,4], list2 = [1,3,4]
  Output: [1,1,2,3,4,4]

Example 2:
  Input: list1 = [], list2 = []
  Output: []

Example 3:
  Input: list1 = [], list2 = [0]
  Output: [0]

Constraints:
  0 <= number of nodes in each list <= 50
  -100 <= Node.val <= 100
  Both lists are sorted in non-decreasing order.

Hints:
1. Start from a dummy node so the head of the result is never a special case.
2. Repeatedly attach the smaller of the two current nodes to the tail.
3. When one list runs out, attach the remainder of the other in one assignment.

Expected: O(n + m) time, O(1) space.
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


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    raise NotImplementedError


if __name__ == "__main__":
    assert to_list(merge_two_lists(from_list([1, 2, 4]), from_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4], 'Check: to_list(merge_two_lists(from_list([1, 2, 4]), from_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]'
    assert merge_two_lists(None, None) is None, 'Check: merge_two_lists(None, None) is None'
    assert to_list(merge_two_lists(None, from_list([0]))) == [0], 'Check: to_list(merge_two_lists(None, from_list([0]))) == [0]'
    assert to_list(merge_two_lists(from_list([5]), None)) == [5], 'Check: to_list(merge_two_lists(from_list([5]), None)) == [5]'
    assert to_list(merge_two_lists(from_list([1, 2, 3]), from_list([4, 5]))) == [1, 2, 3, 4, 5], 'Check: to_list(merge_two_lists(from_list([1, 2, 3]), from_list([4, 5]))) == [1, 2, 3, 4, 5]'
    assert to_list(merge_two_lists(from_list([4, 5]), from_list([1, 2, 3]))) == [1, 2, 3, 4, 5], 'Check: to_list(merge_two_lists(from_list([4, 5]), from_list([1, 2, 3]))) == [1, 2, 3, 4, 5]'
    assert to_list(merge_two_lists(from_list([-3, 0]), from_list([-5, 7]))) == [-5, -3, 0, 7], 'Check: to_list(merge_two_lists(from_list([-3, 0]), from_list([-5, 7]))) == [-5, -3, 0, 7]'
    print("ok")
