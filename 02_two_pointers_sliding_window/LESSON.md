# 02 · Two Pointers & Sliding Window

> Two indices moving through one array can replace a nested loop. The trick is always the
> same: prove that one move can never lose the answer, and then make that move. Every
> problem in this chapter is that proof in a different costume.

**Interview frequency:** very high. Amazon loves the string versions (longest substring,
minimum window). Google uses Trapping Rain Water and Sliding Window Maximum as second-half
follow-ups to warm-up questions.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

Instead of checking every pair with two nested loops, you keep two fingers on the list and
only ever move each finger forward, because the shape of the data tells you which move can
never lose the answer.

### Start with something you already do

**Two pointers.** A cinema has one long row of seats, priced cheapest at the left end and
most expensive at the right. You and a friend want two seats whose prices add to exactly 20.
You stand at the cheap end, your friend at the expensive end, and you both shout your prices.

- Total too small? Only you can fix it. Your friend already has the priciest seat there is.
  If your seat cannot reach 20 even with that partner, it cannot reach 20 with anyone. You
  step one seat inward and never look back.
- Total too big? Same logic in reverse. Your friend steps inward.

Every shout, exactly one of you steps toward the other. Nobody ever steps backward, so you
meet after walking the row once between you. That is two pointers on sorted data.

**Sliding window.** An inchworm crawls along a row of tiles. Its head stretches forward one
tile at a time. Its tail stays put until the body breaks some rule by getting too long, then
scoots forward until the rule holds again. The body always covers a contiguous strip. Neither
end ever moves backward, so each end visits every tile at most once: two walks of the row,
total, however often the tail has to scoot.

### Now the same thing with numbers

**Two pointers.** Sorted `[1, 3, 4, 6, 9]`, target 13.

| left | right | sum | verdict |
|------|-------|-----|---------|
| 1 | 9 | 10 | too small, left steps in |
| 3 | 9 | 12 | too small, left steps in |
| 4 | 9 | 13 | found: 4 and 9 |

Three steps for five numbers. Crossing off the 1 was safe because 9 is the biggest partner
the 1 could ever have, and even that was not enough.

**Sliding window.** Longest stretch of `abcab` with no repeated letter.

| head reads | window before | repeat? | tail scoots | window after | length |
|------------|---------------|---------|-------------|--------------|--------|
| a | | no | | a | 1 |
| b | a | no | | ab | 2 |
| c | ab | no | | abc | 3 |
| a | abc | yes | drop a | bca | 3 |
| b | bca | yes | drop b | cab | 3 |

Best length: 3. Pause and predict: for `abba`, what does the window look like right after
the head reads the second `b`?

<details><summary>Answer</summary>
Window was `ab`. Adding `b` makes `abb`, a repeat. The tail drops `a`: still `bb`, still a
repeat. The tail drops the first `b`: now just `b`. Two scoots for one arrival. That is why
the shrink is a `while`, not an `if`.
</details>

### The words people use

- **Pointer.** Here it just means an index: a finger on one position. Not the scary C kind.
  Usually named `l` and `r`, or `left` and `right`.
- **Opposite ends.** One finger starts at the front, one at the back, and they walk toward
  each other. Needs sorted data, or a rule where the smaller side decides.
- **Sliding window.** A contiguous slice from `left` to `right`. `right` grows it, `left`
  shrinks it, both only move forward.
- **Contiguous, subarray, substring.** Items next to each other with no gaps. A window is
  always contiguous.
- **Expand / shrink.** Move `right` forward (window grows). Move `left` forward (window
  shrinks).
- **Valid / invalid.** Whether the current window obeys the problem's rule. Shrink while
  invalid, then measure.
- **Monotone property.** "If this window breaks the rule, every bigger window containing it
  also breaks it." Only then is shrinking from the left guaranteed to help.
- **Fixed-size window.** The length `k` is given. One item in, one out, no `while` needed.
- **Variable-size window.** The length changes. You shrink with a `while` loop.
- **Read / write pointer.** Two fingers moving the same direction. `read` visits everything,
  `write` marks where the next kept item goes. For "remove in place."
- **In place.** Change the given list instead of building a new one.
- **Amortized.** Averaged over the whole run. A `while` inside a `for` looks like n², but
  `left` moves at most n times in total, so the real cost is about 2n.
- **Deque.** A "double-ended queue": add or remove at either end instantly. Used for the
  window-maximum problem.
- **Monotonic deque.** A deque kept in decreasing order. When a bigger number arrives, older
  smaller numbers are thrown out because they can never be the maximum again.
- **Running minimum, "min so far."** One number you update as you walk. Best Time to Buy
  Stock is nothing more than that.

### Why the fast way is fast

Checking every pair means about n × n ÷ 2 checks. Two fingers moving inward means at most n
steps. A window means at most 2n steps.

| n | every pair | two pointers | window |
|---|------------|--------------|--------|
| 10 | 45 | 10 | 20 |
| 1,000 | 500,000 | 1,000 | 2,000 |
| 100,000 | 5,000,000,000 | 100,000 | 200,000 |

At roughly 100,000,000 simple steps a second, the pair method takes about a minute on the
last row. The pointers take a millisecond.

What did you pay? For opposite ends, the data must be sorted. If it is not, sorting first
costs O(n log n), and that is the price. In return you use no extra memory at all, which is
why interviewers prefer this to the Chapter 01 notepad whenever the input arrives sorted. A
window carries a small notepad (a set or a count table) sized to the alphabet, not the input.

### Try it in your head

1. Sorted `[2, 5, 8, 11]`, target 16. Trace the two fingers.

<details><summary>Answer</summary>
2 + 11 = 13, too small, left steps to 5. 5 + 11 = 16, found. Two steps.
</details>

2. Maximum sum of any 3 consecutive numbers in `[4, 1, 7, 2, 9]`. After adding up the first
   window, how many arithmetic operations does each slide cost?

<details><summary>Answer</summary>
First window 4 + 1 + 7 = 12. Slide: add 2, drop 4, giving 10. Slide: add 9, drop 1, giving
18. Each slide is one add and one subtract, never a fresh sum of three. Answer 18.
</details>

3. Heights `[1, 8, 6, 2, 5, 4, 8, 3, 7]`, Container With Most Water. Fingers on 1 and 7.
   Which one moves, and why?

<details><summary>Answer</summary>
The finger on 1 moves. Water height is capped by the shorter wall. Keeping the 1 and moving
the 7 inward can only make the container narrower with the same cap, so the 1 is finished.
</details>

### Common confusions, cleared

- **"But what if the answer was behind the finger I just moved?"** Prove that it cannot be.
  When the sum with the biggest possible partner is still too small, no partner works. Say
  that sentence out loud before you type the move.
- **"A `while` inside a `for` is n²."** Only if the inner loop can restart from the beginning.
  Here `left` never goes backward, so over the entire run it takes at most n steps. Count
  moves, not loop nestings.
- **"Why `while` to shrink? One removal should fix it."** In `abba`, one removal left the
  window still broken. Shrink while broken, not once.
- **"When do I record the window length?"** Longest problems: after shrinking, when the window
  is valid. Shortest problems: inside the shrink loop, while the window is still valid.

### What to do next

Open Part 2 below and read Part 2 §1 (the core idea) and Part 2 §2 (Valid Palindrome, fully worked). The
"why is the skip safe" sentence there is the cinema row. Then open `exercises.py` and do
`two_sum_sorted` and `longest_substring_no_repeat` with a 30-minute timer each. When both
pass, do `remove_duplicates_sorted` to meet the read/write flavor, then read Part 2 §3 for the rest.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** Amazon Kinesis and every stream-processing system compute
"events in the last five minutes" with a sliding window: new events enter on the right, old ones
expire on the left, and nobody recounts the whole stream. A rate limiter that allows 100 requests
per minute is a window over timestamps. Log analysis tools that find "the busiest ten-second span"
are Sliding Window Maximum with a different label. And when a database merges two sorted runs
during a sort or a join, it walks two pointers down two lists and always takes the smaller head.
The pattern is small. It is everywhere.

**The analogy.** Two people walk toward each other down a hallway, each checking doors. Neither
ever checks a door the other has already passed, and they stop when they meet. That is the
opposite-ends flavor. The sliding window is a caterpillar: the front inches forward, and the back
only catches up when the body gets too long. Neither end ever moves backward. Hold on to that
image, because it is the whole reason the method is fast.

**How it works, in plain words.** A nested loop checks every pair, and most pairs are hopeless.
Two pointers use structure, usually sorted order or the fact that a window only changes at its
ends, to throw away whole families of pairs in one move. If the sum is too small, the left number
can never work with anything to its right, so cross it off and never look back. Each pointer
moves in one direction only, so the total number of moves is at most twice the length of the
input. That is why a `while` inside a `for` here is O(n), not O(n²).

**What learning this will feel like.** The code is short. The doubt is not. You will write
`l += 1` and think "but what if the answer was back there?" That doubt is the actual content of
this chapter, and it is healthy. The aha comes when you can finish the sentence "moving this
pointer is safe because..." out loud, first for Container With Most Water and then for Three Sum,
and realise the sentence *is* the solution. Expect one bug to bite: shrinking a window with `if`
instead of `while`, so one removal leaves the window still invalid. It fails on Longest Substring
Without Repeating Characters in a way you will remember, and then never repeat.

**You will know you have it when** you see "longest substring such that" and your first thought
is not a loop but the question "what makes a window invalid, and does shrinking from the left
always fix it?"

### 1. The core idea

A nested loop tries every pair `(i, j)`. That is O(n²) pairs. Two pointers walks through the
same pairs but *skips* most of them, because it knows in advance they cannot beat what it
has. The knowledge comes from structure: sorted order, or the fact that a window's property
only changes at its two ends.

There are two flavors:

- **Opposite ends.** `left = 0`, `right = n - 1`. Each step moves one pointer inward.
  Works when the input is sorted or when a pair's value depends on the smaller end.
- **Sliding window (same direction).** Both pointers start at 0. `right` expands, and
  `left` shrinks only while the window is invalid. Works for "contiguous subarray/substring
  with property P."

```
brute force (every pair)             opposite ends
for i in range(n):                   l, r = 0, n - 1
    for j in range(i+1, n):          while l < r:
        if a[i] + a[j] == t: ...         s = a[l] + a[r]
                                         if s == t: return
                                         if s < t: l += 1    # need bigger, only l can help
                                         else:     r -= 1    # need smaller, only r can help
O(n²) time                            O(n) time, O(1) space
```

Why is the skip safe? In the sorted case, if `a[l] + a[r] < t`, then `a[l] + a[anything <= r]`
is also `< t`, so no pair using `l` can ever work. Cross `l` off forever. That single sentence
is the entire justification, and you should say it out loud.

For windows, the cue is different: **each pointer moves only forward, so the total number of
moves is at most 2n.** A `while` inside a `for` looks like O(n²), but it is O(n). Interviewers
test whether you know why.

### 2. Anchor problem: Valid Palindrome, fully worked

**Problem.** Given a string, decide whether it reads the same forwards and backwards after
you drop every non-alphanumeric character and ignore case.

**Understand.** Is an empty string a palindrome? Yes (conventionally). Spaces and punctuation
are skipped, not compared. Digits count as characters. Can I allocate a cleaned copy? That
gives O(n) space; the interviewer will want O(1), so plan for two pointers on the original.

**Examples.** `"A man, a plan, a canal: Panama" → True`. `"race a car" → False`.
`" " → True` (nothing left to compare). `"0P" → False` (digit vs letter, case-insensitive
does not rescue it).

**Brute force.** Build `cleaned = [c.lower() for c in s if c.isalnum()]` and compare it with
its reverse. O(n) time, O(n) space. Correct and short. Say it, then improve the space.

**Insight.** Compare the outermost characters, then move inward. Skip anything that is not
alphanumeric before each comparison. No copy is needed.

**Code.**

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

**Test.** `"race a car"`: l=0 'r', r=9 'r' ✓ → l=1 'a', r=8 'a' ✓ → l=2 'c', r=7 'c' ✓ →
l=3 'e', r=6 ' ' skip → r=5 'a'. 'e' != 'a' → `False`. ✓

`" "`: l=0, r=0, loop never runs → `True`. ✓

**Complexity.** O(n) time. Each pointer moves only inward, so at most n moves in total.
O(1) extra space.

**What to say out loud.** "Cleaning into a new string and reversing works in O(n) time but
also O(n) space. I can avoid the copy with two pointers from the ends, skipping
non-alphanumerics as I go. Every step moves a pointer inward, so it is O(n) time and O(1)
space."

### 3. Patterns & templates in this chapter

#### Opposite-ends two pointers (sorted input)

```python
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s == target:
        return [l, r]
    if s < target:
        l += 1              # the sum is too small; only a bigger left can fix it
    else:
        r -= 1
```

The move is safe because sorted order lets you discard one endpoint with certainty. Three Sum
is this template inside a `for` loop over the first element, with duplicate skipping.

#### Two pointers where the smaller side decides

```python
l, r, best = 0, len(h) - 1, 0
while l < r:
    best = max(best, (r - l) * min(h[l], h[r]))
    if h[l] < h[r]:
        l += 1              # the shorter wall limits the area; moving the taller one cannot help
    else:
        r -= 1
```

Container With Most Water. The argument: with the shorter wall fixed, any narrower container
using that wall is worse, so that wall is done. Trapping Rain Water uses the same idea with
running maxima on each side.

#### Slow/fast writer pointer (in-place compaction)

```python
write = 1                                 # first element always stays
for read in range(1, len(nums)):
    if nums[read] != nums[write - 1]:
        nums[write] = nums[read]
        write += 1
return write
```

`read` visits every element; `write` marks where the next kept element goes. Remove
duplicates, move zeros, remove element: all the same shape.

#### Variable-size sliding window

```python
left = 0
state = {}                                # counts, or a set, or a running sum
for right in range(len(s)):
    add(s[right], state)                  # expand
    while invalid(state):                 # shrink only while the window breaks the rule
        remove(s[left], state)
        left += 1
    best = max(best, right - left + 1)    # window [left, right] is valid here
```

Use for "longest substring/subarray such that P," where P is *monotone*: if a window
violates P, every wider window containing it also violates P. Then shrinking from the left
is always the right response. For "shortest window such that P" (Minimum Window Substring),
flip it: shrink *while valid* and record the best inside the shrink loop.

#### Fixed-size sliding window

```python
k = len(pattern)
for right in range(len(s)):
    add(s[right], state)
    if right >= k:
        remove(s[right - k], state)       # keep exactly k elements
    if right >= k - 1 and matches(state):
        return True
```

Use when the window length is given. Permutation in String, "max sum of k consecutive," and
every "average of each window" problem. No `while` needed: one in, one out.

#### Monotonic deque for window max

```python
dq = deque()                              # indices; values are decreasing front to back
for i, x in enumerate(nums):
    while dq and nums[dq[-1]] <= x:
        dq.pop()                          # x makes older, smaller values useless forever
    dq.append(i)
    if dq[0] <= i - k:
        dq.popleft()                      # front has slid out of the window
    if i >= k - 1:
        out.append(nums[dq[0]])           # front is the window max
```

An element smaller than a newer one can never be the maximum of any future window. Drop it.
This is a monotonic stack that also loses elements at the front; Chapter 03 makes the stack
version the main event.

### 4. Recognition cues

| You see | Think |
|---------|-------|
| sorted array, "pair with sum," "closest to target" | opposite-ends two pointers |
| "triplets," "unique combinations sum to 0" | sort, fix one, two pointers on the rest, skip duplicates |
| "area between two lines," "walls," "container" | opposite ends, move the shorter side |
| "trapped water," "bounded on both sides" | two pointers with running left max and right max |
| "longest substring/subarray with property" | variable window, shrink while invalid |
| "shortest window containing" | variable window, shrink while valid and record |
| "permutation / anagram of s1 appears in s2," "every window of size k" | fixed window, one in and one out |
| "maximum of each window" | monotonic deque |
| "in place," "return the new length" | slow writer, fast reader |
| "buy low, sell high," "min so far" | one pass tracking the running minimum |

### 5. Pitfalls

- **Forgetting `l < r` inside inner skip loops** in Valid Palindrome. `"  "` will run off
  the end without it.
- **Skipping duplicates incorrectly in Three Sum.** Skip a repeated first element *before*
  the inner loop, and skip repeated `l` and `r` values *after* recording a triplet, not before.
- **Shrinking the window with `if` instead of `while`.** One removal may not restore
  validity. Always `while invalid`.
- **Measuring the window at the wrong time.** In "longest" problems, measure after the shrink
  loop when the window is valid. In "shortest" problems, measure inside the shrink loop.
- **Longest Repeating Character Replacement:** the window is valid iff
  `window_len - max_count <= k`. People try to recompute `max_count` after shrinking. You do
  not have to: a stale, too-high `max_count` can only keep a window that was already the
  right size, so the answer is still correct.
- **Off-by-one in fixed windows.** The window `[right - k + 1, right]` is complete when
  `right >= k - 1`. Remove `s[right - k]`, not `s[right - k + 1]`.
- **Deque stores indices, not values.** You need the index to know when the front expires.
- **Rain water on a single side.** Water at `i` is `min(max_left, max_right) - h[i]`.
  Missing either side gives wrong answers on `[4, 2, 0, 3, 2, 5]`.

### 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|----------|-----------|----------|----------|
| 1 | `valid_palindrome` | Easy | Amazon, Google | The anchor above. Skip non-alphanumerics inside the loop. |
| 2 | `two_sum_sorted` | Easy | Amazon | Opposite ends. Sum too small → `l += 1`. Return 1-based. |
| 3 | `remove_duplicates_sorted` | Easy | Amazon, Google | Slow writer pointer. Compare to `nums[write - 1]`. |
| 4 | `best_time_stock` | Easy | Amazon, Google | Track the minimum price so far; profit is `price - min_so_far`. |
| 5 | `three_sum` | Medium | Amazon, Google | Sort. For each `i` (skip repeats), two pointers on `i+1..n-1`. |
| 6 | `container_most_water` | Medium | Amazon, Google | Move the pointer at the shorter wall. Say why. |
| 7 | `longest_substring_no_repeat` | Medium | Amazon, Google | Variable window with a set. Shrink while `s[right]` is already in it. |
| 8 | `longest_repeating_char_replacement` | Medium | Google, Amazon | Valid iff `window - max_count <= k`. Do not recompute max on shrink. |
| 9 | `check_permutation_in_string` | Medium | Amazon | Fixed window of size `len(s1)`. Compare 26 counts. |
| 10 | `min_window_substring` | Hard | Amazon, Google | Track `have` vs `need` distinct letters. Shrink while `have == need`. |
| 11 | `trapping_rain_water` | Hard | Amazon, Google | Two pointers with `left_max` and `right_max`. Process the side with the smaller max. |
| 12 | `sliding_window_maximum` | Hard | Amazon, Google | Deque of indices, decreasing values. Pop front when it leaves the window. |

Solve 1–9 in order. 10–12 are the stretch set; do them when 1–9 pass cold.
