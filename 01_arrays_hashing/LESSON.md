# 01 · Arrays & Hashing

**In one sentence.** An array is a row of numbered boxes. A hash map is a row of boxes where the
thing you are looking for tells you which box to open, so you never have to search.

**Why you care.** This is the most asked interview category. Amazon phone screens open with it.
And it runs the real world: Google's search index, your Amazon cart, every cache you have ever
touched is a hash map.

## The idea, with a story

You are at a party with 50 people. Someone says: "find two people whose ages add up to 60."

The slow way: pick a person, ask everyone else their age, check for 60. Repeat for each person.
About 50 × 50 = 2,500 conversations.

The clever way: carry a notepad. Walk the room once. For each person, first check the notepad:
"have I already met someone aged 60 minus this age?" If yes, done. If no, write this age down and
keep walking. 50 conversations.

That notepad is a hash map. Writing in it is *insert*. Checking it is *lookup*. Both take one step
no matter how full the notepad gets. The whole chapter is variations on "carry a notepad so you
never re-walk the room."

## The same story with numbers

Numbers `[8, 3, 15, 7]`, target `10`. Notepad starts empty.

| Meet | I need | On the notepad? | Notepad after |
|------|--------|-----------------|---------------|
| 8 | 2 | no | {8} |
| 3 | 7 | no | {8, 3} |
| 15 | −5 | no | {8, 3, 15} |
| 7 | 3 | **yes** | found 3 and 7 |

Pause and predict: for `[1, 2, 4]` and target `6`, what is on the notepad when you meet the 4?

<details><summary>Answer</summary>
{1, 2}. You need 6 − 4 = 2. It is there. Pair found.
</details>

## The anchor problem: Two Sum

Given `nums` and `target`, return the two indices whose values add to `target`. Exactly one answer.

**Brute force.** Check every pair. O(n²). For 100,000 numbers that is 10 billion checks. Too slow.

**Insight.** At each number, I need `target - number`. If I have written every earlier number
and its index on a notepad, I can ask in one step.

```python
def two_sum(nums, target):
    seen = {}                        # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:       # check first ...
            return [seen[target - x], i]
        seen[x] = i                  # ... then record, so i is never paired with itself
    return []
```

**Complexity.** O(n) time, O(n) space. You spent memory to save time. Say that sentence out loud.

**What to say.** "Brute force is all pairs, O(n²). The repeated work is searching for the
complement, so I store each number in a hash map and look up the complement in O(1). One pass."

## Templates you memorize

**Count things.**
```python
from collections import Counter
counts = Counter(words)            # {"the": 2, "cat": 1}
counts.most_common(2)              # top two as (word, count)
```

**Group things that are "the same" under a rule.** Compute a label every group member shares.
```python
from collections import defaultdict
groups = defaultdict(list)
for w in words:
    groups[tuple(sorted(w))].append(w)    # anagrams share the sorted letters
```

**Running totals (prefix sums).** Sum of positions `i..j` is `total_up_to[j] - total_up_to[i-1]`.
Pair it with a notepad to count subarrays that sum to `k`:
```python
seen = {0: 1}; running = count = 0     # the empty prefix sums to 0
for x in nums:
    running += x
    count += seen.get(running - k, 0)
    seen[running] = seen.get(running, 0) + 1
```

**Best subarray ending here (Kadane).** Extend the run, or start fresh if it went negative.
```python
best = cur = nums[0]
for x in nums[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)
```

## When you see X, think Y

| You see | Think |
|---------|-------|
| "find a pair", "does X exist" | a set or dict of what you have seen |
| "count", "most frequent", "anagram" | `Counter` |
| "group by ..." | a shared label as the dict key |
| "subarray sum equals k" | prefix sums plus a dict |
| "maximum subarray" | Kadane |
| "consecutive numbers", unsorted | put everything in a set, count runs from their starts |
| "O(1) insert, delete, random" | list for random, dict for position, swap-with-last to delete |

## Words you will hear

- **Index.** The box number. Starts at 0.
- **Key / value.** What you look up by, and what you get back. `ages["Priya"] = 31`.
- **Set.** A notepad that only records *that* you saw something.
- **Hash function.** Turns a key into a box number. Built in. You never write one.
- **Collision.** Two keys land in the same box. Python handles it. Cost stays "average O(1)".
- **Subarray.** A contiguous slice, boxes next to each other.

## Mistakes everyone makes once

- **Writing before checking** in Two Sum pairs a number with itself. Check, then record.
- **Using a list as a dict key.** Lists can change, so they cannot be keys. Use `tuple(...)`.
- **Starting prefix sums with an empty dict** instead of `{0: 1}` misses subarrays from index 0.
- **Kadane with `max(0, cur + x)`** breaks when every number is negative. Use `max(x, cur + x)`.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `contains_duplicate` | Easy | A set of what you have seen. |
| 2 | `two_sum` | Easy | The anchor. Write it without looking. |
| 3 | `is_anagram` | Easy | Same letter counts. Compare lengths first. |
| 4 | `group_anagrams` | Medium | `tuple(sorted(word))` is the label. |
| 5 | `top_k_frequent` | Medium | Count, then bucket by count: `buckets[count].append(x)`. |
| 6 | `product_except_self` | Medium | One pass multiplying from the left, one from the right. |
| 7 | `max_subarray` | Medium | Kadane. |
| 8 | `subarray_sum_k` | Medium | Prefix sums with `seen = {0: 1}`. |
| 9 | `longest_consecutive` | Medium | Set. Only count up from `x` if `x - 1` is missing. |
| 10 | `encode` / `decode` | Medium | Prefix each string with its length and `#`. |
| 11 | `RandomizedSet` | Medium | List plus dict of value → index. Delete by swapping with the last. |
| 12 | `first_missing_positive` | Hard | Answer is in 1..n+1. Put value `v` at index `v-1`. |

Start with 1 and 2 today. Do 3 to 9 over the week. 10 to 12 are for when the first nine pass cold.
