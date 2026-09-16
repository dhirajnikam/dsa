"""04 · Linked Lists — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
from __future__ import annotations

import heapq
from typing import Optional

from exercises import ListNode, RandomNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head
    while cur:
        nxt = cur.next                 # save before touching next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
    # O(n) time, O(1) space.


def merge_two_sorted(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2               # whichever list still has nodes
    return dummy.next
    # O(n + m) time, O(1) extra space: nodes are reused, not copied.


def middle_node(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    # O(n) time, O(1) space. Even length: slow lands on the second middle.


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
    # O(n) time, O(1) space. Fast gains one step per iteration, so it cannot skip over slow.


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n + 1):             # gap of n+1 so slow stops just BEFORE the target
        fast = fast.next
    while fast:
        slow, fast = slow.next, fast.next
    slow.next = slow.next.next         # unlink the target
    return dummy.next
    # One pass, O(n) time, O(1) space. Dummy handles removing the head.


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    carry = 0
    while l1 or l2 or carry:           # carry alone can create a final node
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next
    # O(max(n, m)) time and space.


def reorder_list(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return
    slow, fast = head, head.next       # fast starts one ahead: slow ends at the FIRST middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = reverse_list(slow.next)   # reverse the second half
    slow.next = None                   # cut, or the first half runs into the second
    first = head
    while second:                      # interleave; second is never longer than first
        n1, n2 = first.next, second.next
        first.next = second
        second.next = n1
        first, second = n1, n2
    # O(n) time, O(1) space.


def copy_random_list(head: Optional[RandomNode]) -> Optional[RandomNode]:
    mapping: dict[RandomNode, RandomNode] = {}
    cur = head
    while cur:                         # pass 1: create every copy, values only
        mapping[cur] = RandomNode(cur.val)
        cur = cur.next
    cur = head
    while cur:                         # pass 2: wire pointers through the mapping
        copy = mapping[cur]
        copy.next = mapping.get(cur.next)        # .get: None maps to None
        copy.random = mapping.get(cur.random)
        cur = cur.next
    return mapping.get(head)
    # O(n) time, O(n) space. O(1)-space variant: interleave copies (A->A'->B->B'), then unweave.


def find_duplicate_number(nums: list[int]) -> int:
    slow = fast = nums[0]              # i -> nums[i] is a linked list; a duplicate is a cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]                     # phase 2: walk from the head to the cycle entrance
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
    # O(n) time, O(1) space, array untouched. Index 0 is never a target (values >= 1),
    # so it is a true head outside the cycle.


class LRUCache:
    class _Node:
        __slots__ = ("key", "val", "prev", "next")

        def __init__(self, key: int = 0, val: int = 0) -> None:
            self.key, self.val = key, val
            self.prev: Optional[LRUCache._Node] = None
            self.next: Optional[LRUCache._Node] = None

    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.map: dict[int, LRUCache._Node] = {}
        self.head = self._Node()       # sentinel: most recent lives right after head
        self.tail = self._Node()       # sentinel: least recent lives right before tail
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node: "LRUCache._Node") -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_front(self, node: "LRUCache._Node") -> None:
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)             # touching it makes it most recent
        self._add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_front(node)
            return
        node = self._Node(key, value)
        self.map[key] = node
        self._add_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev       # least recently used
            self._remove(lru)
            del self.map[lru.key]      # the key on the node is what makes eviction O(1)
    # get / put O(1). Sentinels mean _remove and _add_front never check for None.
    # OrderedDict version: move_to_end on get/put, popitem(last=False) to evict.


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev_group = dummy
    while True:
        kth = prev_group
        for _ in range(k):             # is there a full group ahead?
            kth = kth.next
            if kth is None:
                return dummy.next      # fewer than k remain: leave them
        next_group = kth.next
        prev, cur = next_group, prev_group.next     # reverse the group, ending at next_group
        while cur is not next_group:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        first = prev_group.next        # old group head, now the group tail
        prev_group.next = kth          # splice: previous group points at the new head
        prev_group = first
    # O(n) time, O(1) space. Every node is visited a constant number of times.


def merge_k_sorted_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    heap: list[tuple[int, int, ListNode]] = []
    for i, node in enumerate(lists):
        if node:
            heap.append((node.val, i, node))     # i breaks ties; ListNode has no ordering
    heapq.heapify(heap)
    dummy = ListNode()
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
    # O(N log k) time for N total nodes, O(k) heap space. Divide-and-conquer pairwise merging
    # gives the same time with O(1) extra space.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
