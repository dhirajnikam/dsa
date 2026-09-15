"""
Problem: Merge k Sorted Lists
Difficulty: Hard | Pattern: k-way merge with heap
Source: LeetCode 23

You are given an array of k linked lists, each sorted in ascending order. Merge all the
lists into one sorted linked list and return its head.

Example 1:
  lists = [[1, 4, 5], [1, 3, 4], [2, 6]] -> [1, 1, 2, 3, 4, 4, 5, 6]
Example 2:
  lists = [] -> []
Example 3:
  lists = [[]] -> []

Constraints:
  0 <= k <= 10^4
  Total number of nodes <= 10^4
  -10^4 <= Node.val <= 10^4

Hints:
1. Heap holds one node per list: the current head. Pop the smallest, append it, push its next.
2. ListNode objects are not comparable. Push (val, list_index, node) so ties break on the index.
3. Alternative: divide and conquer, merging pairs. Same O(N log k).

Expected: O(N log k) time, O(k) space  (N = total nodes)
"""
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def from_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    raise NotImplementedError


if __name__ == "__main__":
    mk = lambda ls: merge_k_lists([from_list(l) for l in ls])
    assert to_list(mk([[1, 4, 5], [1, 3, 4], [2, 6]])) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert to_list(mk([])) == []
    assert to_list(mk([[]])) == []
    assert to_list(mk([[], [], []])) == []
    assert to_list(mk([[1]])) == [1]
    assert to_list(mk([[5], [1], [3]])) == [1, 3, 5]
    assert to_list(mk([[1, 1], [1], [1, 1, 1]])) == [1, 1, 1, 1, 1, 1]
    assert to_list(mk([[-2, 0], [-3, 4], []])) == [-3, -2, 0, 4]
    print("ok")
