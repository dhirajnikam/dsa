# Greedy: make a choice you can defend

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Sorting, array scans, and counterexamples.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **greedy algorithm** makes a local choice and commits to it. It is correct only if that choice can be part of an optimal result. A plausible rule is a hypothesis, not a proof.

An **exchange argument** shows that an optimal arrangement can be changed to include your choice without becoming worse. A **stays-ahead argument** shows that after each step your partial result is at least as promising as an alternative. Write the quantity you preserve, such as the farthest reachable boundary.

Sorting often exposes a useful order. Earliest finish, smallest requirement, and farthest reach suit different contracts. Local choices can fail when later consequences interact; DP keeps alternatives when a single commitment cannot be justified.

Boundary cases are especially valuable: one item, impossible progress, equal endpoints, and large later obstacles. Include sorting in complexity. Some tasks promise reachability; do not silently assume that promise in another question.

## Walk through a small example

Consider coin values 1, 3, 4 and a target of 6. Choosing the largest affordable coin first gives 4+1+1, while 3+3 uses fewer coins. This counterexample disproves that greedy rule for arbitrary coin systems. A rule needs a reason that applies to the specific problem.

## Watch for

Assuming a locally good choice is globally best; transferring a greedy rule to a different contract; forgetting impossible inputs when they are allowed.

## Your next small step

Open [jump game](problems/01_jump_game.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 15/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Jump Game](problems/01_jump_game.py)
- [Jump Game II](problems/02_jump_game_ii.py)
- [Gas Station](problems/03_gas_station.py)
- [Assign Cookies](problems/04_assign_cookies.py)
- [Partition Labels](problems/05_partition_labels.py)
- [Candy](problems/06_candy.py)
- [Minimum Number of Arrows to Burst Balloons](problems/07_min_arrows_burst_balloons.py)

</details>
