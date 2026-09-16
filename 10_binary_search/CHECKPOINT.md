# Check your understanding: Binary search: discard only what you can prove

[Back to the lesson](README.md)

Allow about 10 minutes. Close the lesson first. These are learning prompts, not a scored exam. There are no completed exercise answers in this repo.

## Explain from memory

1. For an empty candidate interval, how do your chosen boundaries look?

2. Why is searching an unsorted list with the same comparisons invalid?

3. If each feasibility check scans n items and the answer range has width R, what total work do you expect?

## Apply it

Open [binary search](problems/01_binary_search.py). Before reading hints:

1. Restate the input and exact return value in your own words.
2. Trace the smallest allowed example; track the changing state after every step.
3. Add a different valid edge case with the expected output and a reason for it. Avoid inventing behavior outside the stated constraints.
4. Explain time and auxiliary space. Name the work that grows and any hidden copying.

Run `python learn.py check 10/01` for executable correctness feedback.

## Optional transfer challenge

After the chapter feels comfortable, open [median two sorted arrays](problems/08_median_two_sorted_arrays.py). Identify what changes from the first task. Sketch an approach before coding; later exercises can be substantially harder and are not a gate for continuing the first lap.

## Decide what to do next

- **I can explain and trace it:** continue to your next task; revisit tomorrow without looking at the code.
- **I can code it but cannot explain it:** reread one relevant paragraph and make a new trace.
- **I am stuck:** name the smallest unclear step, read one hint, and retry a smaller example. Returning later counts as progress.

There is no automatic score for these explanations. Check factual claims against the lesson, and test your examples. Record successful recall with `python learn.py reviewed 10/01` when the review is due; do not mark recall just because an old implementation still passes.
