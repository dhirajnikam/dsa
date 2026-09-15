"""
Problem: Linked List Cycle
Difficulty: Easy | Pattern: Floyd's fast/slow pointers
Source: LeetCode 141

Given head, return True if the linked list has a cycle in it. A cycle exists if some node
can be reached again by continuously following next pointers.

Example 1:
  Input: head = [3,2,0,-4], tail connects to node index 1
  Output: True

Example 2:
  Input: head = [1,2], tail connects to node index 0
  Output: True

Example 3:
  Input: head = [1]
  Output: False

Constraints:
  0 <= number of nodes <= 10^4
  -10^5 <= Node.val <= 10^5

Hints:
1. A set of visited nodes works in O(n) space. Can you do O(1)?
2. Two runners on a circular track always meet. Move slow by 1 and fast by 2.
3. Compare nodes with 'is', not by value; values can repeat without a cycle.

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


def has_cycle(head: ListNode | None) -> bool:
    raise NotImplementedError


def _with_cycle(values: list, pos: int) -> ListNode:
    """Build a list and connect the tail to the node at index pos (-1 for no cycle)."""
    head = from_list(values)
    if pos < 0:
        return head
    tail = head
    while tail.next:
        tail = tail.next
    target = head
    for _ in range(pos):
        target = target.next
    tail.next = target
    return head


if __name__ == "__main__":
    assert has_cycle(_with_cycle([3, 2, 0, -4], 1)) is True
    assert has_cycle(_with_cycle([1, 2], 0)) is True
    assert has_cycle(_with_cycle([1], -1)) is False
    assert has_cycle(None) is False
    assert has_cycle(_with_cycle([1], 0)) is True  # self-loop
    assert has_cycle(_with_cycle([1, 1, 1, 1], -1)) is False  # equal values, no cycle
    assert has_cycle(_with_cycle(list(range(1000)), 999)) is True
    assert has_cycle(_with_cycle(list(range(1000)), -1)) is False
    print("ok")
