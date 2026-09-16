# 09 · Recursion & Backtracking, explained from zero

Read this first if "backtracking" sounds like a dance move and `path.pop()` looks like a typo.
When the wardrobe below makes sense, move to `LESSON.md`, the dense reference. This file is
the conversation with a patient friend before you open the reference.

## In one sentence

Backtracking is trying every option one decision at a time, and whenever a choice leads
nowhere, putting it back and trying the next one.

## Start with something you already do

You want to see *every* outfit you could wear. Three shirts, two trousers, two pairs of shoes.

You do not spread all twelve outfits on the bed. You put on shirt 1, trousers 1, shoes 1.
Look in the mirror, write it down. Take the shoes off, put shoes 2 on. Write it down. Out of
shoes, so take them off, take off trousers 1, put on trousers 2, and start again with shoes
1. Out of trousers, swap the shirt and repeat the whole thing.

Notice the rhythm. Put something on. Go deeper. Take it off. Try the next thing. "Take it
off" is the backtrack. In code it is `path.pop()`: putting the item back on the shelf so the
next choice starts clean.

Now a rule: the red shirt clashes with the green trousers. You put on the red shirt, reach for
the green trousers, and stop. You skip both pairs of shoes for that combination because you
can already see it fails. That is *pruning*: not entering a corridor you can see is blocked.

Same story as a maze. At every fork, take the first corridor. At a dead end, walk back to the
last fork and take the next one. The corridors you have walked so far are your `path` list.
Walking back is popping.

## Now the same thing with numbers

Find every subset of `[1, 2]`, including "nothing" and "both." At each number, one decision:
take it or skip it.

```
                     start: []
                   /            \
             take 1              skip 1
              [1]                  []
            /     \              /     \
       take 2    skip 2     take 2    skip 2
       [1, 2]      [1]        [2]        []
```

The bottom row is the four subsets. The walk goes left first, all the way down, then back up
one step, then the next branch.

| Step | Action | `path` now |
|------|--------|------------|
| 1 | take 1 | [1] |
| 2 | take 2 | [1, 2] → record |
| 3 | put 2 back | [1] |
| 4 | skip 2 | [1] → record |
| 5 | put 1 back | [] |
| 6 | skip 1, take 2 | [2] → record |
| 7 | put 2 back | [] |
| 8 | skip 2 | [] → record |

Every "take" is matched by a "put back," so `path` is always exactly what it was when control
returns to a fork. Pause and predict: for `[1, 2, 3]`, how many boxes in the bottom row, and
how many rows of decisions?

<details><summary>Answer</summary>
Eight boxes, three rows. Each number doubles the count: 2 × 2 × 2 = 8. That is 2ⁿ, which is
why the answer is exponential no matter how clever you are.
</details>

## The words people use

- **Recursion.** A function that calls itself on a smaller version of the problem. See
  `00_foundations/THEORY.md` for the staircase picture.
- **Backtracking.** Recursion where you make a choice, go deeper, then undo the choice and
  try the next.
- **Decision tree.** The picture above. Each fork is one choice; each bottom box is a finished
  candidate.
- **Leaf.** A bottom box. A complete answer, or a dead end.
- **Path.** The choices made so far, from the top of the tree to where you stand. The outfit
  you currently have on.
- **Choose / explore / un-choose.** The three lines at the heart of every solution: append to
  path, recurse, pop from path.
- **`path[:]`.** A copy of the path. You record a copy at the leaf because the original keeps
  changing.
- **Pruning.** Skipping a branch you can already see will fail. The red-shirt rule.
- **Constraint.** The rule that lets you prune. "Sum must not exceed 7."
- **Goal.** The condition that says "this is a finished answer, record it and turn back."
- **State.** Everything the function needs to know where it is: current index, path, what is
  still available.
- **Subset.** Any selection from a list, order ignored. `[1, 3]` equals `[3, 1]`.
- **Permutation.** An ordering. `[1, 3]` and `[3, 1]` are different.
- **Combination.** A subset of a fixed size. "Choose 2 of 4."
- **Power set.** All subsets. 2ⁿ of them.
- **Start index.** For subsets and combinations: only look at items *after* the one you just
  took, so you never build the same set in two orders.
- **Used array.** For permutations: a checklist of what is already on the path, so you never
  wear the same shirt twice.
- **Duplicate skip.** Sort the input, then at one fork never try a value equal to the one you
  just finished. Prevents identical answers when the input has repeats.
- **Enumeration.** Listing every candidate. Backtracking is enumeration with pruning.
- **n! ("n factorial").** n × (n−1) × ... × 1. The number of orderings of n things.

## Why the fast way is fast

Honestly, there is no fast way, and that is the point. If the problem asks for *all* subsets,
the answer itself has 2ⁿ lists. You cannot print a million lists in fewer than a million steps.

| n | Subsets (2ⁿ) | Orderings (n!) |
|---|-------------|----------------|
| 10 | 1,024 | 3,628,800 |
| 20 | about 1,000,000 | about 2.4 × 10¹⁸ |
| 1,000 | more than atoms in the universe | do not ask |

So `n ≤ 20` is the interviewer whispering "just try everything, and do it tidily." `n ≤
100,000` says the opposite, and you belong in chapter 10 or earlier.

The trade-off here is not speed for memory. It is *blind* enumeration versus *pruned*
enumeration. Generating every string of 8 brackets and filtering the balanced ones means 256
candidates. Building only prefixes that could still balance visits 14 leaves. Pruning does
not change the Big-O, but it often decides whether you finish in time.

## Try it in your head

1. Permutations of `[a, b, c]`. How many leaves, and how many choices at the second row?

<details><summary>Answer</summary>
Six leaves: 3 × 2 × 1. Two choices at the second row, because one letter is already on the
path and marked used.
</details>

2. Combinations summing to 7 from `[2, 3, 5]`, and your path is `[2, 3]` with sum 5. Which
   next choices can you prune?

<details><summary>Answer</summary>
Adding 5 gives 10, prune. Adding 3 gives 8, prune. Adding 2 gives 7, a goal. With a sorted
list you can stop the loop at the first overshoot, since every later value is bigger.
</details>

3. Someone writes `out.append(path)` instead of `out.append(path[:])`. What does `out` hold?

<details><summary>Answer</summary>
Many references to the *same* list, which is empty at the end because every append was
popped. Every entry looks like `[]`. The copy freezes a snapshot.
</details>

## Common confusions, cleared

- **"How can `path.pop()` undo anything? The call below already used it."** The call below
  appended and popped in matched pairs, so it handed `path` back exactly as received. Your pop
  removes only the item *you* added. Trace the table once with a pen and the mystery ends.
- **"Isn't O(2ⁿ) just wrong?"** Not when the output has 2ⁿ items. The complexity is the size
  of the answer. Say it without apologising, and add that pruning trims the constant.
- **"Subsets and permutations look the same. Why different tricks?"** Subsets ignore order,
  so you only look forward with a start index. Permutations care about order, so every unused
  item is a candidate at every row, and you need a used checklist instead.
- **"Why sort before skipping duplicates?"** The skip compares each value to the one right
  before it. That only catches repeats if equal values sit side by side.

## What to do next

Open `LESSON.md` and read §2, Subsets worked three ways, with the tree above next to you. Way
3 is the template you will reuse everywhere. Then open `exercises.py` and do `subsets` and
`permutations` with a timer. When they pass, read the universal template at the top of §3 and
notice both exercises were that template with different blanks.
