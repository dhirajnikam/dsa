# Check your understanding: Greedy: make a choice you can defend

[Back to the lesson](README.md)

Allow about 10 minutes. Close the lesson first. These are learning prompts, not a scored exam. There are no completed exercise answers in this repo.

## Explain from memory

1. What would count as a counterexample to your proposed greedy rule?

2. Why is “it worked on three examples” weaker than an exchange argument?

3. Which quantity does your next greedy task maintain, and how does each choice preserve it?

## Apply it

Open [jump game](problems/01_jump_game.py). Before reading hints:

1. Restate the input and exact return value in your own words.
2. Trace the smallest allowed example; track the changing state after every step.
3. Add a different valid edge case with the expected output and a reason for it. Avoid inventing behavior outside the stated constraints.
4. Explain time and auxiliary space. Name the work that grows and any hidden copying.

Run `python learn.py check 15/01` for executable correctness feedback.

## Optional transfer challenge

After the chapter feels comfortable, open [min arrows burst balloons](problems/07_min_arrows_burst_balloons.py). Identify what changes from the first task. Sketch an approach before coding; later exercises can be substantially harder and are not a gate for continuing the first lap.

## Decide what to do next

- **I can explain and trace it:** continue to your next task; revisit tomorrow without looking at the code.
- **I can code it but cannot explain it:** reread one relevant paragraph and make a new trace.
- **I am stuck:** name the smallest unclear step, read one hint, and retry a smaller example. Returning later counts as progress.

There is no automatic score for these explanations. Check factual claims against the lesson, and test your examples. Record successful recall with `python learn.py reviewed 15/01` when the review is due; do not mark recall just because an old implementation still passes.
