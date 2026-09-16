# 04 · Linked Lists

**In one sentence.** A linked list is a chain of boxes where each box holds a value and an arrow
to the next box, and every problem is about redrawing arrows without losing the chain.

**Why you care.** The LRU cache you build here sits inside Redis and every CDN. Git history is a
linked list of commits. Interview frequency is medium but concentrated: Reverse Linked List and
Merge Two Lists are warm-ups everywhere, and LRU Cache is one of the most asked Amazon problems.

## The idea, with a story

**A treasure hunt.** Clue 1 is taped under your pillow. It says "the next clue is in the fridge."
The fridge clue says "the next clue is in the mailbox." And so on. There is no map, so to read
clue 7 you must read clues 1 through 6. Now the important part: if you burn clue 3 before reading
it, clues 4 through 10 still exist, but you will never find them. That is what happens when you
overwrite a box's arrow before saving where it pointed.

**Reversing the hunt.** Standing at clue 3, you rewrite it to say "the next clue is where clue 2
was." But if you rewrite before reading where clue 4 lives, you are stuck. So: read the old arrow
and remember it, rewrite, step forward using what you remembered. Save, rewire, advance.

**A fake first clue.** The first clue lives in your head, not on paper, so deleting it works
differently from every other clue. Fix: tape a blank clue 0 to the wall saying only "clue 1 is
under the pillow." Now every real clue has a clue before it. That is the dummy head.

**Two runners.** Two friends start together on a path. One runs twice as fast. If the path has an
end, the fast one reaches it when the slow one is halfway. If the path is a loop, the fast one
eventually laps the slow one. So "did they meet?" answers "is there a loop?"

## The same story with numbers

A list is boxes with arrows. Each box holds a value and one arrow.

```
head
 |
 v
[1|•]-->[2|•]-->[3|•]-->None
```

**Reverse it.** Keep three fingers: `prev` (where I came from), `cur` (where I stand), and `nxt`
(a saved copy of where I was about to go).

```
start    prev=None  cur=1                1 --> 2 --> 3 --> None
step 1   nxt=2.  1's arrow -> None       None <-- 1     2 --> 3 --> None
step 2   nxt=3.  2's arrow -> 1          None <-- 1 <-- 2     3 --> None
step 3   nxt=None.  3's arrow -> 2       None <-- 1 <-- 2 <-- 3
         cur=None, stop. prev=3 is the new head.
```

**Find the middle** of `1→2→3→4→5` with two runners.

| turn | slow | fast |
|------|------|------|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |

Fast has no next box, so stop. Slow is on 3, the middle, without ever counting the length.

Pause and predict: in step 1 of the reversal, what happens if you set 1's arrow to None
*before* saving `nxt`?

<details><summary>Answer</summary>
You have no way to reach 2. Stepping forward gives None, the loop ends, and you return a
one-box list containing just 1. Boxes 2 and 3 still exist but nothing points at them. No error
message. This silence is the whole difficulty of the chapter.
</details>

## The anchor problem: Reverse Linked List

Given the head of a singly linked list, reverse it in place and return the new head.

```
before:  1 --> 2 --> 3 --> None
after:   3 --> 2 --> 1 --> None
```

**Brute force.** Copy values into a Python list, reverse it, rebuild. O(n) time, O(n) space. It
ignores the point of the question.

**Insight.** Walk the list once. At each node, point its arrow backward to the node you just left.
To keep walking after that, you must have saved the old arrow first.

```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next          # 1. save
        cur.next = prev         # 2. rewire
        prev = cur              # 3. advance both
        cur = nxt
    return prev                 # cur is None; prev is the last node visited
```

**Complexity.** O(n) time, O(1) space.

**What to say.** "I keep previous and current. At each node I save its next, point it back at
previous, and step both forward. When current runs off the end, previous is the new head. One
pass, constant space."

## Templates you memorize

The file `exercises.py` gives you `ListNode(val, next)`, plus `from_list` and `to_list` to build
and read lists in tests.

**Dummy head.** A fake node in front so the real head is never a special case.
```python
dummy = ListNode(0, head)
tail = dummy
while ...:
    tail.next = <chosen node>
    tail = tail.next
return dummy.next
```

**Fast and slow pointers.** Middle, cycle detection, and "n from the end" in one walk.
```python
slow = fast = head
while fast and fast.next:       # both checks, every time
    slow = slow.next
    fast = fast.next.next
# slow is the middle. If slow is fast inside the loop, there is a cycle.
```

**In-place reversal.** Save, rewire, advance. Learn it until your hands do it.
```python
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev, cur = cur, nxt
```

## When you see X, think Y

| You see | Think |
|---------|-------|
| "reverse", "in place", "O(1) space" | three-pointer reversal |
| "merge sorted lists" | dummy head, walk both, append the smaller |
| "middle", "half" | fast/slow |
| "cycle", "loop", "does it terminate" | fast/slow, they meet inside the loop |
| "nth from the end" in one pass | two pointers with a gap of n, start at a dummy |
| "array of n+1 values in 1..n, find the duplicate" | treat `i → nums[i]` as a list, find the cycle |
| "least recently used", "O(1) get and put" | dict plus doubly linked list with two sentinels |
| "k sorted lists" | min-heap of heads |

## Words you will hear

- **Node.** One box: a value plus an arrow. Here, `ListNode(val, next)`.
- **Head / tail.** The first box and the last box. The tail's arrow points to None.
- **Dummy head, sentinel.** The fake clue 0. Return `dummy.next` at the end.
- **In place.** Rewire the existing boxes. No new boxes, no copying into a Python list.
- **Fast and slow pointers.** The two runners.
- **Floyd's algorithm.** The formal name for "two runners, if they meet there is a loop."
- **Doubly linked.** Each box also has a `prev` arrow pointing backward. Needed for LRU Cache.

## Mistakes everyone makes once

- **Overwriting `next` before saving it.** The bug behind half of all linked list failures.
- **Forgetting to terminate.** After reordering, a node still points forward. Set its `next` to
  None or you get a cycle and an infinite loop with no error message.
- **Checking only `fast`.** Write `while fast and fast.next`. Otherwise `fast.next.next` crashes.
- **LRU Cache: evicting the node but not the dict key.** A stale entry stays behind and `get`
  happily returns it. Keep the key on the node so eviction can find it.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `reverse_list` | Easy | The anchor. Save, rewire, advance. |
| 2 | `merge_two_sorted` | Easy | Dummy head. Append the smaller head. Attach the leftover list at the end. |
| 3 | `middle_node` | Easy | Fast/slow. `while fast and fast.next`. |
| 4 | `has_cycle` | Easy | Fast/slow. Return True the moment `slow is fast`. |
| 5 | `remove_nth_from_end` | Medium | Dummy. Move `fast` n+1 steps, then both. `slow.next = slow.next.next`. |
| 6 | `add_two_numbers` | Medium | Walk both with a carry. `while l1 or l2 or carry`. |
| 7 | `reorder_list` | Medium | Find the first middle, cut, reverse the second half, interleave. |
| 8 | `copy_random_list` | Medium | Pass 1: dict old node to new node. Pass 2: wire `next` and `random` through it. |
| 9 | `find_duplicate_number` | Medium | `i → nums[i]` is a linked list. Find the cycle, then its entrance. |
| 10 | `LRUCache` | Medium | Dict plus doubly linked list with two sentinels. Key lives on the node. |
| 11 | `reverse_k_group` | Hard | Count k ahead. Reverse exactly k. Splice back with the nodes before and after. |
| 12 | `merge_k_sorted_lists` | Hard | Heap of `(val, i, node)`. Pop, append, push `node.next`. |

Start with 1 and 3 today. Do 2 to 9 over the week. Do 10 before 11 and 12 if Amazon is your target.
