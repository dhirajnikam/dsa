# Two pointers and windows

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Array indexing, hashing, and Big-O.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **pointer** here is an index. Two pointers can move inward from opposite ends or travel forward at different rates. The key is proving why discarded positions cannot contain a needed answer. Sorted input often provides that proof; unsorted input may not.

A **window** is a contiguous range with a summary such as a sum or character counts. In a fixed-size window, adding a new item and removing the outgoing item avoids recomputing the whole range. In a variable-size window, grow one boundary and shrink the other until the required condition holds.

Write the **invariant**: a sentence that must remain true, such as “the current window contains no repeated characters.” A repair may require several removals, not just one. Inclusive boundaries have length right − left + 1.

Total pointer movement determines complexity. If each moves forward at most n times and updates are constant time, nested-looking loops can still total O(n). Sum-threshold shrinking commonly requires positive numbers; negative values break its monotonic reasoning. That warning does not apply to every window algorithm—fixed-size rolling sums still work with negatives.

## Walk through a small example

For readings [5, 2, 6, 1] and a window of size 2, the first sum is 7. Shift once: remove 5 and add 6 to get 8. Shift again: remove 2 and add 1 to get 7. Three windows require visiting each entering/leaving value only once.

## Watch for

Shrinking once when several removals are needed; applying a positive-sum argument to negative input; assuming every two-pointer algorithm is linear without counting resets.

## Your next small step

Open [valid palindrome two pointers](problems/01_valid_palindrome_two_pointers.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 06/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Valid Palindrome](problems/01_valid_palindrome_two_pointers.py)
- [Two Sum II - Input Array Is Sorted](problems/02_two_sum_sorted.py)
- [3Sum](problems/03_three_sum.py)
- [Container With Most Water](problems/04_container_most_water.py)
- [Remove Duplicates from Sorted Array](problems/05_remove_duplicates_sorted.py)
- [Maximum Sum Subarray of Size K](problems/06_max_sum_subarray_size_k.py)
- [Longest Substring Without Repeating Characters](problems/07_longest_substring_no_repeat.py)
- [Minimum Size Subarray Sum](problems/08_min_size_subarray_sum.py)
- [Longest Repeating Character Replacement](problems/09_longest_repeating_char_replacement.py)
- [Minimum Window Substring](problems/10_minimum_window_substring.py)

</details>
