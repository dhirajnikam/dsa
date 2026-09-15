# Phase 08: Linked Lists

**Goal:** move `.next` pointers around without losing half the list.

## Key idea
A linked list is a chain of nodes. Each node holds a value and a pointer to the next node.
There is no index, so you walk from the head one step at a time.
Two tricks solve most problems: a dummy node in front, and a fast pointer that moves twice as quickly as a slow one.

## Cheat sheet
```python
class ListNode:
    def __init__(self, val=0, next=None): self.val, self.next = val, next
prev, cur = None, head                 # reverse in place
while cur:
    nxt = cur.next                     # save first, or the rest is lost
    cur.next = prev
    prev, cur = cur, nxt
return prev
slow = fast = head                     # fast/slow: middle of list
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
dummy = ListNode(0, head)              # dummy head: the real head may change
prev = dummy                           # edit prev.next freely, then
return dummy.next
```

## When you see... use...
- "the head might be removed or replaced" -> dummy head
- "middle / cycle / k-th from end in one pass" -> fast and slow pointers
- "reverse / reorder / swap" -> the reverse loop as a building block
- "merge two sorted lists" -> dummy head + pick the smaller node each step
- "O(1) get and put with eviction" -> dict + doubly linked list

## Common mistakes
- Overwriting `cur.next` before saving it. The rest of the list is gone.
- Forgetting to cut the tail after splitting: `slow.next = None`.
- Writing `while fast.next and fast` in the wrong order. `None.next` crashes.
- Comparing nodes with `==` when you mean the same node. Use `is`.

## Problems
- `01_reverse_linked_list.py` — the reverse loop
- `02_middle_of_list.py` — fast and slow pointers
- `03_merge_two_sorted_lists.py` — dummy head, pick the smaller
- `04_linked_list_cycle.py` — fast meets slow means a cycle
- `05_remove_nth_from_end.py` — move fast n steps ahead, then walk both
- `06_reorder_list.py` — middle + reverse second half + interleave
- `07_add_two_numbers.py` — digit by digit with a carry
- `08_lru_cache.py` — dict + doubly linked list
