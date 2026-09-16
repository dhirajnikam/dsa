# 04 · Linked Lists

> A linked list is the simplest structure that can hurt you. There is no index, only a chain
> of `next` pointers, and the moment you overwrite one before saving where it pointed, a piece
> of the list is gone forever. This chapter is about the discipline that prevents that.

**Interview frequency:** medium, but concentrated. Reverse Linked List and Merge Two Lists
are warm-ups everywhere. LRU Cache is one of the most asked Amazon problems, period. Google
uses Reverse in k-Groups and Copy List with Random Pointer to test pointer care under pressure.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

A linked list is a chain of boxes where each box holds a value and the location of the next
box, so you can only reach box 7 by walking through boxes 1 to 6, and every problem is about
redrawing arrows without losing the chain.

### Start with something you already do

**A treasure hunt.** Clue 1 is taped under your pillow. It says "the next clue is in the
fridge." The fridge clue says "the next clue is in the mailbox." And so on. There is no map,
so to read clue 7 you must read clues 1 through 6. Now the important part: if you burn clue 3
before reading it, clues 4 through 10 still exist, but you will never find them. That is what
happens when you overwrite a box's arrow before saving where it pointed.

**Reversing the hunt.** Standing at clue 3, you rewrite it to say "the next clue is where
clue 2 was." But if you rewrite before reading where clue 4 lives, you are stuck. So: read
the old arrow and remember it, rewrite, step forward using what you remembered. Save,
rewire, advance.

**A fake first clue.** The first clue is awkward. It lives in your head, not on paper, so
deleting it or inserting before it works differently from every other clue. Fix: tape a
blank clue 0 to the wall saying only "clue 1 is under the pillow." Now every real clue has a
clue before it, and none is special. That is the dummy head.

**Two runners.** Two friends start together on a path. One runs twice as fast. If the path
has an end, the fast one reaches it when the slow one is halfway. If the path is a loop, the
fast one eventually laps the slow one and they stand on the same spot, which never happens on
a path with an end. So "did they meet?" answers "is there a loop?"

### Now the same thing with numbers

A list is drawn as boxes with arrows. Each box holds a value and one arrow.

```
head
 |
 v
[1|•]-->[2|•]-->[3|•]-->None
```

**Reverse it.** Keep three fingers: `prev` (where I came from), `cur` (where I stand), and
`nxt` (a saved copy of where I was about to go).

```
start    prev=None  cur=1                1 --> 2 --> 3 --> None
step 1   nxt=2.  1's arrow -> None       None <-- 1     2 --> 3 --> None
         prev=1  cur=2
step 2   nxt=3.  2's arrow -> 1          None <-- 1 <-- 2     3 --> None
         prev=2  cur=3
step 3   nxt=None.  3's arrow -> 2       None <-- 1 <-- 2 <-- 3
         prev=3  cur=None   stop. prev is the new head.
```

Pause and predict: in step 1, what happens if you set 1's arrow to None *before* saving
`nxt`?

<details><summary>Answer</summary>
You have no way to reach 2. Stepping forward gives None, the loop ends, and you return a
one-box list containing just 1. Boxes 2 and 3 still exist but nothing points at them. No
error message. This silence is the whole difficulty of the chapter.
</details>

**Find the middle** of `1→2→3→4→5` with two runners.

| turn | slow | fast |
|------|------|------|
| 0 | 1 | 1 |
| 1 | 2 | 3 |
| 2 | 3 | 5 |

Fast has no next box, so stop. Slow is on 3, the middle, found without ever counting the
length.

### The words people use

- **Node.** One box: a value plus an arrow. In this repo, `ListNode(val, next)`.
- **Pointer / reference.** The arrow. In Python it is simply a variable that holds a node.
  `cur.next` means "the arrow out of the box I am standing at."
- **Head.** The first box. The list is nothing more than an arrow to it. Lose the head, lose
  the list.
- **Tail.** The last box. Its arrow points to None.
- **None.** The "no next clue" marker. Every proper list ends in it.
- **Singly / doubly linked.** Arrows go one way only, or each box also has a `prev` arrow
  pointing backward. A music player's next and previous buttons are a doubly linked list.
- **Dummy head, sentinel.** The fake clue 0. A throwaway box in front of the real head so the
  first box is not a special case. You return `dummy.next` at the end.
- **In place.** Rewire the existing boxes. No new boxes, no copying values into a Python list.
- **Traverse, walk.** Follow arrows from head to tail: `while cur: cur = cur.next`.
- **Fast and slow pointers.** The two runners. Finds the middle, detects loops, and reaches
  "n from the end" in one walk.
- **Floyd's algorithm.** The formal name for "two runners, if they meet there is a loop."
- **Cycle.** A box whose arrow points back to an earlier box. Walking never ends.
- **Splice.** Cut a segment out of the chain, change it, and reconnect both ends.
- **Carry.** In Add Two Numbers, the 1 you carry when two digits sum to 10 or more.
- **Deep copy.** A full duplicate where new boxes point only at other new boxes.
- **LRU cache.** "Least recently used." A fixed-size store that throws out the item you
  touched longest ago. Built from a dict plus a doubly linked list.

### Why the fast way is fast

This chapter's trade is not "slow versus fast." It is "which operation do you need fast?"

| operation | array (row of boxes) | linked list (chain) |
|-----------|----------------------|---------------------|
| open box number 7 | 1 step | 7 steps |
| insert at the front | shift everything: n steps | redraw 2 arrows |
| delete the box you stand at | shift everything after it | redraw 1 arrow |

For n = 10, 1,000 and 100,000, a front insert into an array costs 10, 1,000 and 100,000
shifts. Into a chain it costs 2, 2 and 2 arrow changes. Reading position k is the mirror
image: instant for the array, k steps for the chain.

So you reach for a chain when you constantly insert and delete in the middle and rarely jump
to a numbered position. The LRU cache is exactly that: every access moves one item to the
front and eviction removes the item at the back, two arrows each.

Reversal costs one walk of n steps using three variables. Copying values into a Python list
also costs n steps, but needs n extra memory and dodges the skill being tested.

### Try it in your head

1. Reverse `1→2`. Trace `prev` and `cur` after each step.

<details><summary>Answer</summary>
nxt=2, 1's arrow to None, prev=1, cur=2. Then nxt=None, 2's arrow to 1, prev=2, cur=None.
Return prev, which is 2. List reads 2→1.
</details>

2. Two runners on `1→2→3→4`. Where does slow stop?

<details><summary>Answer</summary>
Slow visits 1, 2, 3. Fast visits 1, 3, then has no next box. Slow stops on 3, the second of
the two middles. If a problem wants the first middle (2), start fast one box ahead.
</details>

3. Remove the first box from `5→6→7`. What is awkward without a dummy, and what changes with
   one?

<details><summary>Answer</summary>
Without: no box comes before 5, so "point the previous box past this one" has nothing to
point from, and you need a separate `head = head.next` case. With a dummy in front,
`dummy.next = dummy.next.next` removes 5 with the same line that removes any other box.
</details>

### Common confusions, cleared

- **"Why not copy everything into a Python list and reverse that?"** It works and costs n
  extra memory. The interviewer is testing whether you can rewire arrows safely. Mention the
  copy in one sentence, then do it in place.
- **"My code hangs forever with no error."** You made a loop, almost certainly by forgetting
  to set the old head's arrow to None after reversing, or by overwriting an arrow before
  saving it. Draw the boxes after each step and the loop shows up immediately.
- **"Why check both `fast` and `fast.next`?"** The fast runner takes two steps at once. If
  `fast.next` is None, asking for `fast.next.next` crashes. Check both, every time.
- **"Could the fast runner jump over the slow one in a loop?"** No. Each turn the gap between
  them shrinks by exactly one box. From a gap of k it reaches zero after k turns and never
  skips past it.

### What to do next

Open Part 2 below and read Part 2 §2 (Reverse Linked List, fully worked) with paper in hand, redrawing
the boxes after every line. Then open `exercises.py` and do `reverse_list` and `middle_node`
with a 30-minute timer each. When both pass, do `merge_two_sorted` to meet the dummy head,
then read Part 2 §3 for the patterns you will reuse on everything else.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

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

### 1. The core idea

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

### 2. Anchor problem: Reverse Linked List, fully worked

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

### 3. Patterns & templates in this chapter

#### Dummy head

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

#### Fast and slow pointers

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

#### Floyd on an array (Find the Duplicate Number)

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

#### In-place reversal of a segment

Reverse k Groups and Reorder List both reverse part of a list and splice it back. Steps:

1. Find the node *before* the segment (`prev_group`) and the node *after* it (`next_group`).
2. Reverse the segment with the three-pointer loop, stopping at `next_group`.
3. `prev_group.next` = new segment head; segment tail `.next = next_group`.

Draw the four boundary pointers before you write a line.

#### Doubly linked list + dict (LRU Cache)

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

#### Merge with a heap (previews Chapter 07)

Merging k sorted lists: push `(val, list_index, node)` for each head into a heap. Pop the
smallest, append to the output, push that node's `next`. O(N log k) for N total nodes. The
`list_index` breaks ties so nodes are never compared directly.

### 4. Recognition cues

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

### 5. Pitfalls

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

### 6. Exercises

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
