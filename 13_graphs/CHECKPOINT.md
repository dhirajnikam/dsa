# Check your understanding: Graphs: track both connections and visits

[Back to the lesson](README.md)

Allow about 10 minutes. Close the lesson first. These are learning prompts, not a scored exam. There are no completed exercise answers in this repo.

## Explain from memory

1. When does BFS guarantee the shortest route, and what definition of shortest is it using?

2. How would you detect a component that the first traversal never reached?

3. Why does a route with a remaining-stops constraint need more state than just its current city?

## Apply it

Open [number of islands](problems/01_number_of_islands.py). Before reading hints:

1. Restate the input and exact return value in your own words.
2. Trace the smallest allowed example; track the changing state after every step.
3. Add a different valid edge case with the expected output and a reason for it. Avoid inventing behavior outside the stated constraints.
4. Explain time and auxiliary space. Name the work that grows and any hidden copying.

Run `python learn.py check 13/01` for executable correctness feedback.

## Optional transfer challenge

After the chapter feels comfortable, open [alien dictionary](problems/12_alien_dictionary.py). Identify what changes from the first task. Sketch an approach before coding; later exercises can be substantially harder and are not a gate for continuing the first lap.

## Decide what to do next

- **I can explain and trace it:** continue to your next task; revisit tomorrow without looking at the code.
- **I can code it but cannot explain it:** reread one relevant paragraph and make a new trace.
- **I am stuck:** name the smallest unclear step, read one hint, and retry a smaller example. Returning later counts as progress.

There is no automatic score for these explanations. Check factual claims against the lesson, and test your examples. Record successful recall with `python learn.py reviewed 13/01` when the review is due; do not mark recall just because an old implementation still passes.
