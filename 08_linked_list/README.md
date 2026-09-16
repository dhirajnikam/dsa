# Linked lists: preserve the next connection

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Object references and classes from chapter 01; loops and hashing.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **node** holds a value and a reference to the next node. A linked list begins at a head reference and ends at None. Unlike an array, finding the kth node requires following links, so access is O(n). Insertion beside a known node can be constant time, but finding that node is a separate cost.

Changing a link can make the rest of a list unreachable. Before rewiring, name the parts you still need. A dummy/sentinel node can make changes at the head follow the same rule as changes in the middle.

Two traversal references can move at different speeds or keep a fixed gap. In a cycle, neither reaches None. State which middle to return for an even-length list and how n is counted from the end.

Merging and reordering operate on node identity as well as values. Digit lists require handling carry after both inputs finish. An LRU cache combines a dictionary for lookup and an ordered linked structure for recency; “recently used” includes operations specified by the contract.

## Walk through a small example

Suppose head references node P, whose next is Q, whose next is R. If P.next is replaced before Q is saved anywhere, traversal from P can lose access to Q and R. Draw the three nodes and give the old next reference a temporary name before moving any connection.

## Watch for

Losing the rest of the list while rewiring; dereferencing None; comparing values when node identity matters; ignoring changes to the head.

## Your next small step

Open [reverse linked list](problems/01_reverse_linked_list.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 08/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Reverse Linked List](problems/01_reverse_linked_list.py)
- [Middle of the Linked List](problems/02_middle_of_list.py)
- [Merge Two Sorted Lists](problems/03_merge_two_sorted_lists.py)
- [Linked List Cycle](problems/04_linked_list_cycle.py)
- [Remove Nth Node From End of List](problems/05_remove_nth_from_end.py)
- [Reorder List](problems/06_reorder_list.py)
- [Add Two Numbers](problems/07_add_two_numbers.py)
- [LRU Cache](problems/08_lru_cache.py)

</details>
