# Stacks and queues: choose the next item

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Lists, loops, and the idea of an invariant.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **stack** serves the most recently added item first (LIFO), like undo history. A **queue** serves the oldest item first (FIFO), like waiting customers. A Python list works well as a stack at its end. A deque supports efficient queue removal from the front.

Stacks help with nested structure: the most recent unmatched opening must be resolved first. An expression evaluator similarly keeps unfinished values until an operation can combine them. A minimum stack needs enough additional information to answer the minimum after a pop, including duplicate minima.

A **monotonic stack** keeps values in an ordered relation. An incoming item resolves some waiting items and removes them. Even if one arrival triggers many removals, each item is pushed and popped at most once; this is an amortized O(n) argument over the full scan.

Queues can be implemented with two stacks by transferring items in batches. Parsing nested encoded text needs both the repeated content and the surrounding unfinished context. Collision and histogram problems require careful rules about which pending items remain relevant.

## Walk through a small example

An undo stack receives actions A, B, C; undo removes C first. A queue receiving the same arrivals serves A first. Now imagine waiting temperatures 20, 18, then 23: the final arrival can resolve more than one earlier “waiting for warmer” question. Store positions if you need distances.

## Watch for

Using list.pop(0) for a large queue; storing only values when the answer needs indices; discarding duplicate minima; assuming many pops for one item imply quadratic total work.

## Your next small step

Open [valid parentheses](problems/01_valid_parentheses.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 07/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Valid Parentheses](problems/01_valid_parentheses.py)
- [Min Stack](problems/02_min_stack.py)
- [Evaluate Reverse Polish Notation](problems/03_evaluate_rpn.py)
- [Daily Temperatures](problems/04_daily_temperatures.py)
- [Next Greater Element I](problems/05_next_greater_element.py)
- [Implement Queue using Stacks](problems/06_queue_using_stacks.py)
- [Decode String](problems/07_decode_string.py)
- [Asteroid Collision](problems/08_asteroid_collision.py)
- [Largest Rectangle in Histogram](problems/09_largest_rectangle_histogram.py)

</details>
