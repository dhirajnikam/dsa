# 02 · Two Pointers & Sliding Window

**In one sentence.** Instead of checking every pair with two nested loops, you keep two fingers
on the list and only ever move each finger forward, because the shape of the data tells you which
move can never lose the answer.

**Why you care.** Every "events in the last five minutes" system, every rate limiter, and every
database merge is one of these two tricks. Interview frequency is very high. Amazon loves the
string versions. Google uses the hard ones as second-half follow-ups.

## The idea, with a story

**Two pointers.** A cinema has one long row of seats, priced cheapest at the left end and most
expensive at the right. You and a friend want two seats whose prices add to exactly 20. You stand
at the cheap end, your friend at the expensive end, and you both shout your prices.

Total too small? Only you can fix it. Your friend already has the priciest seat there is. If your
seat cannot reach 20 even with that partner, it cannot reach 20 with anyone. You step one seat
inward and never look back. Total too big? Your friend steps inward.

Every shout, exactly one of you steps toward the other. Nobody ever steps backward, so you meet
after walking the row once between you.

**Sliding window.** An inchworm crawls along a row of tiles. Its head stretches forward one tile
at a time. Its tail stays put until the body breaks some rule by getting too long, then scoots
forward until the rule holds again. Neither end ever moves backward, so each end visits every tile
at most once.

## The same story with numbers

**Two pointers.** Sorted `[1, 3, 4, 6, 9]`, target 13.

| left | right | sum | verdict |
|------|-------|-----|---------|
| 1 | 9 | 10 | too small, left steps in |
| 3 | 9 | 12 | too small, left steps in |
| 4 | 9 | 13 | found: 4 and 9 |

Crossing off the 1 was safe because 9 is the biggest partner the 1 could ever have.

**Sliding window.** Longest stretch of `abcab` with no repeated letter.

| head reads | window before | repeat? | window after | length |
|------------|---------------|---------|--------------|--------|
| a | | no | a | 1 |
| b | a | no | ab | 2 |
| c | ab | no | abc | 3 |
| a | abc | yes, drop a | bca | 3 |
| b | bca | yes, drop b | cab | 3 |

Best length: 3.

Pause and predict: for `abba`, what does the window look like right after the head reads the
second `b`?

<details><summary>Answer</summary>
Window was `ab`. Adding `b` makes `abb`, a repeat. The tail drops `a`: still `bb`, still a
repeat. The tail drops the first `b`: now just `b`. Two scoots for one arrival. That is why
the shrink is a <code>while</code>, not an <code>if</code>.
</details>

## The anchor problem: Valid Palindrome

Given a string, decide whether it reads the same forwards and backwards after dropping every
non-alphanumeric character and ignoring case. `"race a car"` is `False`. `" "` is `True`.

**Brute force.** Build a cleaned lowercase copy and compare it with its reverse. O(n) time, O(n)
space.

**Insight.** Compare the outermost characters, then move inward. Skip junk before each comparison.
No copy is needed.

```python
def valid_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1                            # skip junk from the left
        while l < r and not s[r].isalnum():
            r -= 1                            # skip junk from the right
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
```

**Complexity.** O(n) time, O(1) space. Each pointer only moves inward, so at most n moves total.

**What to say.** "Cleaning into a new string and reversing works in O(n) space. I can avoid the
copy with two pointers from the ends, skipping non-alphanumerics as I go. O(n) time, O(1) space."

## Templates you memorize

**Opposite ends on sorted input.** Too small, move left. Too big, move right.
```python
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s == target:
        return [l, r]
    if s < target:
        l += 1              # only a bigger left can fix a small sum
    else:
        r -= 1
```

**Variable-size window.** Expand with `right`. Shrink with `left` only while the window breaks the
rule. Measure when it is valid.
```python
left = 0
for right in range(len(s)):
    add(s[right])                          # expand
    while invalid():                       # shrink while broken, not once
        remove(s[left])
        left += 1
    best = max(best, right - left + 1)     # window [left, right] is valid here
```

**Fixed-size window.** Length `k` is given. One in, one out. No `while` needed.
```python
for right in range(len(s)):
    add(s[right])
    if right >= k:
        remove(s[right - k])               # keep exactly k elements
    if right >= k - 1 and matches():
        return True
```

**Read/write pointer for in-place removal.** `read` visits everything. `write` marks where the next
kept item goes.
```python
write = 1                                  # first element always stays
for read in range(1, len(nums)):
    if nums[read] != nums[write - 1]:
        nums[write] = nums[read]
        write += 1
return write
```

## When you see X, think Y

| You see | Think |
|---------|-------|
| sorted array, "pair with sum" | opposite-ends two pointers |
| "triplets that sum to 0" | sort, fix one, two pointers on the rest, skip duplicates |
| "container", "walls", "area between lines" | opposite ends, move the shorter side |
| "trapped water" | two pointers with a running max on each side |
| "longest substring with property" | variable window, shrink while invalid |
| "shortest window containing" | variable window, shrink while valid and record inside |
| "anagram of s1 in s2", "every window of size k" | fixed window, one in and one out |
| "maximum of each window" | deque of indices, kept decreasing |

## Words you will hear

- **Pointer.** Just an index. A finger on one position. Usually named `l` and `r`.
- **Window.** A contiguous slice from `left` to `right`. Both ends only move forward.
- **Contiguous, subarray, substring.** Items next to each other with no gaps.
- **Expand / shrink.** Move `right` forward. Move `left` forward.
- **Monotone property.** "If this window breaks the rule, every bigger window containing it also
  breaks it." Only then does shrinking from the left always help.
- **Amortized.** Averaged over the whole run. A `while` inside a `for` looks like n², but `left`
  moves at most n times in total, so the real cost is about 2n.
- **Deque.** Double-ended queue. Add or remove at either end in one step.

## Mistakes everyone makes once

- **Shrinking with `if` instead of `while`.** One removal may leave the window still broken.
  `abba` proves it.
- **Forgetting `l < r` inside the skip loops** in Valid Palindrome. `"  "` runs off the end.
- **Measuring at the wrong time.** Longest problems: after the shrink loop. Shortest problems:
  inside the shrink loop, while still valid.
- **Off-by-one in fixed windows.** Remove `s[right - k]`, not `s[right - k + 1]`. The first full
  window appears when `right == k - 1`.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `valid_palindrome` | Easy | The anchor. Skip non-alphanumerics inside the loop. |
| 2 | `two_sum_sorted` | Easy | Opposite ends. Sum too small, `l += 1`. Return 1-based. |
| 3 | `remove_duplicates_sorted` | Easy | Read/write pointer. Compare to `nums[write - 1]`. |
| 4 | `best_time_stock` | Easy | Track the minimum price so far. Profit is `price - min_so_far`. |
| 5 | `three_sum` | Medium | Sort. For each `i` (skip repeats), two pointers on the rest. |
| 6 | `container_most_water` | Medium | Move the pointer at the shorter wall. Say why. |
| 7 | `longest_substring_no_repeat` | Medium | Variable window with a set. Shrink while `s[right]` is in it. |
| 8 | `longest_repeating_char_replacement` | Medium | Valid iff `window - max_count <= k`. No need to recompute max on shrink. |
| 9 | `check_permutation_in_string` | Medium | Fixed window of size `len(s1)`. Compare 26 counts. |
| 10 | `min_window_substring` | Hard | Track `have` vs `need`. Shrink while `have == need`, record inside. |
| 11 | `trapping_rain_water` | Hard | Two pointers with `left_max` and `right_max`. Process the smaller side. |
| 12 | `sliding_window_maximum` | Hard | Deque of indices, decreasing values. Pop front when it leaves the window. |

Start with 1, 2, and 7 today. Do 3 to 9 over the week. 10 to 12 are for when the first nine pass cold.
