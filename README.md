# Python + DSA, one small step at a time

You do not need to finish the whole repository. Start with one idea and one function.

**Your first action:** read [Python basics](00_python_basics/README.md), then open [basic arithmetic](00_python_basics/problems/01_hello_math.py). If you already started, keep your work and use the checks to find the next step.

From the repository folder, with Python 3.10 or newer:

```bash
python learn.py
```

This shows one task. There is no installation, account, or dependency setup. If your computer uses `python3`, substitute that in each command.

## A session you can actually finish

1. **Understand:** read one part of the lesson and trace its small example.
2. **Try:** implement one function. Aim for 10–20 minutes; five minutes still counts.
3. **Check:** run `python learn.py check 00/01` (replace the chapter/exercise numbers).
4. **Recall:** cover your code and explain what changes at each step. Add one edge case.

Stop after one useful step. If you miss a day, resume the next task; there is no streak to lose or backlog to clear. If you are stuck, read one hint, trace a smaller input, then retry. A test failure tells you what to investigate.

## Where to go

- [Learning path](ROADMAP.md): a short first lap, then optional depth.
- [How to practise and debug](PRACTICE.md): examples, test feedback, and recall reviews.
- Each chapter’s `README.md` teaches the theory; `CHECKPOINT.md` asks you to explain and apply it.
- Each `problems/*.py` contains a question, examples, hints, your implementation area, and executable checks.

Completed reference solutions have been removed. Existing work in the problem files is retained. Small teaching examples explain concepts; they do not implement the practice answers.

<details>
<summary>More commands, when you need them</summary>

```bash
python learn.py today          # one next task or due recall review
python learn.py check 05/01    # check one file, with a five-second timeout
python learn.py reviewed 05/01 # record successful recall when due
python learn.py list           # browse all exercises
python progress.py            # next task and saved practice history
python progress.py 05         # check one chapter
python progress.py --all      # optional: check the entire library
```

Checks stop at the first failure in that file. Passing requires completing all its functions. You can still work on just one function today. Progress is recorded by these commands, not by running files directly. Review dates use your computer’s local date.

Practice history stays in an ignored local file. It does not sync between computers. Re-running passing code does not postpone a review or claim that you remembered it.

Maintainer checks: `python -m unittest discover -s tests -v`. These validate the learning tools and content structure. Unfinished exercises are expected to fail their own practice checks.

</details>
