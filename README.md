# Zero to Hundred: Python + DSA

Learn Python, then data structures and algorithms, then pass coding interviews.
Everything is plain `.py` files with built-in tests. Needs Python 3.10+.

## How it works

```
zero_to_hundred/
  progress.py              # run this: prints your score 0..100
  NN_topic/
    README.md              # short notes: key idea, templates, mistakes
    problems/xx_name.py    # problem + empty function + tests (you fill it in)
    solutions/xx_name.py   # answer
```

## Daily loop
1. Read the phase README (5 min).
2. Open a problem. Try for 25 minutes.
3. Run `python problems/xx_name.py`. Fix until it prints `ok`.
4. Stuck? Read the hints, then the solution. Redo it from scratch 3 days later.
5. Run `python progress.py` to see your score.

## Phases

| Phase | Folder | Learn |
|------:|--------|-------|
| 00-02 | `python_*` | Python itself |
| 03 | `complexity_math` | Big-O, recursion, bits |
| 04-06 | `arrays`, `hashing`, `two_pointers` | Array and string patterns |
| 07-08 | `stack_queue`, `linked_list` | Linear structures |
| 09-10 | `recursion_backtracking`, `binary_search` | Search |
| 11-13 | `trees`, `heaps_intervals`, `graphs` | Non-linear structures |
| 14-15 | `dynamic_programming`, `greedy` | Optimization |
| 16-17 | `tries_advanced`, `interview_mastery` | Extras and mock interviews |

Score = percent of problems that pass. Do phases in order.

## Running things

```bash
python progress.py            # score and per-phase breakdown
python progress.py 05         # only phase 05
python 05_hashing/problems/01_two_sum.py   # one problem
```
