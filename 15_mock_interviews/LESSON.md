# 15 · Mock Interviews & the Plan

**In one sentence.** A mock interview is a full-length rehearsal with the timer, the talking,
and the being-watched all switched on, so that none of the three is new on the day.

**Why you care.** This chapter is for everyone, from week 1 to the night before the loop. It
decides whether twelve weeks of preparation survives the first three minutes of a real round.
The biggest reason prepared candidates fail is the gap between solving at a desk and solving
while a stranger watches and a clock runs.

## The idea, with a story

You learn to drive. You read the handbook, pass the written test, know every rule. Then you
sit in the car with an examiner in the passenger seat, pull up to the first traffic light, and
stall. Twice.

You did not forget how a clutch works. Three new loads landed at once: someone is watching,
the light is about to change, and the examiner just asked you to say out loud what you are
checking in your mirrors. Each one eats a slice of attention, and attention is what you were
using to drive.

The fix is not more handbook. It is the empty parking lot on a Sunday, where you practice
until the clutch costs no thought, then add a passenger, then a stopwatch. Mocks are the empty
parking lot. Chapters 1 to 12 were learning the rules. This chapter is driving with a person
in the seat.

An interview asks four things at once: solve the problem, talk while you do it, watch the
clock, and be observed. Mocks make the last three automatic.

## The same story with numbers

A coding round is 45 minutes. Introductions and your questions eat a few, so the usable
budget is about 40. Spend it like this.

| Minutes | Phase | What you produce | The failure if you skip it |
|---------|-------|------------------|----------------------------|
| 0–5 | Clarify and examples | Restated problem, 2 examples, 1 edge case, written down | Solving the wrong problem for 30 minutes |
| 5–10 | Brute force and complexity | A correct slow approach and its O(), said aloud | Nothing on the board if the clever idea never comes |
| 10–15 | Optimize and get buy-in | The pattern, the better O(), a one-line plan, a nod | Coding an approach they already know is wrong |
| 15–35 | Code | Clean, named, narrated code | Running out of time with half a function |
| 35–42 | Test by hand | A line-by-line trace of one example, one edge case | The interviewer finds your bug and grades it |
| 42–45 | Complexity and follow-ups | Time and space, unprompted | Ending on silence |

Still designing at minute 20? Say so, pick the best approach you have, and code it. A working
O(n log n) beats an imagined O(n).

Pause and predict: at minute 12 you go silent for 90 seconds, staring at the screen and
thinking hard. What does the interviewer write down?

<details><summary>Answer</summary>
"Long silence; unclear whether stuck or thinking." Ninety seconds of good thinking scores the
same as ninety seconds of panic if none of it is spoken. The fix is one sentence: "I am
thinking about how to handle duplicates." Now the silence has a label.
</details>

## The out-loud script

"Think out loud" means narrating decisions and questions, not reading your code aloud. You
do not need to improvise. These are the sentences.

| Phase | What you literally say |
|-------|------------------------|
| Clarify | "Let me make sure I understand. We are given ___ and need to return ___. Is that right?" "Can the input be empty? Negative? Duplicates? How large can n be?" "Let me write two examples and an edge case." |
| Brute force | "The brute force is to ___, which is O(___). That works but is too slow for n up to 10^5." "The repeated work is ___." |
| Optimize | "That repeated work looks like a ___ problem, so I will ___. That brings it to O(___)." "Before I code, does this approach look right to you?" |
| If pushed back | "Good point. Let me think about the case where ___." Never defend an approach you have been told is wrong. |
| Code | "I will write a helper for ___ so the main loop stays readable." "I am using a dict from value to index because ___." "Wait, this breaks when ___. Let me fix that." |
| Silent over 30 seconds | "I am thinking about how to handle ___." |
| Test | "Let me trace this on the example. i=0, x=3, seen is empty, so seen becomes {3: 0}. i=1, ..." Actually write the values. "Now the edge case: empty input." |
| Wrap | "Time is O(___) because ___. Space is O(___) because ___." "If this were called a million times on the same array, I would precompute ___." "Is there a follow-up you would like me to look at?" |

The size question tells you the target: n ≤ 20 hints at exponential, n ≤ 10^5 means
O(n log n) or better. Finding your own bug while writing is a positive signal.

## What they write down

Knowing the rubric changes how you spend your minutes.

| Company | Axis | Lean Hire | Strong Hire |
|---------|------|-----------|-------------|
| Google | Algorithms | Working solution with hints | Optimal approach unprompted, with an alternative discussed |
| Google | Coding | Correct after a bug or two caught in testing | Clean and correct on first pass, edge cases in the code |
| Google | Communication | Explained when asked, some silence | Narrated continuously, checked in before coding, adjusted to hints |
| Google | Problem solving | Needed the brute force pointed out | Found it fast, named the repeated work, derived the optimization |
| Amazon | Working code | Correct on the main case after fixes | Correct including edge cases, tested before they asked |
| Amazon | Complexity | Stated when asked | Stated unprompted for brute force and final |
| Amazon | Handling hints | Took the hint and moved | Said what the hint changed, then finished cleanly |
| Amazon | Leadership Principles | Some evidence in the 15 to 25 minutes of questions | Specific stories with numbers, from chapter 14 |

At Google, a committee that never met you reads all the packets, and two "No Hire" ratings
usually end it. A silent, correct solution can score Hire on algorithms and No Hire on
communication in the same round. At Amazon, a coding round with no Leadership Principle
evidence is graded as incomplete even if the code passed.

## Six timed mock sets

Three problems per set, 45 minutes each on a timer, out loud. Solve from the chapter's
exercise file with the lesson closed. Afterward ask: did I *recognize* the pattern in the
first five minutes, or find it by trial? Solved without recognition goes on the redo list.

| Set | Problem 1 | Problem 2 | Problem 3 |
|-----|-----------|-----------|-----------|
| 1 · Phone screen, Amazon | `01_arrays_hashing` `two_sum` | `03_stack_queue` `valid_parentheses` | `05_binary_search` `search_rotated` |
| 2 · Phone screen, Google | `04_linked_list` `reverse_list` | `02_two_pointers_sliding_window` `longest_substring_no_repeat` | `08_graphs` `num_islands` |
| 3 · Onsite, data structures | `07_heaps` `kth_largest` | `03_stack_queue` `daily_temperatures` | `04_linked_list` `LRUCache` |
| 4 · Onsite, recursion | `12_tries_unionfind_bits` `single_number` | `09_recursion_backtracking` `subsets` | `10_dynamic_programming` `coin_change` |
| 5 · Onsite, graphs and intervals | `11_greedy_intervals` `merge_intervals` | `08_graphs` `rotting_oranges` | `08_graphs` `alien_dictionary` |
| 6 · Onsite, hard-ish | `01_arrays_hashing` `product_except_self` | `10_dynamic_programming` `word_break` | `02_two_pointers_sliding_window` `trapping_rain_water` |

With a friend: give them the problem and solution the day before. They answer clarifying
questions honestly, give one hint after two minutes of silence, and take notes. Alone: a
45-minute timer and a phone camera pointed at your screen, with you asking "does this look
right?" and answering as the interviewer would. Watch it back at 1.5× speed.

Score each mock from 1 to 3 on ten rows: clarified, wrote examples, stated brute force with
its O(), got buy-in, correct code, readable code, traced by hand, stated complexity
unprompted, no silence over 30 seconds, finished in time. Hireable is 24 or more with no 1s.
Fix the two lowest rows, not everything.

## The 12-week calendar

Assumes 1.5 to 2 hours a day. "Coding" means one problem, 30-minute timer, out loud, tests,
redo list.

| Week | Chapters | Weekdays, per day | Weekend |
|------|----------|-------------------|---------|
| 1 | 00 Foundations | 60 min reading and Python drills, 30 min Big-O | Read this chapter. Start `redo.txt`. |
| 2 | 01 Arrays & Hashing | 90 min coding | Redo list. No mock yet. |
| 3 | 02 Two Pointers & Sliding Window | 90 min coding, 20 min story matrix (chapter 14) | Redo list. Write 2 STAR stories. |
| 4 | 03 Stack & Queue, 04 Linked Lists | 90 min coding, 20 min behavioral | **Mock set 1.** Grade it. |
| 5 | 05 Binary Search | 90 min coding, 20 min behavioral | **Mock set 2.** Redo list. |
| 6 | 06 Trees | 90 min coding, 20 min behavioral (matrix complete) | **Mock set 3.** |
| 7 | 06 Trees (finish), 07 Heaps | 90 min coding, tell 4 stories aloud, timed | Redo list. One 45-min mock with a friend. |
| 8 | 08 Graphs | 100 min coding, 15 min probes | **Mock set 4.** |
| 9 | 08 Graphs (finish), 09 Backtracking | 90 min coding, 30 min behavioral drill | **Mock set 5.** Redo list. |
| 10 | 10 Dynamic Programming | 90 min coding, 30 min behavioral drill | Full behavioral mock, 25 min, 4 questions. |
| 11 | 10 DP (finish), 11 Greedy & Intervals, 12 Tries, Union-Find & Bits | 100 min coding, weakest 2 stories | **Mock set 6.** |
| 12 | 13 System Design (SDE2+ / L4+; new grads use the redo list) | 60 min one design aloud, 45 min one mock problem, 15 min behavioral | Two full mock loops with a human. Then rest. |

From week 8, do one mock with a real human every two weeks: a friend, a colleague, or a
platform such as Pramp (free) or interviewing.io (paid). Five human mocks before the loop is
the minimum. Practice in the real tool. Google uses a plain Google Doc with no autocomplete,
so write ten problems in one before the phone screen.

## When you get stuck

You will get stuck. They grade the next two minutes. Five moves, in order.

- **Restate the problem from the examples.** "So for [1, 3, 5] and target 8 we want indices 1 and 2." Half the time this exposes what you misread.
- **Shrink the example.** Solve n=1, 2, 3 by hand. What changed between 2 and 3 is usually the recurrence or the pointer move.
- **Say the brute force and start coding it.** Slow working code earns partial credit. A blank screen earns none.
- **Name a pattern out loud, even a wrong one.** "This feels like sliding window, but it would shrink from both ends, so maybe prefix sums." That reasoning is what the problem-solving axis grades.
- **Ask for a hint with shape.** "I have tried a hash map and sorting. Neither handles duplicates. What am I missing?" Then say what the hint changed. One hint plus a clean finish is a Hire. The same hint twice is not.

## Day-of checklist

The week before: redo list only, two human mocks, all eight stories told aloud once, tool and
round order confirmed with the recruiter, sleep on schedule. The day before, one easy problem
in the morning, then nothing.

- [ ] Eat something with protein. Water on the desk. Bathroom before each round.
- [ ] Paper and two pens beside you, even for virtual interviews.
- [ ] Editor open and blank, in the exact tool they use. Font readable on a shared screen.
- [ ] Phone silenced and out of sight. Notifications off.
- [ ] Your one-page list of story titles within glance range. Never read from it.
- [ ] Between rounds: stand up, drink water, do not replay the last round. Each interviewer grades independently.
- [ ] After the last round: write down every question you got. It is useless in a week.

## Words you will hear

- **Phone screen.** The first live interview. 45 to 60 minutes, one engineer, a shared editor.
- **Onsite / loop.** Four or five interviews back to back. The main event.
- **Online Assessment (OA).** Amazon's automated first filter: two coding problems plus a work-style questionnaire.
- **Buy-in.** The nod after "does this approach look right?" and before you write code.
- **Hint.** A nudge when you are stuck. Budgeted for. Not a failure.
- **Rubric.** The scoring sheet. Google has four axes. Amazon has a coding bar plus Leadership Principles.
- **Talk ratio.** How much of the time you are narrating. Silences over 30 seconds count against it.
- **Redo list.** Problems you solved without recognizing the pattern. Do them again a week later.

## Mistakes everyone makes once

- **Saving mocks for after you finish learning.** Talking and timing are skills. They need reps from week 1.
- **Believing talking slows you down.** Narration costs seconds and buys hints, because the interviewer can see where you are.
- **Coding before the plan.** Twenty minutes designing and half a function at the buzzer. Get the nod first.
- **Treating the phone screen as the easy one.** Same 45 minutes with less slack, and at Google the document is all the interviewer sees.

## What to do next

Set a 20-minute timer and start your phone recording. Solve `two_sum` from chapter 01 out loud
using the script above, including "does this look right to you?" answered by yourself. Watch
the recording at 1.5× speed and count the silences longer than 30 seconds. That count is your
starting number. Beat it next weekend.
