# Check your understanding: Linked lists: preserve the next connection

[Back to the lesson](README.md)

Allow about 10 minutes. Close the lesson first. These are learning prompts, not a scored exam. There are no completed exercise answers in this repo.

## Explain from memory

1. Why is linked-list index access not constant time?

2. What reference must survive before you replace a node’s next link?

3. For four nodes, which node is “the middle”? What should the problem specify?

## Apply it

Open [reverse linked list](problems/01_reverse_linked_list.py). Before reading hints:

1. Restate the input and exact return value in your own words.
2. Trace the smallest allowed example; track the changing state after every step.
3. Add a different valid edge case with the expected output and a reason for it. Avoid inventing behavior outside the stated constraints.
4. Explain time and auxiliary space. Name the work that grows and any hidden copying.

Run `python learn.py check 08/01` for executable correctness feedback.

## Optional transfer challenge

After the chapter feels comfortable, open [lru cache](problems/08_lru_cache.py). Identify what changes from the first task. Sketch an approach before coding; later exercises can be substantially harder and are not a gate for continuing the first lap.

## Decide what to do next

- **I can explain and trace it:** continue to your next task; revisit tomorrow without looking at the code.
- **I can code it but cannot explain it:** reread one relevant paragraph and make a new trace.
- **I am stuck:** name the smallest unclear step, read one hint, and retry a smaller example. Returning later counts as progress.

There is no automatic score for these explanations. Check factual claims against the lesson, and test your examples. Record successful recall with `python learn.py reviewed 08/01` when the review is due; do not mark recall just because an old implementation still passes.
