# Cracking Google & Amazon, From Zero

> "The only way to learn mathematics is to do mathematics." — Paul Halmos.
> The only way to pass a coding interview is to solve problems out loud, badly, and then better.

This repository is a course. It assumes you know almost nothing and takes you to the level
where a Google or Amazon onsite is a fair fight. There is no framework, no account, no app.
Just Python 3.10+, a terminal, and you.

## What these interviews actually test

Forget the myth that you need to know 500 problems. Interviewers at Google and Amazon grade
four things, and you can name them:

| Axis | What it looks like in the room |
|------|-------------------------------|
| **Problem solving** | You turn a vague prompt into a precise one, find the brute force, then find the pattern that beats it. |
| **Coding** | Your code is clean, correct the first time, and you test it yourself before they ask. |
| **Communication** | You think out loud, state assumptions, and say the complexity without being asked. |
| **Depth** | When they say "what if the input doesn't fit in memory?" you have an answer. |

Amazon adds a fifth axis: **Leadership Principles**. Every Amazon round opens with 15 to 20
minutes of behavioral questions. Chapter 14 covers this. Do not skip it. People with perfect
code fail Amazon loops on behavioral answers every week.

Roughly 15 patterns cover 90% of what is asked. This course teaches those patterns, one per
chapter, in the order a good teacher would: each chapter uses only tools from earlier ones.

## The path

| # | Chapter | Weeks | Why it is here |
|---|---------|-------|----------------|
| 00 | [Foundations](00_foundations/LESSON.md) | 1 | Python fluency, Big-O, recursion, and the protocol you use in every interview. |
| 01 | [Arrays & Hashing](01_arrays_hashing/LESSON.md) | 1 | The most asked category. Hash maps trade space for time. |
| 02 | [Two Pointers & Sliding Window](02_two_pointers_sliding_window/LESSON.md) | 1 | Turn O(n²) into O(n) on sorted data and contiguous ranges. |
| 03 | [Stack & Queue](03_stack_queue/LESSON.md) | 1 | Matching, monotonic stacks, "next greater" problems. |
| 04 | [Linked Lists](04_linked_list/LESSON.md) | 0.5 | Pointer discipline. Amazon loves LRU Cache. |
| 05 | [Binary Search](05_binary_search/LESSON.md) | 1 | One template, "search on the answer," never off by one again. |
| 06 | [Trees](06_trees/LESSON.md) | 1.5 | Recursion made concrete. DFS, BFS, BST invariants. |
| 07 | [Heaps](07_heaps/LESSON.md) | 0.5 | Top-K, streams, scheduling. |
| 08 | [Graphs](08_graphs/LESSON.md) | 1.5 | BFS, DFS, topological sort, Dijkstra, union-find. Google's favorite. |
| 09 | [Recursion & Backtracking](09_recursion_backtracking/LESSON.md) | 1 | Generate all subsets, permutations, and paths with one template. |
| 10 | [Dynamic Programming](10_dynamic_programming/LESSON.md) | 2 | The chapter people fear. Taught as memoized recursion first. |
| 11 | [Greedy & Intervals](11_greedy_intervals/LESSON.md) | 0.5 | Sort, then sweep. Meeting rooms and friends. |
| 12 | [Tries, Union-Find & Bits](12_tries_unionfind_bits/LESSON.md) | 0.5 | The last few structures that still show up. |
| 13 | [System Design](13_system_design/LESSON.md) | 1 | Required for SDE2/L4 and above. Estimation, building blocks, five walked designs. |
| 14 | [Behavioral](14_behavioral/LESSON.md) | ongoing | Amazon Leadership Principles, STAR stories, Googleyness. |
| 15 | [Mock Interviews & Plan](15_mock_interviews/LESSON.md) | 2 | The 45-minute protocol, timed sets, the 12-week calendar. |

The chapter weeks add up to about 16 at 1.5 to 2 hours a day. Chapter 15 compresses this into a
12-week calendar by pairing the half-week chapters and running 14 alongside everything else. If you
have even less time, do chapters 00 to 10, then 14 and 15. Never skip 14 for Amazon.

## How your brain learns this, and how to use that

Most people fail interview prep not because the material is hard but because they study the
way school taught them: read, nod, move on. Here is what actually works, and why.

- **Every lesson starts with "why."** Each chapter opens with where the idea lives in real
  Google and Amazon systems, an everyday analogy, and how it works in plain words. Your brain
  files new ideas next to things it already knows. Give it the hook first and the details stick.
- **Recall beats recognition.** Reading a solution and thinking "yes, obvious" is recognition.
  Producing it with the book closed is recall. Interviews test recall. So does this course:
  the exercises have no solutions in view, and the checker tells you honestly where you stand.
- **Struggle is the point.** Thirty minutes of being stuck is not wasted time. It is the moment
  your brain is building the connection. A solution read after struggle sticks for months. The
  same solution read before struggle is gone by Thursday. This is why the honor rule exists.
- **Spacing beats cramming.** Redoing a problem after three days, then seven, moves it from
  short-term to long-term memory. `redo.txt` is that system with zero ceremony.
- **Out loud is not optional.** Explaining forces you to find the gaps in your own understanding.
  It also happens to be a graded axis in the room. Two birds.
- **Small wins, daily.** One problem solved cold is a real win. Chase the streak of daily
  sessions, not the count of problems. Motivation follows progress, not the other way around.

Each lesson also tells you what learning that chapter will *feel* like, because knowing that
"this is the part where everyone feels lost" is the difference between pushing through and
quitting.

## How one study session works

Every chapter has three files:

- `LESSON.md` teaches the pattern. Read it once slowly with a pen. Trace every example by hand.
- `exercises.py` has 8 to 21 problems as empty functions with tests. Run it: `python exercises.py`.
- `solutions.py` has reference answers. It is locked by honor, not by code.

The loop, every day:

1. **Read** one lesson section or re-read the template you keep forgetting.
2. **Pick one problem.** Read it aloud. Write down two examples and one edge case before coding.
3. **Set a timer for 30 minutes.** Talk out loud as if someone is listening. Yes, alone, out loud.
4. **Run the tests.** `python exercises.py` prints PASS, FAIL, or TODO per problem.
5. **Stuck at 30 minutes?** Read the one hint in the lesson's exercise table. Still stuck at 40? Open
   `solutions.py`, read only that function, close it, and rewrite it from memory. Mark it for redo.
6. **After solving:** say the time and space complexity out loud. Name the pattern. Ask yourself
   "what would break this?" and add that test.

Keep a plain text file called `redo.txt`. Every problem you needed the solution for goes in it
with today's date. Redo it after 3 days, then after 7. A problem leaves the list when you solve
it cold twice. That is the whole spaced-repetition system. It works.

## Running things

```bash
python 01_arrays_hashing/exercises.py     # your work, per-problem PASS/FAIL/TODO
python 01_arrays_hashing/solutions.py     # proves the reference passes the same tests
python check_all.py                       # one progress line per chapter
python check_all.py solutions             # sanity: every reference solution passes
```

`redo.txt` at the repo root is your spaced-repetition list. It is a plain text file; edit it by hand.

No dependencies. If `python` opens Python 2 or fails, use `python3`.

## Rules of the house

- **Brute force first, always.** Say it, state its complexity, then improve. Interviewers want to
  see you can find *an* answer before *the* answer.
- **Out loud.** Communication is a graded axis. Silent correct code scores lower than narrated
  correct code.
- **Complexity every time.** Never finish a problem without saying time and space.
- **Test your own code.** Walk through one example line by line before you say "done."
- **Redo beats new.** Solving 60 problems twice beats solving 120 once.

## After this course

When you finish, you will have solved 180 problems that map closely to the well-known
Blind 75 and NeetCode 150 lists. From there, practice on LeetCode by company tag for the
company you are targeting, and do at least five live mock interviews with a human (Pramp,
interviewing.io, or a friend). Chapter 15 tells you how to run them.

Start now: open [00_foundations/LESSON.md](00_foundations/LESSON.md).
