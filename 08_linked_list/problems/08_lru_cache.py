"""
Problem: LRU Cache
Difficulty: Medium (Hard in practice) | Pattern: Dict + doubly linked list
Source: LeetCode 146

Design a data structure that follows the Least Recently Used (LRU) cache constraints.

  LRUCache(capacity): initialize with positive capacity.
  get(key) -> int: return the value if key exists, else -1.
  put(key, value): insert or update the key. If the number of keys exceeds capacity,
                   evict the least recently used key.

Both get and put count as "use". Both must run in O(1) average time.

Example:
  cache = LRUCache(2)
  cache.put(1, 1); cache.put(2, 2)
  cache.get(1)      -> 1
  cache.put(3, 3)   # evicts key 2
  cache.get(2)      -> -1
  cache.put(4, 4)   # evicts key 1
  cache.get(1)      -> -1
  cache.get(3)      -> 3
  cache.get(4)      -> 4

Constraints:
  1 <= capacity <= 3000
  0 <= key, value <= 10^4
  At most 2 * 10^5 calls to get and put.

Hints:
1. A dict gives O(1) lookup but no ordering; a doubly linked list gives O(1) move/remove
   but no lookup. Use both: dict maps key -> node.
2. Use two sentinel nodes (head, tail) so insert/remove never checks for None.
3. Write two private helpers, _remove(node) and _add_front(node); every operation is a
   combination of those.

Expected: O(1) time per operation, O(capacity) space.
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


class LRUCache:
    def __init__(self, capacity: int):
        raise NotImplementedError

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4

    c = LRUCache(1)
    c.put(2, 1)
    assert c.get(2) == 1
    c.put(3, 2)
    assert c.get(2) == -1 and c.get(3) == 2

    # update existing key refreshes recency and changes value
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 10)
    c.put(3, 3)  # evicts 2, not 1
    assert c.get(1) == 10 and c.get(2) == -1 and c.get(3) == 3
    assert c.get(99) == -1
    print("ok")
