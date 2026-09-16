# 15 · Mock Interviews & the Plan

> Nobody plays their first real match at the tournament. Every problem in this repo was
> practice; this chapter is the scrimmage. You will be uncomfortable, timed, and talking to
> a wall. That discomfort is the point. The room feels easy after this.

**How to use this chapter:** read sections 1 to 3 in week 1 of the course and use the
timeline on every problem you solve. Come back for the mock sets from week 4 onward, one
per weekend. Sections 6 to 9 are for the last two weeks before your interviews.

## 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** The single biggest reason prepared candidates fail is
the gap between solving a problem at your desk and solving the same problem while a stranger
watches and a clock runs. Every interviewer has seen it: a candidate who clearly knows the
material freezes, codes before thinking, or goes silent for three minutes. That stress is
measuring something real. Senior engineers explain their thinking under pressure in design
reviews and incident calls every week. Performance under observation is a skill, and like a
musician's recital, it is trained separately from the material itself.

**The analogy.** A pilot's simulator hours, or a sports team's scrimmage. The pilot already
knows how to fly. The simulator exists so the emergency procedure costs no thought when the
real alarm sounds, because attention is the scarcest thing in a cockpit. The scrimmage exists
because a team that has only run drills has never made a decision with someone in its way.
Every problem in the previous fourteen chapters was a drill. This chapter is the scrimmage,
with the timer, the talking, and the being watched all switched on at once.

**How it works, in plain words.** The interview asks you to do four things at once: solve the
problem, talk while you do it, watch the clock, and be observed. Each one costs working
memory, and you have a fixed amount. Mocks rehearse the three non-problem skills until they
run on autopilot. The script in section 2 means you never have to invent a sentence. The
timeline in section 1 means you never have to decide which phase you are in. After enough
repetitions, talking and timing cost nothing, and your whole attention returns to the actual
problem, the only place it was ever useful.

**What learning this will feel like.** Mocks feel embarrassing, so people avoid them, and then
meet the embarrassment for the first time in the real room. Recording yourself is worse: you
will hear every "um, so, basically" and every long silence, and you will want to stop the
playback. Do not. That cringe is the accurate signal that the recording shows you what the
interviewer sees, and it is the exact thing you can fix. The aha arrives early. The second
mock is already easier than the first, because the novelty of being watched has worn off. And the first time you get stuck and a scripted sentence comes out
instead of silence, the "what do I say now" freeze is gone. It does not come back.

**You will know you have it when** a timer starting and a camera pointing at you changes
nothing about how you solve the problem.

## 1. The 45-minute coding interview, minute by minute

Both companies give you one problem (sometimes a warm-up plus a main problem) in 45 minutes.
The interviewer expects to spend the first few minutes on introductions and the last few on
your questions, so the real budget is about 40 minutes. Here is how to spend it.

| Minutes | Phase | What you produce | The failure if you skip it |
|---------|-------|------------------|----------------------------|
| 0–5 | **Clarify and examples** | Restated problem, 2 examples, 1 edge case, written down | Solving the wrong problem for 30 minutes |
| 5–10 | **Brute force and complexity** | A correct slow approach, its O(), said out loud | Nothing on the board if the clever idea never comes |
| 10–15 | **Optimize and get buy-in** | The pattern, the better O(), a one-line plan, interviewer nod | Coding an approach the interviewer already knows is wrong |
| 15–35 | **Code** | Clean, named, narrated code; helper functions where they clarify | Running out of time with half a function |
| 35–42 | **Test by hand** | A trace of one example line by line; one edge case; a bug found and fixed | The interviewer finds your bug and grades it |
| 42–45 | **Complexity and follow-ups** | Time and space, stated without prompting; a sentence on what you would change at scale | Ending on silence instead of on a strong note |

Twenty minutes of coding for a medium problem is plenty if you have a plan. If you are still
designing at minute 20, say so, pick the best approach you have, and code it. A working
O(n log n) solution beats an imagined O(n).

The phone screen is the same shape with less slack: the warm-up, if there is one, should be
done in 10 minutes.

## 2. The out-loud script

You do not need to improvise. Use these sentences. They sound natural because they are what
good candidates actually say, and they hit the communication rubric on purpose.

**Minutes 0–5, clarify**

- "Let me make sure I understand. We are given ___ and need to return ___. Is that right?"
- "Can the input be empty? Can values be negative? Are there duplicates? How large can n be?"
  (The size question tells you the target complexity: n ≤ 20 hints at exponential, n ≤ 10^5
  means O(n log n) or better.)
- "Let me write two examples. For input ___ the output is ___ because ___. And an edge case:
  ___."
- "Should I return the value or the index? If there are multiple valid answers, is any one
  fine?"

**Minutes 5–10, brute force**

- "The brute force is to ___, which is O(___) time and O(___) space. That works but is too
  slow for n up to 10^5."
- "The repeated work is ___." (This sentence is the bridge to the optimization. Say it every
  time.)

**Minutes 10–15, optimize and buy-in**

- "That repeated work looks like a ___ problem" (hash lookup, sliding window, monotonic stack,
  BFS, binary search on the answer, DP over prefixes). "So I will ___."
- "That brings it to O(___) time, O(___) space."
- "Before I code, does this approach look right to you?" (Always ask. A nod saves you 20
  minutes; a frown saves you the interview.)
- If they push back: "Good point. Let me think about the case where ___." Do not defend an
  approach you have been told is wrong.

**Minutes 15–35, code**

- "I will write a helper for ___ so the main loop stays readable."
- "I am using a dict from value to index because ___."
- Narrate decisions, not keystrokes. "Now the loop" is fine. Reading each character aloud is
  not.
- When you notice a bug while writing: "Wait, this would break when ___. Let me fix that."
  Finding your own bug is a positive signal, not a negative one.
- If you go quiet for more than 30 seconds: "I am thinking about how to handle ___."

**Minutes 35–42, test**

- "Let me trace this on the example. i=0, x=3, need=3, seen is empty, so seen becomes {3:0}.
  i=1, ..." Actually walk it. Write the variable values down.
- "Now the edge case: empty input. We never enter the loop and return [], which is correct."
- "I want to check the boundary at ___." (Off-by-one at the last index, the first element, the
  single-element input.)

**Minutes 42–45, wrap**

- "Time is O(___) because ___. Space is O(___) because ___."
- "If the input did not fit in memory, I would ___." or "If this were called a million times
  with the same array, I would precompute ___."
- "Is there a follow-up you would like me to look at?"

## 3. What the interviewer writes down

Knowing the rubric changes how you spend your minutes.

### Google: four axes

Every Google coding interviewer writes feedback under these four headings, each with a rating
from Strong No Hire to Strong Hire, and a hiring committee reads them without meeting you.

| Axis | Lean Hire looks like | Strong Hire looks like |
|------|----------------------|------------------------|
| **Algorithms / data structures** | Got to a working solution with hints; knew the right structure once named | Identified the optimal approach unprompted, explained why it works, discussed an alternative |
| **Coding** | Correct code with a bug or two caught during testing; some messy naming | Clean, idiomatic, correct on first pass; sensible helpers; handled edge cases in the code, not as an afterthought |
| **Communication** | Explained the approach when asked; some silent stretches | Narrated reasoning continuously, asked good clarifying questions, checked in before coding, adjusted well to hints |
| **Problem solving** | Needed the brute force pointed out; followed hints to the optimization | Found the brute force fast, named the repeated work, derived the optimization; handled follow-ups with a new idea |

The committee is looking for consistency across four or five interviewers. One "Lean Hire"
with strong others is fine. One "No Hire" needs to be outweighed by clear strength elsewhere.
Two "No Hire" ratings and the packet usually does not pass.

### Amazon: coding bar plus Leadership Principles

Amazon interviewers rate whether your coding met the bar for the level and write a
separate section on the two or three LPs they were assigned (see chapter 14). In the coding
portion they weight:

| Signal | Lean Hire | Strong Hire |
|--------|-----------|-------------|
| **Working code** | Runs correctly on the main case after fixes | Correct including edge cases, tested by you before they asked |
| **Complexity awareness** | Stated when asked | Stated unprompted for the brute force and the final; knew the trade-off |
| **Clarification** | Asked one or two questions | Nailed scope, found the edge case that mattered, wrote examples |
| **Handling hints** | Took the hint and moved | Took the hint, said what it changed, and finished cleanly (graded as Learn and Be Curious / Earn Trust) |
| **Ownership of bugs** | Fixed bugs when pointed out | Found them yourself; said what you would add as tests |

At Amazon the coding bar is somewhat lower than Google's per problem, but the behavioral
half is graded just as hard and a coding round with no LP evidence is an incomplete round.

## 4. How to run a mock

### With a friend

Give them the problem and the solution the day before. Their job in the room: read the
prompt once, answer clarifying questions honestly, give one hint if you are silent for two
minutes, and take notes against the rubric below. They should not teach, hint early, or
react to your code with their face. Forty-five minutes on a timer, then 10 minutes of
feedback using the table. Swap roles next time; interviewing someone teaches you what
interviewers notice.

### Alone

It works better than you expect. Set a 45-minute timer. Record yourself: phone camera
pointed at your paper or screen, audio on. Talk to the camera as if it were a person,
including "does this look right to you?" (then answer as the interviewer would). Do not look
at hints or solutions until the timer ends. Then watch the recording at 1.5x speed and grade
it with the rubric. The recording is the point. You will hear the silences, the "um, so,
basically," and the moment you started coding before you had a plan.

### The rubric

Score each row 1 (missing), 2 (partial), 3 (solid). A hireable mock scores 24 or more out
of 30 with no 1s.

| # | Criterion | 1 | 2 | 3 |
|---|-----------|---|---|---|
| 1 | Restated the problem and asked about size, duplicates, empty input | Started coding | Asked one question | Restated, 3+ questions, wrote examples |
| 2 | Wrote 2 examples and 1 edge case before coding | None | Examples only | Examples and an edge case that later mattered |
| 3 | Stated a brute force with its complexity | None | Approach without O() | Approach and O(), then named the repeated work |
| 4 | Named the pattern and got buy-in before coding | Neither | One of the two | Named it, gave the new O(), asked "does this look right?" |
| 5 | Code correctness on first full pass | Wrong | One bug | Correct, or bug found by own trace |
| 6 | Code clarity: names, helpers, no dead code | Hard to read | Readable | Someone else could maintain it |
| 7 | Traced an example by hand, line by line | Did not test | Described the test | Actually traced with variable values |
| 8 | Stated final time and space unprompted | Did not | When asked | Unprompted, with a reason |
| 9 | Talk ratio: silences under 30 seconds, no monologues over 2 minutes | Long silences or rambling | Mostly fine | Steady narration of decisions |
| 10 | Finished within 45 minutes with a working solution | Did not finish | Finished with hints | Finished with time for a follow-up |

Keep a log: date, problem, score, the two lowest rows. After five mocks the low rows are
your pattern. Fix those, not everything.

## 5. Six timed mock sets

Three problems per set, 45 minutes each on a timer, out loud, in one sitting if you can
(2 hours 15 minutes plus breaks) or one per day if not. Solve from the exercise file for
that chapter with the tests hidden until you are done; do not open the lesson. Order within
each set is easy → medium → hard-ish, which is also the order an onsite tends to escalate.

After the set, read the pattern column and check: did you *recognize* the pattern in the
first five minutes, or did you find it by trial? Recognition is the skill the mocks are
training. A problem you solved without recognizing the pattern goes on your redo list.

### Set 1 · Phone-screen shape, Amazon-flavored

| # | Chapter | Function | Pattern being tested |
|---|---------|----------|----------------------|
| 1 | `01_arrays_hashing` | `two_sum` | Hash map of what you have seen; check before record |
| 2 | `03_stack_queue` | `valid_parentheses` | Stack for matching; map closers to openers |
| 3 | `05_binary_search` | `search_rotated` | Binary search with a modified invariant: which half is sorted? |

### Set 2 · Phone-screen shape, Google-flavored

| # | Chapter | Function | Pattern being tested |
|---|---------|----------|----------------------|
| 1 | `04_linked_list` | `reverse_list` | Three-pointer iteration; then do it recursively |
| 2 | `02_two_pointers_sliding_window` | `longest_substring_no_repeat` | Variable-size sliding window with a set or last-index map |
| 3 | `08_graphs` | `num_islands` | Grid as implicit graph; DFS or BFS flood fill; mark visited in place |

### Set 3 · Onsite round, data structures

| # | Chapter | Function | Pattern being tested |
|---|---------|----------|----------------------|
| 1 | `07_heaps` | `kth_largest` | Min-heap of size k; O(n log k) beats sorting |
| 2 | `03_stack_queue` | `daily_temperatures` | Monotonic stack for "next greater element" |
| 3 | `04_linked_list` | `LRUCache` | Dict plus doubly linked list; O(1) get and put; Amazon's favorite |

### Set 4 · Onsite round, recursion

| # | Chapter | Function | Pattern being tested |
|---|---------|----------|----------------------|
| 1 | `12_tries_unionfind_bits` | `single_number` | XOR cancels pairs; O(1) space |
| 2 | `09_recursion_backtracking` | `subsets` | Choose / don't choose backtracking template |
| 3 | `10_dynamic_programming` | `coin_change` | Unbounded knapsack; memoized recursion → bottom-up 1D table |

### Set 5 · Onsite round, graphs and intervals

| # | Chapter | Function | Pattern being tested |
|---|---------|----------|----------------------|
| 1 | `11_greedy_intervals` | `merge_intervals` | Sort by start, then sweep and merge |
| 2 | `08_graphs` | `rotting_oranges` | Multi-source BFS; level count is the answer |
| 3 | `08_graphs` | `alien_dictionary` | Build a graph from adjacent-word comparisons, then topological sort; detect cycles |

### Set 6 · Onsite round, hard-ish

| # | Chapter | Function | Pattern being tested |
|---|---------|----------|----------------------|
| 1 | `01_arrays_hashing` | `product_except_self` | Prefix and suffix products without division |
| 2 | `10_dynamic_programming` | `word_break` | DP over prefixes: `dp[i]` = can `s[:i]` be segmented |
| 3 | `02_two_pointers_sliding_window` | `trapping_rain_water` | Two pointers moving from the lower max side; or prefix max arrays |

### Swap-in pool

When you have done all six sets, build your own from this pool. Aim for one problem from each
difficulty, different chapters, and at least one you have not seen for a week.

| Difficulty | Chapter | Function | Pattern |
|------------|---------|----------|---------|
| Easy | `06_trees` | `level_order` | BFS by level with queue length |
| Easy | `10_dynamic_programming` | `house_robber` | 1D DP: take or skip |
| Easy | `03_stack_queue` | `MinStack` | Auxiliary stack of running minimums |
| Easy | `02_two_pointers_sliding_window` | `container_most_water` | Two pointers from the ends; move the shorter side |
| Medium | `01_arrays_hashing` | `group_anagrams`, `top_k_frequent`, `longest_consecutive`, `subarray_sum_k` | Canonical key; bucket sort by count; set with run starts; prefix sum plus map |
| Medium | `02_two_pointers_sliding_window` | `three_sum` | Sort, fix one, two pointers; skip duplicates |
| Medium | `03_stack_queue` | `decode_string` | Stack of (string, count) at each `[` |
| Medium | `04_linked_list` | `reorder_list`, `copy_random_list` | Find middle, reverse second half, interleave; map old → new nodes |
| Medium | `05_binary_search` | `min_eating_speed`, `TimeMap` | Binary search on the answer; binary search over timestamps per key |
| Medium | `06_trees` | `is_valid_bst`, `lowest_common_ancestor` | Pass (low, high) bounds down; recurse, return the node where paths split |
| Medium | `07_heaps` | `task_scheduler`, `meeting_rooms_ii` | Max-heap by count with cooldown queue; min-heap of end times |
| Medium | `08_graphs` | `find_order_courses`, `network_delay_time` | Kahn's topological sort; Dijkstra |
| Medium | `09_recursion_backtracking` | `combination_sum`, `word_search` | Backtrack with a start index to avoid duplicates; DFS on grid with undo |
| Medium | `10_dynamic_programming` | `longest_common_subsequence`, `length_of_lis` | 2D table over two prefixes; O(n²) DP or patience sort with binary search |
| Medium | `11_greedy_intervals` | `non_overlapping_intervals`, `jump_game_ii` | Sort by end, greedy keep; greedy furthest reach per jump |
| Medium | `12_tries_unionfind_bits` | `Trie`, `accounts_merge` | Trie insert / search / prefix; union-find over emails |
| Hard | `01_arrays_hashing` | `first_missing_positive` | Use the array itself as the hash |
| Hard | `02_two_pointers_sliding_window` | `min_window_substring` | Sliding window with a "have vs need" counter |
| Hard | `03_stack_queue` | `largest_rectangle_histogram` | Monotonic stack; pop computes width |
| Hard | `04_linked_list` | `merge_k_sorted_lists` | Min-heap of heads; O(N log k) |
| Hard | `05_binary_search` | `median_two_sorted` | Binary search the partition of the shorter array |
| Hard | `06_trees` | `max_path_sum`, `Codec` | Post-order returning best single branch; preorder serialize with null markers |
| Hard | `07_heaps` | `MedianFinder` | Two heaps, balanced |
| Hard | `08_graphs` | `word_ladder` | BFS over words with wildcard buckets |
| Hard | `09_recursion_backtracking` | `n_queens` | Backtrack with column and diagonal sets |
| Hard | `10_dynamic_programming` | `edit_distance` | 2D table; three transitions |
| Hard | `12_tries_unionfind_bits` | `find_words` | Trie plus grid DFS; prune found words |

## 6. The 12-week calendar

The README gives per-chapter durations that add up to about 14 weeks of content plus two for
mocks. This calendar compresses that into 12 by pairing the half-week chapters and running
behavioral practice (chapter 14) and weekend mocks (this chapter) alongside the coding
chapters instead of after them. If you have 16 weeks, use the README durations literally and
keep the same weekend structure.

Daily minutes assume 1.5 to 2 hours a day. "Coding" means the loop from the README: one
problem, 30-minute timer, out loud, tests, redo list.

| Week | Chapters | Weekday, per day | Weekend |
|------|----------|------------------|---------|
| 1 | 00 Foundations | 60 min reading and Python drills; 30 min Big-O and recursion exercises | Read sections 1–3 of this chapter. Write your first `redo.txt`. |
| 2 | 01 Arrays & Hashing | 90 min coding (2 problems) | Redo everything on the list. No mock yet. |
| 3 | 02 Two Pointers & Sliding Window | 90 min coding; start 14: 20 min, story matrix (14 §4) | Redo list. Write 2 STAR stories. |
| 4 | 03 Stack & Queue, 04 Linked Lists | 90 min coding; 20 min behavioral (2 more stories) | **Mock set 1.** Grade with the rubric. |
| 5 | 05 Binary Search | 90 min coding; 20 min behavioral (2 more stories) | **Mock set 2.** Redo list. |
| 6 | 06 Trees | 90 min coding; 20 min behavioral (last 2 stories; matrix complete) | **Mock set 3.** |
| 7 | 06 Trees (finish), 07 Heaps | 90 min coding; 20 min behavioral: tell 4 stories out loud, timed | Redo list. One 45-min mock with a friend on a tree problem. |
| 8 | 08 Graphs | 100 min coding; 15 min behavioral: probes (14 §5) | **Mock set 4.** |
| 9 | 08 Graphs (finish), 09 Backtracking | 90 min coding; 30 min behavioral: 14 §9 week 1 drill | **Mock set 5.** Redo list. |
| 10 | 10 Dynamic Programming | 90 min coding; 30 min behavioral: 14 §9 week 2 drill | Full behavioral mock (25 min, 4 questions, probing). |
| 11 | 10 DP (finish), 11 Greedy & Intervals, 12 Tries, Union-Find & Bits | 100 min coding; 15 min behavioral: weakest 2 stories | **Mock set 6.** |
| 12 | 13 System Design (L4+ / SDE2+; new grads use this time for the redo list), sections 7–9 of this chapter | 60 min: one design out loud (13 §7) or redo list; 45 min: one swap-in mock problem; 15 min behavioral | Two full mock loops with a human: coding + behavioral, back to back. Then rest. |

Ongoing from week 3: chapter 14 never stops. Twenty minutes a day is enough; the two-week drill
in weeks 9–10 is the intensive block.

From week 8 onward, do at least one mock with a real human every two weeks: a friend, a
colleague, or a platform (Pramp is free and peer-to-peer; interviewing.io has paid sessions
with engineers from the target companies). Five human mocks before the real loop is the
minimum. Alone-with-a-camera mocks are for the weekends in between.

## 7. Phone screen vs onsite at Google and Amazon

### Amazon

**Online Assessment (OA).** Before any human contact, most SDE1 and many SDE2 candidates get
an OA in a browser. Two coding questions, about 70 minutes total, usually a medium string or
array problem and a medium graph, heap, or greedy problem. Tests are hidden except for a few
samples; you are graded on how many hidden tests pass, so handle edge cases even when the
prompt does not mention them. The OA also includes a **work simulation** (also called a work
style assessment): scenarios where you pick what you would do as an Amazon engineer, and
Likert-scale questions about your preferences. Answer as someone who lives the Leadership
Principles would: take ownership, go to the data, escalate late rather than early, favor the
customer. Do not overthink it, but do not answer randomly; it is scored.

**Phone screen.** 45 to 60 minutes with one engineer. Ten to fifteen minutes of LP questions,
then one coding problem in a shared editor (usually LiveCode or a similar tool, no
autocomplete, no running code). Medium difficulty. Often skipped for SDE1 candidates who did
well on the OA.

**Onsite (the "loop").** Four or five rounds of 55 to 60 minutes each, often on one day,
sometimes split across two. A typical SDE2 loop: two coding rounds, one system design round,
one low-level / OOD round, and the Bar Raiser round which is mostly behavioral. Every round
opens with 15 to 25 minutes of LP questions. One of the interviewers is the hiring manager.
The debrief happens the same or next day; a recruiter calls within a week.

### Google

**Phone screen.** 45 minutes with one engineer in a shared Google Doc (no syntax highlighting,
no autocomplete, tabs are your problem). One problem, sometimes with a warm-up. Medium to
medium-hard. No behavioral questions. The doc is the only thing the interviewer sees, so
write the examples and complexity in the doc, not just say them. Some candidates get two phone
screens. New grads may get an online coding test instead.

**Onsite.** Four or five rounds of 45 minutes: three or four coding, one Googleyness &
Leadership, and for L5 and above a system design round. Rounds are back to back with a lunch
that is not graded. Coding rounds are harder than the phone screen and the interviewers vary
more in style: some talk a lot, some say almost nothing. Interviewers write feedback; a
hiring committee that did not meet you reads the packet and decides. Then team matching, then
a compensation committee. Expect two to six weeks between onsite and offer.

### What to expect, side by side

| | Amazon | Google |
|-|--------|--------|
| First filter | Online assessment: 2 coding + work simulation | Recruiter screen, then phone screen |
| Phone screen | 45–60 min, LPs then coding, shared editor | 45 min, coding only, shared Google Doc |
| Onsite rounds | 4–5 × 60 min, each with 15–25 min of LPs | 4–5 × 45 min, one dedicated G&L round |
| Design | System design (SDE2+) and OOD / low-level (SDE1 and SDE2) | System design for L5+ |
| Behavioral weight | Half of every round; Bar Raiser can veto | One round; hiring committee reads all feedback |
| Decision | Debrief within a day; answer within a week | Hiring committee, then team match; weeks |
| Editor | Online editor, no execution | Google Doc, no execution |

Practice in the tool you will use. For Google, write at least ten problems in a plain Google
Doc before the phone screen. For Amazon, practice in any online editor with autocomplete off.

## 8. Checklists

### The week before

- [ ] Stop learning new patterns. Redo list only. Nothing new enters the list this week.
- [ ] Do two full mocks with a human, one coding and one behavioral, on different days.
- [ ] Re-read every chapter's recognition-cue table (section 4 of each lesson). Thirty minutes total.
- [ ] Tell all eight STAR stories out loud once. Fix any that run over 2:30.
- [ ] Confirm the schedule with the recruiter: round order, interviewer names if given, tool
      used for coding, whether you may use paper.
- [ ] Look up each interviewer's team if names are given. One sentence of context each; no
      more.
- [ ] Prepare your two questions for the end of each round (chapter 14 §8).
- [ ] For virtual interviews: test camera, microphone, second monitor, the exact link, and a
      backup device. Charge everything.
- [ ] Sleep on schedule for the full week. A rested candidate outscores a crammed one.
- [ ] The day before: one easy problem in the morning to stay warm, then nothing. Walk.

### Day of

- [ ] Eat something with protein. Water on the desk. Bathroom before each round.
- [ ] Paper and two pens beside you even for virtual interviews (for drawing examples), unless
      the recruiter said not to.
- [ ] Editor open, blank, in the exact tool they use. Font size readable on a shared screen.
- [ ] Phone silenced and out of sight. Notifications off on the computer.
- [ ] Your one-page story-bank list (titles only) within glance range for behavioral rounds.
      Never read from it; it is a memory aid.
- [ ] Between rounds: stand up, drink water, do not replay the last round. Each interviewer
      grades independently and does not know what happened before.
- [ ] After the last round: write down every question you got while you remember. It is the
      most valuable study material you will ever own, and it is useless in a week.

## 9. When you get stuck in the real room

You will get stuck. Interviewers expect it and often plan for it. What they grade is what you
do in the next two minutes. Five moves, in the order to try them:

1. **Restate the problem out loud, from the examples.** "So for [1, 3, 5] and target 8 we want
   indices 1 and 2." Half the time, saying it exposes the thing you misread. It also fills the
   silence with signal instead of nothing.

2. **Shrink the example.** Take n=1, n=2, n=3. Solve those by hand. Write the outputs. Ask what
   changed between n=2 and n=3. That difference is usually the recurrence, the invariant, or the
   pointer move you need.

3. **Say the brute force and start coding it.** "I don't see the optimal approach yet. Let me
   write the O(n²) version so we have something working, and I will look for the repeated work
   as I go." Working code is worth partial credit; a blank screen is worth none. Interviewers
   often hint once you have the slow version because now there is something concrete to
   improve.

4. **Name the pattern out loud, even a wrong one.** "This feels like a sliding window because
   we want a contiguous range... but the window would have to shrink from both ends, which
   breaks the pattern. So maybe prefix sums instead." Reasoning out loud about which pattern
   fits and why is exactly what the problem-solving axis grades. The interviewer will often
   confirm or redirect, and either way you have moved.

5. **Ask for a hint, gracefully.** "I have considered a hash map and a sorted approach and
   neither handles the duplicate case. Could you point me toward what I am missing?" Notice the
   shape: what you have tried, what specifically blocks you, then the ask. That is a different
   request from "I don't know, can you help?"

**How hints are graded.** A hint is not a failure. Interviewers budget for one or two; the
notes say "needed a hint on X, then finished cleanly" and that is a Hire in most rooms. What
costs you is: needing the same hint twice, ignoring a hint because you were attached to your
approach, or needing hints on every phase. The best recovery after a hint is to say what it
changed: "Right, if I sort first the duplicates are adjacent, so I can skip them with a
while loop. That makes the whole thing O(n log n)." That sentence turns a hint into evidence
that you learn fast, which Amazon literally has a Leadership Principle for.

One last thing. An interview is 45 minutes of a stranger watching you think. Everything in
this repository was preparation for that, and none of it is wasted if you walk in, take a
breath, and start with "Let me make sure I understand."
