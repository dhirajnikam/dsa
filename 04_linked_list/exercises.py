"""04 · Linked Lists — exercises.

Run:  python exercises.py
Replace each `raise NotImplementedError` with your solution. PASS / FAIL / TODO per problem.
Stuck 30 min? Hint in LESSON.md. Stuck 40? One function from solutions.py, then rewrite it cold.
"""
from __future__ import annotations

import heapq  # noqa: F401 — needed for merge_k_sorted_lists
from typing import Optional


# ----------------------------------------------------------------------------- helpers
# These are complete. Use them in your solutions and in the checks; do not edit them.

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({to_list(self)})"


def from_list(values: list[int]) -> Optional[ListNode]:
    """[1, 2, 3] -> 1 -> 2 -> 3 -> None. Empty list -> None."""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    """1 -> 2 -> 3 -> None -> [1, 2, 3]. Stops after 10_000 nodes so a cycle cannot hang the test."""
    out: list[int] = []
    while head and len(out) <= 10_000:
        out.append(head.val)
        head = head.next
    return out


class RandomNode:
    """Node for copy_random_list: val, next, and a random pointer to any node (or None)."""

    def __init__(self, val: int, next: Optional["RandomNode"] = None,
                 random: Optional["RandomNode"] = None) -> None:
        self.val = val
        self.next = next
        self.random = random


# ----------------------------------------------------------------------------- problems

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse the list in place and return the new head. O(1) extra space.
    1->2->3->4->5 -> 5->4->3->2->1 ; 1->2 -> 2->1 ; None -> None
    """
    raise NotImplementedError


def merge_two_sorted(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted lists into one sorted list by splicing the existing nodes.
    1->2->4, 1->3->4 -> 1->1->2->3->4->4 ; None, None -> None ; None, 0 -> 0
    """
    raise NotImplementedError


def middle_node(head: ListNode) -> ListNode:
    """The middle node. For even length return the second of the two middles.
    1->2->3->4->5 -> node 3 ; 1->2->3->4->5->6 -> node 4
    """
    raise NotImplementedError


def has_cycle(head: Optional[ListNode]) -> bool:
    """True if following next pointers from head ever revisits a node. O(1) extra space.
    3->2->0->-4 with -4.next = node 2 -> True ; 1->2 -> False ; None -> False
    """
    raise NotImplementedError


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove the n-th node counting from the end (1 = the last node). One pass. 1 <= n <= length.
    1->2->3->4->5, 2 -> 1->2->3->5 ; 1, 1 -> None ; 1->2, 2 -> 2
    """
    raise NotImplementedError


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Each list stores a non-negative integer with digits in reverse order (ones digit first).
    Return their sum as a list in the same format.
    2->4->3 (342), 5->6->4 (465) -> 7->0->8 (807) ; 0, 0 -> 0 ; 9->9, 1 -> 0->0->1
    """
    raise NotImplementedError


def reorder_list(head: Optional[ListNode]) -> None:
    """Rearrange L0->L1->...->Ln in place into L0->Ln->L1->Ln-1->L2->... Change links, not values.
    Returns nothing; the test reads the list through the original head.
    1->2->3->4 -> 1->4->2->3 ; 1->2->3->4->5 -> 1->5->2->4->3 ; 1 -> 1
    """
    raise NotImplementedError


def copy_random_list(head: Optional[RandomNode]) -> Optional[RandomNode]:
    """Deep copy a list whose nodes also have a `random` pointer to any node in the list or None.
    New nodes must point only at new nodes. The copy must have the same shape: same values in
    order, and each copy's random points to the copy of the original's random target.
    """
    raise NotImplementedError


def find_duplicate_number(nums: list[int]) -> int:
    """nums has n + 1 integers, each in 1..n, so at least one value repeats. Exactly one value
    is repeated (possibly many times). Return it. O(1) extra space, do not modify nums.
    [1, 3, 4, 2, 2] -> 2 ; [3, 1, 3, 4, 2] -> 3 ; [3, 3, 3, 3, 3] -> 3
    """
    raise NotImplementedError


class LRUCache:
    """Least-recently-used cache with a fixed capacity. get and put are both O(1).
    get(key) returns the value or -1, and marks the key as most recently used.
    put(key, value) inserts or updates, marks most recent, and evicts the least recently used
    key when the capacity is exceeded.
    Build it with a dict + doubly linked list (two sentinels), the way an interviewer expects.
    cap 2: put(1,1) put(2,2) get(1)->1 put(3,3) get(2)->-1 put(4,4) get(1)->-1 get(3)->3 get(4)->4
    """

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverse every consecutive group of k nodes. A final group with fewer than k nodes stays
    as is. Change links, not values. O(1) extra space.
    1->2->3->4->5, 2 -> 2->1->4->3->5 ; 1->2->3->4->5, 3 -> 3->2->1->4->5 ; 1->2, 1 -> 1->2
    """
    raise NotImplementedError


def merge_k_sorted_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted lists into one sorted list. Aim for O(N log k) with heapq.
    [1->4->5, 1->3->4, 2->6] -> 1->1->2->3->4->4->5->6 ; [] -> None ; [None] -> None
    """
    raise NotImplementedError


# ----------------------------------------------------------------------------- checks

def _t_01_reverse_list():
    assert to_list(reverse_list(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(from_list([1, 2]))) == [2, 1]
    assert reverse_list(None) is None
    assert to_list(reverse_list(from_list([7]))) == [7]


def _t_02_merge_two_sorted():
    assert to_list(merge_two_sorted(from_list([1, 2, 4]), from_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert merge_two_sorted(None, None) is None
    assert to_list(merge_two_sorted(None, from_list([0]))) == [0]
    assert to_list(merge_two_sorted(from_list([1, 2, 3]), from_list([4, 5]))) == [1, 2, 3, 4, 5]
    assert to_list(merge_two_sorted(from_list([5]), from_list([1, 2]))) == [1, 2, 5]


def _t_03_middle_node():
    assert middle_node(from_list([1, 2, 3, 4, 5])).val == 3
    assert middle_node(from_list([1, 2, 3, 4, 5, 6])).val == 4
    assert middle_node(from_list([1])).val == 1
    assert to_list(middle_node(from_list([1, 2]))) == [2]


def _t_04_has_cycle():
    head = from_list([3, 2, 0, -4])
    head.next.next.next.next = head.next            # -4 -> 2: cycle
    assert has_cycle(head) is True
    assert has_cycle(from_list([1, 2])) is False
    assert has_cycle(None) is False
    single = ListNode(1)
    single.next = single                            # self-loop
    assert has_cycle(single) is True
    assert has_cycle(ListNode(1)) is False


def _t_05_remove_nth_from_end():
    assert to_list(remove_nth_from_end(from_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert remove_nth_from_end(from_list([1]), 1) is None
    assert to_list(remove_nth_from_end(from_list([1, 2]), 2)) == [2]
    assert to_list(remove_nth_from_end(from_list([1, 2]), 1)) == [1]
    assert to_list(remove_nth_from_end(from_list([1, 2, 3]), 3)) == [2, 3]


def _t_06_add_two_numbers():
    assert to_list(add_two_numbers(from_list([2, 4, 3]), from_list([5, 6, 4]))) == [7, 0, 8]
    assert to_list(add_two_numbers(from_list([0]), from_list([0]))) == [0]
    assert to_list(add_two_numbers(from_list([9, 9]), from_list([1]))) == [0, 0, 1]
    assert to_list(add_two_numbers(from_list([9, 9, 9, 9]), from_list([9, 9, 9]))) == [8, 9, 9, 0, 1]


def _t_07_reorder_list():
    h = from_list([1, 2, 3, 4]); reorder_list(h)
    assert to_list(h) == [1, 4, 2, 3]
    h = from_list([1, 2, 3, 4, 5]); reorder_list(h)
    assert to_list(h) == [1, 5, 2, 4, 3]
    h = from_list([1]); reorder_list(h)
    assert to_list(h) == [1]
    h = from_list([1, 2]); reorder_list(h)
    assert to_list(h) == [1, 2]
    h = from_list([1, 2, 3]); reorder_list(h)
    assert to_list(h) == [1, 3, 2]


def _build_random(values: list[int], random_idx: list[Optional[int]]) -> Optional[RandomNode]:
    nodes = [RandomNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for node, r in zip(nodes, random_idx):
        node.random = None if r is None else nodes[r]
    return nodes[0] if nodes else None


def _describe_random(head: Optional[RandomNode]) -> tuple[list[int], list[Optional[int]]]:
    nodes: list[RandomNode] = []
    cur = head
    while cur and len(nodes) <= 10_000:
        nodes.append(cur)
        cur = cur.next
    index = {id(n): i for i, n in enumerate(nodes)}
    return [n.val for n in nodes], [None if n.random is None else index[id(n.random)] for n in nodes]


def _t_08_copy_random_list():
    vals, rnd = [7, 13, 11, 10, 1], [None, 0, 4, 2, 0]
    orig = _build_random(vals, rnd)
    copy = copy_random_list(orig)
    assert _describe_random(copy) == (vals, rnd), _describe_random(copy)
    # deep: no node of the copy may be a node of the original
    originals = set()
    cur = orig
    while cur:
        originals.add(id(cur)); cur = cur.next
    cur = copy
    while cur:
        assert id(cur) not in originals and (cur.random is None or id(cur.random) not in originals)
        cur = cur.next
    assert _describe_random(orig) == (vals, rnd)          # original untouched
    assert copy_random_list(None) is None
    one = _build_random([5], [0])                          # random points at itself
    c = copy_random_list(one)
    assert c is not one and c.random is c and c.val == 5


def _t_09_find_duplicate_number():
    assert find_duplicate_number([1, 3, 4, 2, 2]) == 2
    assert find_duplicate_number([3, 1, 3, 4, 2]) == 3
    assert find_duplicate_number([3, 3, 3, 3, 3]) == 3
    assert find_duplicate_number([1, 1]) == 1
    nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1, 4]
    snapshot = list(nums)
    assert find_duplicate_number(nums) == 9
    assert nums == snapshot                                # not modified


def _t_10_lru_cache():
    c = LRUCache(2)
    c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)                                            # evicts 2
    assert c.get(2) == -1
    c.put(4, 4)                                            # evicts 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    c.put(3, 30)                                           # update existing, now most recent
    assert c.get(3) == 30
    c.put(5, 5)                                            # evicts 4
    assert c.get(4) == -1 and c.get(3) == 30 and c.get(5) == 5
    one = LRUCache(1)
    one.put(1, 1); one.put(2, 2)
    assert one.get(1) == -1 and one.get(2) == 2


def _t_11_reverse_k_group():
    assert to_list(reverse_k_group(from_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert to_list(reverse_k_group(from_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert to_list(reverse_k_group(from_list([1, 2]), 1)) == [1, 2]
    assert to_list(reverse_k_group(from_list([1, 2, 3, 4, 5, 6]), 3)) == [3, 2, 1, 6, 5, 4]
    assert to_list(reverse_k_group(from_list([1, 2, 3]), 5)) == [1, 2, 3]
    assert reverse_k_group(None, 2) is None


def _t_12_merge_k_sorted_lists():
    lists = [from_list([1, 4, 5]), from_list([1, 3, 4]), from_list([2, 6])]
    assert to_list(merge_k_sorted_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_sorted_lists([]) is None
    assert merge_k_sorted_lists([None]) is None
    assert to_list(merge_k_sorted_lists([None, from_list([2]), None, from_list([1])])) == [1, 2]
    assert to_list(merge_k_sorted_lists([from_list([5, 5]), from_list([5])])) == [5, 5, 5]


def _check():
    checks = [(n[3:], f) for n, f in sorted(globals().items()) if n.startswith("_t_")]
    passed = 0
    for name, fn in checks:
        try:
            fn()
            print(f"PASS  {name}")
            passed += 1
        except NotImplementedError:
            print(f"TODO  {name}")
        except AssertionError as e:
            print(f"FAIL  {name}  {e}")
        except Exception as e:  # noqa: BLE001 — show the student what blew up
            print(f"FAIL  {name}  {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(checks)} passed")


if __name__ == "__main__":
    _check()
