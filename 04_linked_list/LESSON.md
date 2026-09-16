# 04 · Linked Lists

*New to this topic? Read `THEORY.md` in this folder first. It explains the idea from zero.*

> A linked list is the simplest structure that can hurt you. There is no index, only a chain
> of `next` pointers, and the moment you overwrite one before saving where it pointed, a piece
> of the list is gone forever. This chapter is about the discipline that prevents that.

**Interview frequency:** medium, but concentrated. Reverse Linked List and Merge Two Lists
are warm-ups everywhere. LRU Cache is one of the most asked Amazon problems, period. Google
uses Reverse in k-Groups and Copy List with Random Pointer to test pointer care under pressure.

## 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** The LRU cache you will build in this chapter sits inside
every CDN edge server and inside Redis, deciding which item to evict when memory is full. Operating
systems keep runnable processes in linked lists so a scheduler can move one to the front in
constant time. Your music app's next and previous buttons walk a doubly linked playlist. Git
history is a linked list: each commit holds a pointer to its parent, and a branch is just a name
pointing at one node. Nobody uses them to store a million numbers. Everybody uses them where a
middle insert or delete must be instant.

**The analogy.** A treasure hunt. Each clue tells you only where the next clue is. There is no map;
to reach clue seven you read clues one through six. Tear up a clue before reading it and every clue
after it is lost forever. That is exactly what happens when you overwrite a `next` pointer before
saving where it pointed. The rest of the list still exists. You simply have no way to get there.

**How it works, in plain words.** A node is a value plus an arrow to the next node. The list is one
arrow to the first node. Insert and delete are constant time once you are standing next to the
right node, because you only redraw two arrows. Finding that node costs a walk. Every problem in
this chapter is about redrawing arrows in the right order, and the order never changes: save the
arrow you are about to overwrite, overwrite it, then move forward using the copy.

**What learning this will feel like.** Reverse Linked List has four lines of body, and you will get
them in the wrong order at least once. The list will vanish or loop forever, with no error message
to help. That silence is the chapter's real difficulty, and it is normal. The cure is not
cleverness. Draw boxes and arrows on paper, and redraw after each pointer change. That is not a
crutch. It is the skill, and interviewers trust candidates who draw. The aha arrives when the
three-pointer dance stops being memorised steps and becomes "save, rewire, advance," a rhythm your
hands know. Expect LRU Cache to be a wall the first time: it is two structures working together,
and forgetting to delete the dict key on eviction is the bug that teaches you why the key lives on
the node.

**You will know you have it when** you write `nxt = cur.next` before you have decided what
`cur.next` will become, and you reach for a dummy head the moment the real head might be deleted.

## 1. The core idea

A node holds a value and a pointer to the next node. The list is just a pointer to the first
node, called the head. You get O(1) insert and delete *once you are standing at the right
node*, and O(n) for everything that needs to find that node.

Every linked list bug is the same bug: you changed a pointer, then needed the old value.
The fix is a rule: **save `next` before you touch `next`.**

```
what people write                       what works
cur.next = prev                         nxt = cur.next      # 1. save
cur = cur.next   # already overwritten! cur.next = prev     # 2. rewire
                                        prev = cur          # 3. advance
                                        cur = nxt
```

Three habits cover almost every problem in this chapter:

- **Dummy head.** A fake node in front of the real head. Now "insert before the first node"
  and "delete the first node" are not special cases. Return `dummy.next`.
- **Fast and slow pointers.** Two walkers at different speeds or with a fixed gap. Finds the
  middle, detects cycles, and reaches "n from the end" in one pass.
- **In-place reversal.** The three-pointer dance above. Learn it until your hands do it.

Draw the list. Always. Boxes and arrows on paper, and redraw after each pointer change. An
interviewer who sees you draw trusts your code more.

## 2. Anchor problem: Reverse Linked List, fully worked

**Problem.** Given the head of a singly linked list, reverse it and return the new head.

**Understand.** In place, so no new nodes and O(1) extra space. Empty list returns `None`.
Single node returns itself. The old tail becomes the new head, and the old head's `next` must
become `None` or the list is cyclic.

**Examples.** `1→2→3→4→5` becomes `5→4→3→2→1`. `1→2` becomes `2→1`. `[]` becomes `[]`.

**Brute force.** Copy values into a Python list, reverse it, and rebuild. O(n) time, O(n)
space. Correct. It also ignores the point of the question, which is pointer manipulation.

**Insight.** Walk the list once. At each node, point its `next` backward to the node you just
left. To keep walking after that, you must have saved the old `next` first.

**Code.**

```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next          # save
        cur.next = prev         # reverse the arrow
        prev = cur              # advance both
        cur = nxt
    return prev                 # cur is None; prev is the last node visited
```

**Test trace.** `1→2→3`:

```
start        prev=None  cur=1        1 → 2 → 3
step 1       nxt=2; 1.next=None      None ← 1    2 → 3
             prev=1  cur=2
step 2       nxt=3; 2.next=1         None ← 1 ← 2    3
             prev=2  cur=3
step 3       nxt=None; 3.next=2      None ← 1 ← 2 ← 3
             prev=3  cur=None
return prev = 3                      3 → 2 → 1 ✓
```

**Recursive version.** Reverse everything after `head`, then hang `head` on the end.

```python
def reverse_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)   # head.next is now the tail of the reversed rest
    head.next.next = head                     # tail points back to head
    head.next = None                          # head is the new tail
    return new_head
```

O(n) time, O(n) stack space. Interviewers sometimes ask for it after the iterative version
to see whether you understand the call stack. Know both; write the iterative one by default.

**Complexity.** O(n) time, O(1) space.

**What to say out loud.** "I keep two pointers, previous and current. At each node I save its
next, point it back at previous, and step both forward. When current runs off the end,
previous is the new head. One pass, constant space. I'll trace three nodes to check the
end conditions."

## 3. Patterns & templates in this chapter

### Dummy head

```python
dummy = ListNode(0, head)
tail = dummy
while ...:
    tail.next = <chosen node>
    tail = tail.next
return dummy.next
```

Merging, partitioning, removing nodes. Any time the head itself might be removed or replaced,
a dummy removes the special case.

### Fast and slow pointers

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is the middle (second middle for even length); fast is at or past the end
```

Cycle detection (Floyd): if `slow is fast` ever becomes true inside the loop, there is a
cycle. The fast pointer laps the slow one inside the loop, and because it gains exactly one
step per iteration it cannot jump over.

Fixed gap: advance `fast` n steps first, then move both until `fast` reaches the end.
`slow` is now n from the end.

### Floyd on an array (Find the Duplicate Number)

An array of `n + 1` values in `1..n` is a linked list in disguise: `i → nums[i]`. A duplicate
value means two indices point to the same node, which means a cycle. Phase 1 finds a meeting
point; phase 2 restarts one pointer at the head and walks both one step at a time until they
meet at the cycle entrance, which is the duplicate.

```python
slow = fast = nums[0]
while True:
    slow, fast = nums[slow], nums[nums[fast]]
    if slow == fast: break
slow = nums[0]
while slow != fast:
    slow, fast = nums[slow], nums[fast]
return slow
```

### In-place reversal of a segment

Reverse k Groups and Reorder List both reverse part of a list and splice it back. Steps:

1. Find the node *before* the segment (`prev_group`) and the node *after* it (`next_group`).
2. Reverse the segment with the three-pointer loop, stopping at `next_group`.
3. `prev_group.next` = new segment head; segment tail `.next = next_group`.

Draw the four boundary pointers before you write a line.

### Doubly linked list + dict (LRU Cache)

`OrderedDict` gives a 15-line answer and interviewers know it. They will ask you to build it
yourself. The structure: a dict from key to node, and a doubly linked list of nodes ordered
by recency with two sentinels so insert and remove never check for `None`.

```python
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

def _remove(node):                     # unlink node from wherever it is
    node.prev.next = node.next
    node.next.prev = node.prev

def _add_front(node):                  # insert right after the head sentinel (most recent)
    node.next = head.next
    node.prev = head
    head.next.prev = node
    head.next = node
```

`get`: look up, `_remove`, `_add_front`, return value. `put`: if present, update and move to
front; else create and add to front; if over capacity, remove `tail.prev` and delete its key
from the dict. Every operation is O(1). The `key` lives on the node so eviction can find the
dict entry.

### Merge with a heap (previews Chapter 07)

Merging k sorted lists: push `(val, list_index, node)` for each head into a heap. Pop the
smallest, append to the output, push that node's `next`. O(N log k) for N total nodes. The
`list_index` breaks ties so nodes are never compared directly.

## 4. Recognition cues

| You see | Think |
|---------|-------|
| "reverse," "in place," "O(1) space" | three-pointer reversal |
| "merge sorted lists" | dummy head, walk both, append the smaller |
| "middle," "half" | fast/slow |
| "cycle," "loop," "does it terminate" | Floyd: fast/slow, meet inside the loop |
| "nth from the end" in one pass | two pointers with a gap of n |
| "array of n+1 values in 1..n, find duplicate, no extra space" | array as linked list, Floyd |
| "L0→Ln→L1→Ln-1" | middle, reverse second half, interleave |
| "digits stored reversed" | walk both with a carry, dummy head |
| "random pointer," "deep copy" | dict old node → new node, two passes (or interleave) |
| "least recently used," "O(1) get and put" | dict + doubly linked list with sentinels |
| "k sorted lists" | min-heap of heads |
| "reverse every k" | count k ahead, reverse the segment, splice |

## 5. Pitfalls

- **Overwriting `next` before saving it.** The bug behind half of all linked list failures.
- **Forgetting to terminate.** After reversing or reordering, the old head or the middle
  node still points forward. Set its `next = None` or you get a cycle and an infinite loop.
- **Losing the head.** If you walk `head` forward you cannot return it. Walk a copy.
- **`while fast and fast.next`.** Both checks. `fast.next.next` on a `None` crashes.
- **Even-length middle.** The template above returns the *second* middle. For Reorder List
  you want the first middle: start `fast = head.next`, or stop when `fast.next is None or
  fast.next.next is None`.
- **Remove nth from end with n == length.** The head itself is removed. Use a dummy and
  start both pointers there.
- **Add Two Numbers: final carry.** `9→9` plus `1` needs one more node. Loop
  `while l1 or l2 or carry`.
- **Reverse k Groups: partial last group.** Count k nodes ahead first. If fewer remain, stop
  and leave them alone.
- **Copy Random List: `random` may be `None`.** `mapping.get(None)` is `None`, which is the
  right answer, so use `.get` or guard.
- **LRU Cache: update the dict on eviction.** Removing the tail node without deleting its
  key leaves a stale entry that `get` will happily return.
- **LRU Cache: `put` on an existing key** must update the value *and* move to front.
- **Comparing nodes in a heap.** `ListNode` has no `<`. Push a tuple with a tiebreaker index.

## 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|----------|-----------|----------|----------|
| 1 | `reverse_list` | Easy | Everyone | The anchor above. Save, reverse, advance. |
| 2 | `merge_two_sorted` | Easy | Amazon, Google | Dummy head. Append the smaller head; attach the leftover list at the end. |
| 3 | `middle_node` | Easy | Amazon | Fast/slow. `while fast and fast.next`. |
| 4 | `has_cycle` | Easy | Amazon, Google | Floyd. Return True the moment `slow is fast`. |
| 5 | `remove_nth_from_end` | Medium | Amazon, Google | Dummy. Move `fast` n+1 steps, then both. `slow.next = slow.next.next`. |
| 6 | `add_two_numbers` | Medium | Amazon, Google | Walk both with a carry. `while l1 or l2 or carry`. |
| 7 | `reorder_list` | Medium | Amazon, Google | Find first middle, cut, reverse the second half, interleave. |
| 8 | `copy_random_list` | Medium | Amazon, Google | Pass 1: dict old → new with values. Pass 2: wire `next` and `random` through the dict. |
| 9 | `find_duplicate_number` | Medium | Amazon, Google | `i → nums[i]` is a linked list. Floyd, then find the cycle entrance. |
| 10 | `LRUCache` | Medium | Amazon (very often), Google | Dict + doubly linked list with two sentinels. `key` on the node. |
| 11 | `reverse_k_group` | Hard | Google, Amazon | Count k ahead. Reverse exactly k. Splice with `prev_group` and `next_group`. |
| 12 | `merge_k_sorted_lists` | Hard | Amazon, Google | Heap of `(val, i, node)`. Pop, append, push `node.next`. |

Solve 1–9 in order. 10–12 are the stretch set; do them when 1–9 pass cold. Do not skip 10
if Amazon is your target.
