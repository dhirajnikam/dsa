# 02 · Two Pointers & Sliding Window, explained from zero

Read this first if "two pointers" sounds like a dance move and "sliding window" sounds like
a home repair. When it makes sense, open `LESSON.md`, the dense reference you will come back
to. This file is the patient conversation before it.

## In one sentence

Instead of checking every pair with two nested loops, you keep two fingers on the list and
only ever move each finger forward, because the shape of the data tells you which move can
never lose the answer.

## Start with something you already do

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

## Now the same thing with numbers

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

## The words people use

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

## Why the fast way is fast

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

## Try it in your head

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

## Common confusions, cleared

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

## What to do next

Open `LESSON.md` and read §1 (the core idea) and §2 (Valid Palindrome, fully worked). The
"why is the skip safe" sentence there is the cinema row. Then open `exercises.py` and do
`two_sum_sorted` and `longest_substring_no_repeat` with a 30-minute timer each. When both
pass, do `remove_duplicates_sorted` to meet the read/write flavor, then read §3 for the rest.
