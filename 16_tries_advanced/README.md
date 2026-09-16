# Advanced structures: return here when needed

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Hashing, trees, heaps, windows, and bit operations. Optional after the first lap.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

A **trie** shares prefixes of strings in a tree of character edges. A terminal marker distinguishes a complete stored word from a prefix. Inserting or looking up a word visits O(L) characters, while total memory reflects stored prefixes and representation overhead. Wildcard search may branch; it is not always O(L).

A **monotonic deque** retains candidates for a sliding-window extremum, removing expired positions and candidates dominated by newer ones. Keep indices so expiry can be checked even for duplicate values.

A **Fenwick tree** or **segment tree** maintains range information while values change. Static prefix sums give fast queries but costly updates; these structures trade some simplicity for logarithmic updates and queries. State whether an update replaces a value or adds a delta.

A binary trie can compare bit prefixes for XOR choices. Fix the assumptions about sign and bit width before using a bitwise model. Counting bits can also reuse smaller-number facts.

An LFU cache evicts by use frequency and needs a tie-breaker for equally frequent keys. This differs from LRU, which tracks recency alone. Multiple structures must agree about membership, count, and ordering after every operation.

## Walk through a small example

Insert the words “car” and “cart” conceptually. Their first three edges are shared. The node after r must be marked as a complete word, even though another edge leads to t. Searching for “ca” reaches a valid prefix but not a complete stored word.

## Watch for

Confusing a prefix with a complete word; claiming wildcard lookup is always linear; retaining expired deque items; confusing update values with deltas; missing cache tie-breakers.

## Your next small step

Open [implement trie](problems/01_implement_trie.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 16/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Implement Trie (Prefix Tree)](problems/01_implement_trie.py)
- [Word Search II](problems/02_word_search_ii.py)
- [Design Add and Search Words Data Structure](problems/03_design_add_search_words.py)
- [Sliding Window Maximum](problems/04_sliding_window_maximum.py)
- [Range Sum Query - Mutable](problems/05_range_sum_query_mutable.py)
- [Maximum XOR of Two Numbers in an Array](problems/06_maximum_xor_two_numbers.py)
- [Counting Bits](problems/07_counting_bits.py)
- [LFU Cache](problems/08_lfu_cache.py)

</details>
