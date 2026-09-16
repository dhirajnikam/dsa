# 04 · Linked Lists, explained from zero

Read this first if "pointer" makes you nervous and "reverse a linked list" sounds like a
hazing ritual. When it makes sense, open `LESSON.md`, the dense reference. This file is the
patient conversation before it, and it wants you to have paper and a pen nearby.

## In one sentence

A linked list is a chain of boxes where each box holds a value and the location of the next
box, so you can only reach box 7 by walking through boxes 1 to 6, and every problem is about
redrawing arrows without losing the chain.

## Start with something you already do

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

## Now the same thing with numbers

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

## The words people use

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

## Why the fast way is fast

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

## Try it in your head

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

## Common confusions, cleared

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

## What to do next

Open `LESSON.md` and read §2 (Reverse Linked List, fully worked) with paper in hand, redrawing
the boxes after every line. Then open `exercises.py` and do `reverse_list` and `middle_node`
with a 30-minute timer each. When both pass, do `merge_two_sorted` to meet the dummy head,
then read §3 for the patterns you will reuse on everything else.
