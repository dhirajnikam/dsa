# 01 · Arrays & Hashing

> The hash map is the single most valuable tool in interviews. It turns "have I seen this
> before?" from a scan into a lookup. Most O(n²) → O(n) improvements in this chapter are
> exactly that trade: memory for time.

**Interview frequency:** highest of any category. Amazon phone screens open with these.
Google uses them as warm-ups before a harder follow-up.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

An array is a row of numbered boxes; a hash map is a row of boxes where the *thing you are
looking for* tells you which box to open, so you never have to search.

### Start with something you already do

You are at a party with 50 people. Someone says: "find two people whose ages add up to 60."

The slow way: pick person A, then walk to every other person and ask their age, checking if
it adds to 60. Then pick person B and do it again. For 50 people that is roughly 50 × 50 =
2,500 conversations. Exhausting.

The clever way: get a notepad. Walk through the room once. Each time you meet someone, first
check your notepad: "have I already written down someone aged 60 minus this person's age?" If
yes, done. If no, write this person's age and name on the notepad, and move on. You talk to
each person once. 50 conversations, not 2,500.

That notepad is a hash map. Writing in it is "insert." Checking it is "lookup." The whole
chapter is variations on "carry a notepad so you never re-walk the room."

### Now the same thing with numbers

Numbers: `[8, 3, 15, 7]`, target `10`. Walk through once, notepad starts empty.

| Meet | I need | Is it on the notepad? | Notepad after |
|------|--------|-----------------------|---------------|
| 8 | 10 − 8 = 2 | no | {8} |
| 3 | 10 − 3 = 7 | no | {8, 3} |
| 15 | 10 − 15 = −5 | no | {8, 3, 15} |
| 7 | 10 − 7 = 3 | **yes** | found: 3 and 7 |

Four steps for four numbers. Pause and predict: for `[1, 2, 4], 6`, what does the notepad
contain when you meet the 4, and do you find a pair?

<details><summary>Answer</summary>
Notepad is {1, 2}. You need 6 − 4 = 2, which is there. Pair found: 2 and 4.
</details>

### The words people use

- **Array / list.** A row of boxes numbered from 0. `nums[3]` means "the box at position 3."
  Opening a box by its number is instant.
- **Index.** The box number. Starts at 0, not 1. This trips everyone once.
- **Hash map / dict / dictionary.** The notepad. You store a *key* (what you look up by) with a
  *value* (what you want back). `ages["Priya"] = 31`. Looking up `ages["Priya"]` is instant.
- **Set.** A notepad that only records *that* you saw something, not any extra value. Perfect
  for "have I seen this before?"
- **Key.** The thing you look up by. Must be unchangeable (a number, a string, a tuple), because
  the map computes the box number from it once and expects it to stay put.
- **Hash function.** The machine that turns a key into a box number. You never write one; Python
  has it built in. You only need to know it exists and is fast.
- **Collision.** Two keys get the same box number. Python handles it; the cost stays near
  instant on average. Say "average O(1)" if asked.
- **O(1), O(n), O(n²).** How the work grows. O(1): the same no matter the size. O(n): doubles when
  the input doubles. O(n²): quadruples when the input doubles. See `00_foundations/LESSON.md`.
- **Prefix sum.** A running total. If you know the total up to position 5 and up to position 2,
  the sum of positions 3 to 5 is the difference. No re-adding.
- **Subarray.** A contiguous slice, boxes next to each other. `[3, 15]` is a subarray of
  `[8, 3, 15, 7]`. `[8, 15]` is not.

### Why the fast way is fast

For 10 people, the pair-checking way does about 100 checks, the notepad way about 10.
For 1,000 people: 1,000,000 vs 1,000. For 100,000 (a normal interview constraint):
10,000,000,000 vs 100,000. A computer does about 100,000,000 simple things a second, so the
slow way takes minutes and the fast way takes a millisecond. The interviewer knows this,
which is why they wrote the constraint. The constraint is a hint.

What did you pay? Memory. The notepad has to hold up to n entries. That is the trade in
this entire chapter: **spend memory to save time.** Say that sentence in the interview.

### Try it in your head

1. You have a list of 1,000 usernames and need to know if any name appears twice. Notepad or
   nested loop? What goes on the notepad?

<details><summary>Answer</summary>
Notepad (a set). Walk once; if a name is already in the set, it is a duplicate. What goes on
it: every name you have passed.
</details>

2. Group these words so that anagrams are together: `eat, tea, ant, tan`. What could you write
   on the notepad as the "label" that `eat` and `tea` share but `ant` does not?

<details><summary>Answer</summary>
The letters sorted: `eat` → `aet`, `tea` → `aet`, `ant` → `ant`, `tan` → `ant`. Same label,
same group. The label is the key; the group is the value.
</details>

3. Running totals of `[2, 4, 1, 3]` are `[2, 6, 7, 10]`. What is the sum of the middle two
   numbers, using only the running totals?

<details><summary>Answer</summary>
Total up to position 2 (7) minus total up to position 0 (2) = 5. Check: 4 + 1 = 5.
</details>

### Common confusions, cleared

- **"Isn't a dict just a list with names?"** A list finds things by *position*. A dict finds
  things by *content*. Asking a list "where is 7?" means checking every box. Asking a dict is
  one step.
- **"Why check the notepad before writing on it?"** If you write first, you find yourself. In
  the party story, you would "pair" a 30-year-old with themself. Check, then write.
- **"Do I need to know how hashing works inside?"** For the interview, one sentence is enough:
  "a hash function maps the key to a bucket index; collisions are handled with short chains;
  average O(1)." You will never be asked to implement it.

### What to do next

Open Part 2 below, read Part 2 §2 (Two Sum, fully worked) and notice it is the party story in code.
Then open `exercises.py` and do `contains_duplicate` and `two_sum` with a 30-minute timer.
When they pass, come back and read Part 2 §3 of the lesson: every pattern there is a different thing
to write on the notepad.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

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

### 1. The core idea

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

### 2. Anchor problem: Two Sum, fully worked

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

### 3. Patterns in this chapter

#### Counting with a dict or `Counter`

Anagram, frequency, "most common," "exactly k times." Build counts in one pass.
Two strings are anagrams iff `Counter(s) == Counter(t)`. For lowercase letters a fixed list of
26 ints is even faster and shows you know the alphabet is a constant.

#### Canonical keys for grouping

To group things that are "the same under some rule," compute a key that is identical for
every member of a group and use it as a dict key.

```python
groups = defaultdict(list)
for word in words:
    groups[tuple(sorted(word))].append(word)     # anagrams share a sorted key
```

A 26-count tuple is an O(k) key instead of the O(k log k) sort. Mention it as an upgrade.

#### Prefix sums

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

#### Prefix and suffix products

"Product of everything except me" without division: multiply a left-running product and a
right-running product into the same output array.

#### Kadane: the best subarray ending here

`best_ending_here = max(x, best_ending_here + x)`. If the running sum went negative, it can
only hurt, so start fresh. One pass, O(1) space. This is a one-dimensional DP in disguise.

#### Sets for O(1) membership

"Longest consecutive sequence": put all numbers in a set. Only start counting from numbers
that are the *start* of a run (`x - 1 not in nums_set`). Each number is visited O(1) times
in total, so the whole thing is O(n) even with a nested `while`.

#### Encoding with a length prefix

To join strings so they can be split back, prefix each with its length and a delimiter:
`"5#hello3#abc"`. The delimiter can appear inside strings safely because you read the
length first.

### 4. Recognition cues

| You see | Think |
|---------|-------|
| "find a pair / complement / does X exist" | hash set or map of what you have seen |
| "count", "frequency", "most common", "anagram" | `Counter` or 26-slot array |
| "group by ...", "same under rule R" | canonical key → `defaultdict(list)` |
| "subarray sum equals k", "range sum" | prefix sums, often plus a hash map |
| "maximum subarray" | Kadane |
| "consecutive", "sequence" with unsorted input | set, count runs from their starts |
| "O(1) insert, delete, and random" | list + dict of value → index, swap-with-last on delete |

### 5. Pitfalls

- **Recording before checking** in Two Sum reuses the same index. Check, then record.
- **Mutable keys.** Lists cannot be dict keys. Use `tuple(...)`.
- **`sorted(word)` as a key** costs O(k log k). Fine, but know the counting alternative.
- **Prefix sums with `seen = {}`** instead of `{0: 1}` misses subarrays starting at index 0.
- **Kadane with `max(0, ...)`** breaks on all-negative arrays. Use `max(x, running + x)`.
- **Hash map worst case.** Average O(1); say "average" if asked. Adversarial inputs can degrade
  it, which is why some interviewers ask for a sorting alternative too.

### 6. Exercises

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
