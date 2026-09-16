# 01 · Arrays & Hashing, explained from zero

Read this first if "hash map" sounds like a spell. When it makes sense, move to `LESSON.md`,
which is the reference you will come back to for years. This file is the conversation you
would have with a patient friend before opening the reference.

## In one sentence

An array is a row of numbered boxes; a hash map is a row of boxes where the *thing you are
looking for* tells you which box to open, so you never have to search.

## Start with something you already do

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

## Now the same thing with numbers

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

## The words people use

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
  the input doubles. O(n²): quadruples when the input doubles. See `00_foundations/THEORY.md`.
- **Prefix sum.** A running total. If you know the total up to position 5 and up to position 2,
  the sum of positions 3 to 5 is the difference. No re-adding.
- **Subarray.** A contiguous slice, boxes next to each other. `[3, 15]` is a subarray of
  `[8, 3, 15, 7]`. `[8, 15]` is not.

## Why the fast way is fast

For 10 people, the pair-checking way does about 100 checks, the notepad way about 10.
For 1,000 people: 1,000,000 vs 1,000. For 100,000 (a normal interview constraint):
10,000,000,000 vs 100,000. A computer does about 100,000,000 simple things a second, so the
slow way takes minutes and the fast way takes a millisecond. The interviewer knows this,
which is why they wrote the constraint. The constraint is a hint.

What did you pay? Memory. The notepad has to hold up to n entries. That is the trade in
this entire chapter: **spend memory to save time.** Say that sentence in the interview.

## Try it in your head

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

## Common confusions, cleared

- **"Isn't a dict just a list with names?"** A list finds things by *position*. A dict finds
  things by *content*. Asking a list "where is 7?" means checking every box. Asking a dict is
  one step.
- **"Why check the notepad before writing on it?"** If you write first, you find yourself. In
  the party story, you would "pair" a 30-year-old with themself. Check, then write.
- **"Do I need to know how hashing works inside?"** For the interview, one sentence is enough:
  "a hash function maps the key to a bucket index; collisions are handled with short chains;
  average O(1)." You will never be asked to implement it.

## What to do next

Open `LESSON.md`, read §2 (Two Sum, fully worked) and notice it is the party story in code.
Then open `exercises.py` and do `contains_duplicate` and `two_sum` with a 30-minute timer.
When they pass, come back and read §3 of the lesson: every pattern there is a different thing
to write on the notepad.
