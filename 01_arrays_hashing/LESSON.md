# 01 · Arrays & Hashing

*New to this topic? Read `THEORY.md` in this folder first. It explains the idea from zero.*

> The hash map is the single most valuable tool in interviews. It turns "have I seen this
> before?" from a scan into a lookup. Most O(n²) → O(n) improvements in this chapter are
> exactly that trade: memory for time.

**Interview frequency:** highest of any category. Amazon phone screens open with these.
Google uses them as warm-ups before a harder follow-up.

## 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** A hash map is the most used data structure on Earth.
Google's search index is, at its heart, a giant map from word to the list of pages containing
it. Amazon looks up your cart by your user ID in a hash-backed store. Every cache, every
session table, every "have I seen this request before" check is a hash map. When you use a
dictionary in this chapter, you are using the same idea that runs the internet, at a smaller
scale.

**The analogy.** A coat check. You hand over your coat and get ticket 47. Later you say "47"
and get your coat back instantly. Nobody searches the rack. The ticket number *is* the
location. A hash function does the same for any key: it turns `"banana"` into a slot number,
and the value sits in that slot. That is why lookup is O(1): you compute where to look
instead of searching.

**How it works, in plain words.** The array underneath has, say, 1000 slots. `hash("banana")`
gives a big integer; take it modulo 1000 and you have a slot. Two keys sometimes land in the
same slot (a collision), so each slot holds a short list and Python checks that list. As the
map fills up, Python doubles the array and rehashes, keeping the lists short. Average cost:
constant. That is the entire magic trick, and now you can explain it if an interviewer asks
"how does a dict actually work?"

**What learning this will feel like.** The first time you turn a nested loop into a single
pass with a dictionary, it will feel like cheating. It is not. That feeling is your brain
noticing that you traded memory for time, and it is exactly the feeling you are trying to
make automatic. Expect one specific frustration: recording a value *before* checking for its
partner, which makes Two Sum use the same index twice. Everyone does it once. After that
you will never do it again, because the bug is memorable, and memorable bugs are how patterns
stick.

**You will know you have it when** the phrase "is X in this collection?" inside a loop makes
your hand reach for a set before your brain finishes the sentence.

## 1. The core idea

An array gives you O(1) access *by position*. A hash map (Python `dict`) gives you O(1) access
*by value*. When a brute force repeatedly asks "does the array contain X?" or "where is X?",
replace that scan with a dictionary lookup.

The recognition cue: **a nested loop where the inner loop is a search.**

```
brute force                          hashed
for i in range(n):                   seen = {}
    for j in range(i+1, n):          for i, x in enumerate(nums):
        if nums[j] == target - nums[i]   if target - x in seen: ...
                                         seen[x] = i
O(n²) time, O(1) space               O(n) time, O(n) space
```

## 2. Anchor problem: Two Sum, fully worked

**Problem.** Given `nums` and `target`, return indices `[i, j]` with `nums[i] + nums[j] == target`.
Exactly one answer exists. You may not use the same element twice.

**Understand.** Indices, not values. Exactly one solution, so no need to handle "none" or
"multiple." Can numbers be negative? Yes. Duplicates? Yes, e.g. `[3, 3], 6`.

**Examples.** `[2, 7, 11, 15], 9 → [0, 1]`. `[3, 3], 6 → [0, 1]`. `[3, 2, 4], 6 → [1, 2]` (note:
using index 0 twice would wrongly give 6; this is why the "same element" rule matters).

**Brute force.** Every pair. O(n²) time, O(1) space. Say it, then move on.

**Insight.** At index `i`, I need `target - nums[i]`. If I have already recorded every earlier
number with its index, I can ask the dictionary in O(1). One pass.

**Code.**

```python
def two_sum(nums, target):
    seen = {}                        # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i                  # record AFTER checking: prevents using i twice
    return []
```

**Test.** `[3, 2, 4], 6`: i=0 x=3 need=3, not in {} → seen={3:0}. i=1 x=2 need=4, no → seen={3:0,2:1}.
i=2 x=4 need=2, yes → `[1, 2]`. ✓

**Complexity.** O(n) time, O(n) space.

**What to say out loud.** "The brute force checks all pairs in O(n²). The repeated work is
searching for the complement, so I store each number's index in a hash map as I go and look
up the complement in O(1). One pass, O(n) time and space."

## 3. Patterns in this chapter

### Counting with a dict or `Counter`

Anagram, frequency, "most common," "exactly k times." Build counts in one pass.
Two strings are anagrams iff `Counter(s) == Counter(t)`. For lowercase letters a fixed list of
26 ints is even faster and shows you know the alphabet is a constant.

### Canonical keys for grouping

To group things that are "the same under some rule," compute a key that is identical for
every member of a group and use it as a dict key.

```python
groups = defaultdict(list)
for word in words:
    groups[tuple(sorted(word))].append(word)     # anagrams share a sorted key
```

A 26-count tuple is an O(k) key instead of the O(k log k) sort. Mention it as an upgrade.

### Prefix sums

`prefix[i] = nums[0] + ... + nums[i-1]`. Then any range sum is `prefix[j] - prefix[i]` in O(1).
Combine with a hash map to count subarrays with a given sum: at each position, ask how many
earlier prefixes equal `current_prefix - k`.

```python
count = 0; prefix = 0; seen = {0: 1}     # empty prefix has sum 0, once
for x in nums:
    prefix += x
    count += seen.get(prefix - k, 0)
    seen[prefix] = seen.get(prefix, 0) + 1
```

### Prefix and suffix products

"Product of everything except me" without division: multiply a left-running product and a
right-running product into the same output array.

### Kadane: the best subarray ending here

`best_ending_here = max(x, best_ending_here + x)`. If the running sum went negative, it can
only hurt, so start fresh. One pass, O(1) space. This is a one-dimensional DP in disguise.

### Sets for O(1) membership

"Longest consecutive sequence": put all numbers in a set. Only start counting from numbers
that are the *start* of a run (`x - 1 not in nums_set`). Each number is visited O(1) times
in total, so the whole thing is O(n) even with a nested `while`.

### Encoding with a length prefix

To join strings so they can be split back, prefix each with its length and a delimiter:
`"5#hello3#abc"`. The delimiter can appear inside strings safely because you read the
length first.

## 4. Recognition cues

| You see | Think |
|---------|-------|
| "find a pair / complement / does X exist" | hash set or map of what you have seen |
| "count", "frequency", "most common", "anagram" | `Counter` or 26-slot array |
| "group by ...", "same under rule R" | canonical key → `defaultdict(list)` |
| "subarray sum equals k", "range sum" | prefix sums, often plus a hash map |
| "maximum subarray" | Kadane |
| "consecutive", "sequence" with unsorted input | set, count runs from their starts |
| "O(1) insert, delete, and random" | list + dict of value → index, swap-with-last on delete |

## 5. Pitfalls

- **Recording before checking** in Two Sum reuses the same index. Check, then record.
- **Mutable keys.** Lists cannot be dict keys. Use `tuple(...)`.
- **`sorted(word)` as a key** costs O(k log k). Fine, but know the counting alternative.
- **Prefix sums with `seen = {}`** instead of `{0: 1}` misses subarrays starting at index 0.
- **Kadane with `max(0, ...)`** breaks on all-negative arrays. Use `max(x, running + x)`.
- **Hash map worst case.** Average O(1); say "average" if asked. Adversarial inputs can degrade
  it, which is why some interviewers ask for a sorting alternative too.

## 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|----------|-----------|----------|----------|
| 1 | `contains_duplicate` | Easy | Amazon, Google | `len(set(nums)) < len(nums)`, or a running set. |
| 2 | `two_sum` | Easy | Everyone | The anchor above. Write it without looking. |
| 3 | `is_anagram` | Easy | Amazon | Counts must match. Lengths first as a fast reject. |
| 4 | `group_anagrams` | Medium | Amazon, Google | `tuple(sorted(w))` is the key. |
| 5 | `top_k_frequent` | Medium | Amazon, Google | Count, then bucket by frequency: `buckets[count].append(x)`. O(n). |
| 6 | `product_except_self` | Medium | Amazon, Google | Left pass writes prefix products; right pass multiplies suffix products in. |
| 7 | `max_subarray` | Medium | Amazon, Google | Kadane. Best ending here vs. start over at x. |
| 8 | `subarray_sum_k` | Medium | Google, Amazon | Prefix sums plus `seen = {0: 1}`. |
| 9 | `longest_consecutive` | Medium | Google | Set. Only count up from `x` if `x - 1` is absent. |
| 10 | `encode` / `decode` | Medium | Google | Length prefix and `#`. `decode` reads digits until `#`. |
| 11 | `RandomizedSet` | Medium | Amazon | List for O(1) random; dict value → index; delete by swapping with the last element. |
| 12 | `first_missing_positive` | Hard | Amazon, Google | Answer is in 1..n+1. Use the array itself as the hash: put value v at index v-1. |

Solve 1–9 in order. 10–12 are the stretch set; do them when 1–9 pass cold.
