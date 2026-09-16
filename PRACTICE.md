# How to practise without getting buried

[Start](README.md) · [Path](ROADMAP.md)

## Make the start small

Choose a repeatable cue: “After tea, I open the next task for five minutes.” Your minimum session is reading the question and tracing one example. A normal session adds one function and a check. A longer session adds a new edge case or a recall review. Pick the size that fits today.

A passing file is evidence that its checks passed, not proof of mastery. Being able to explain an approach on a new input is the next goal. The first lap is deliberately small; later chapters are a reference library you can return to.

## Before touching the code

Write four lines in your own words:

- Input: what values am I given, and what inputs are allowed?
- Output: exactly what is returned, including order and missing-answer behavior?
- Example: what should happen on one tiny input, and why?
- State: what do I need to remember as I process it?

Use a trace table with one row per step. For a running total over [6, 3], the rows are start=0, after 6=6, after 3=9. For a pointer task, record both indices and what remains a candidate. For recursion, record the current call and what it waits for.

## Read test feedback as a clue

`python learn.py check 00/01` runs one exercise in a separate process. It stops after five seconds if your code hangs. This timeout catches accidental nontermination; it is not a benchmark or proof of the required Big-O.

- **Next function is still waiting:** `NotImplementedError` is a placeholder, not a judgement. Fill one function, then try again.
- **AssertionError:** inspect the labelled expression. It contains the expected result. Print your actual return temporarily, compare it, then remove the debug output.
- **IndexError:** trace the smallest allowed list; does that position exist? Check before reading index zero.
- **SyntaxError or TypeError:** check the reported line and values before changing the algorithm.
- **Stopped after 5s:** identify the variable that should move toward termination. Check every branch updates it. Computing an expression alone does not store the result.

Do not run practice tests with `python -O`: that disables assert statements. The learning runner always starts a normal interpreter even if its parent was launched with optimization.

The checks stop at the first failing assertion. If a file contains several functions, later functions may remain untested until earlier ones pass. Keep your next action small. Printed `ok` must stay at the end, after all the checks; do not remove checks just to get a pass.

## Build better test cases

Use a normal case, the smallest allowed case, and one that challenges your assumption. Examples:

| Contract | Useful case | Why it matters |
|---|---|---|
| Return the second **distinct** largest number, or None | [5, 5] → None | Equal values do not give two distinct ranks |
| Return two different positions for a target sum | [4, 4], target 8 → [0, 1] | Equal values may still occupy different positions |
| Return a new rotated list | Rotation by zero | Equal contents must not hide accidental aliasing |
| Return the best non-empty segment sum | [-7, -2, -9] → -2 | Zero would incorrectly choose an empty segment |
| Brackets must nest correctly | "([)]" → False | Equal opening/closing counts are insufficient |
| Four-direction connected land | Diagonal-only cells | Diagonal adjacency must not merge islands |

Respect constraints: do not demand empty-input handling when the question guarantees non-empty input. For in-place tasks, inspect the original object. For unordered answers, normalize only when the contract allows it. Small correctness checks do not establish performance; explain the complexity separately.

## Return without restarting

After your first pass, the runner schedules recall tomorrow. Successful due reviews schedule the next attempt 3, then 7, then 14 days later; further reviews stay 14 days apart. These are practical defaults, not a scientifically optimal schedule for everyone.

When a review appears, cover your old code. Explain the idea and rewrite it on paper or in a scratch file, then compare with the question and run your checks. Only then use `python learn.py reviewed CH/EX`. A review command is an honest self-report, not an automatic assessment. If recall fails, reread the relevant lesson and leave the review due. You can choose any new exercise manually if you need a change of pace.

No missed-day penalty, reset, or percentage-based readiness claim is used. Previously passed files remain in practice history even if you later edit their code; recheck a file for current correctness.

## Why the learning flow works this way

The implementation uses one visible next action, optional detail, small practice sessions, and specific failure feedback to make starting less demanding. Those are design choices, not guarantees about motivation.

Closed-book recall follows research showing benefits from retrieval practice for later retention ([Karpicke & Roediger, 2008](https://www.science.org/doi/10.1126/science.1152408)). Revisiting material across days follows evidence on distributed practice ([Cepeda et al., 2006](https://pubmed.ncbi.nlm.nih.gov/16719566/)). These studies inform the practice structure; they do not validate this repository, its chosen intervals, or any promised interview outcome.
