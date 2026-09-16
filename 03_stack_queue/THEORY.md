# 03 · Stack & Queue, explained from zero

Read this first if "stack" only means dishes to you and "monotonic" sounds like a medical
condition. When it makes sense, open `LESSON.md`, the dense reference. This file is the
friendly conversation before it.

## In one sentence

A stack is a pile you only touch from the top, a queue is a line you only join at the back
and leave from the front, and the rule "only touch one end" is exactly what makes each of
them useful.

## Start with something you already do

**A stack of plates.** You wash a plate and set it on the pile. When you need one, you take
the top. You always get the plate you put down most recently, and you cannot grab one from
the middle without lifting everything above it. Last in, first out.

**A line at a coffee counter.** Join at the back. The barista serves the front. Whoever
arrived first leaves first, and nobody cuts. First in, first out.

**Doors you opened.** You walk into a house, opening doors as you go. On the way out you close
them in reverse order: the last door you opened is the first one you pass. If you find
yourself closing a door you never opened, or you reach the exit with doors still open,
something went wrong. Brackets are doors. `(`, `[`, `{` open one, and `)`, `]`, `}` close one.
The pile of currently open doors, most recent on top, is a stack.

**People who leave when someone taller arrives.** A line forms for a photo, and each person
wants to know: "who is the first person taller than me to arrive after me?" When a newcomer
arrives, everyone at the back who is shorter gets their answer and leaves. Whoever stays is
taller than the newcomer, so the line is always tallest at the front. That line is a monotonic
stack. Swap "taller" for "warmer" and you have Daily Temperatures.

**Flipping pancakes.** Pancakes come off the pan onto plate A, so the first one cooked is at
the bottom. You want to serve them in cooking order. Flip the whole pile onto plate B: now the
first cooked is on top. Serve from B while new pancakes land on A. Flip again only when B
runs empty. Two stacks, one queue.

## Now the same thing with numbers

**Brackets.** Check `{[]}`.

| read | top before | action | stack after |
|------|------------|--------|-------------|
| `{` | | opener, push | `{` |
| `[` | `{` | opener, push | `{ [` |
| `]` | `[` | matches, pop | `{` |
| `}` | `{` | matches, pop | empty |

Empty at the end: valid. Now `([)]`: push `(`, push `[`, then `)` arrives and the top is `[`.
Wrong door. Invalid, even though every bracket has a twin.

**Daily temperatures.** `[73, 74, 71, 76]`. For each day, how many days until a warmer one?

| day | temp | waiting (days) | what happens | waiting after |
|-----|------|----------------|--------------|---------------|
| 0 | 73 | | nothing to beat, push | 0 |
| 1 | 74 | 0 | 74 beats 73: day 0 waited 1 day | 1 |
| 2 | 71 | 1 | 71 beats nothing, push | 1, 2 |
| 3 | 76 | 1, 2 | beats 71: day 2 waited 1. Beats 74: day 1 waited 2 | 3 |

Answer `[1, 2, 1, 0]`. Day 3 never gets a warmer day, so it stays 0. Pause and predict: for
`[30, 40, 50]`, how many pops happen in total across the whole run?

<details><summary>Answer</summary>
Two. Day 0 is popped when 40 arrives, day 1 when 50 arrives. Answer `[1, 1, 0]`. Every day
is pushed once and popped at most once, so the total work can never exceed two moves per day.
</details>

## The words people use

- **Stack.** A list you only touch at one end. Last in, first out.
- **Push / pop / peek.** Add to the top. Remove the top and hand it back. Look at the top
  without removing it. In Python: `append`, `pop`, `[-1]`.
- **LIFO / FIFO.** Last in, first out (stack). First in, first out (queue).
- **Queue.** Join at the back, leave from the front. In Python, `collections.deque` with
  `append` and `popleft`.
- **Deque.** Double-ended queue. Instant add or remove at either end. A plain list's `pop(0)`
  shifts every remaining item down a slot, which is slow.
- **Top.** The most recent item still waiting. Always one `[-1]` away.
- **Matching.** Pairing each closer with the nearest opener not yet closed.
- **Monotonic stack.** A stack kept sorted from bottom to top by popping anything the
  newcomer beats.
- **Next greater element.** For each item, the first item to its right that is bigger.
- **Index vs value.** Where an item sits vs what number it holds. Store the index so you can
  compute "how many days" or "how wide" later.
- **Sentinel.** A fake final item (a height of 0, say) that forces the stack to empty so every
  waiting item gets measured.
- **Amortized.** Averaged over all operations. One expensive flip is paid for by the many
  cheap pushes before it.
- **RPN / postfix.** Operator written after its operands: `3 4 +` means 3 + 4.
- **Operand / operator.** The numbers, and the symbol that combines them.
- **Call stack, stack overflow.** Where unfinished function calls wait. Too many at once and
  the program gives up.
- **Min stack.** A stack that also reports its smallest item instantly, by storing
  (value, smallest so far) at every level.

## Why the fast way is fast

"Days until warmer" the obvious way: for each day, scan forward until you find one. On a
cooling trend you scan the whole rest of the list every time, about n × n ÷ 2 looks.

| n | scan forward | monotonic stack |
|---|--------------|-----------------|
| 10 | 45 | 20 |
| 1,000 | 500,000 | 2,000 |
| 100,000 | 5,000,000,000 | 200,000 |

At roughly 100,000,000 simple steps a second, the scan takes about a minute on the last row
and the stack takes two milliseconds.

What did you pay? Memory. On a cooling trend nothing ever gets popped, so the stack holds
all n days at once: O(n) space bought to get O(n) time. The two-stack queue trades
differently. A single flip can cost n moves, but each pancake is flipped exactly once in its
life, so the average cost per operation stays constant.

## Try it in your head

1. Is `"(()"` valid?

<details><summary>Answer</summary>
Push `(`, push `(`, then `)` pops one. The string ends with one `(` still on the stack.
Invalid. This is the "leftover" failure that people forget to check.
</details>

2. Evaluate the RPN tokens `2 3 4 * +`.

<details><summary>Answer</summary>
Push 2, 3, 4. On `*`: pop 4, pop 3, push 12. On `+`: pop 12, pop 2, push 14. Answer 14. The
second pop is always the left operand, which matters for subtraction and division.
</details>

3. Two-stack queue: push 1, push 2, pop, push 3, pop, pop. Which pops trigger a flip?

<details><summary>Answer</summary>
First pop: B is empty, flip [1, 2] so 1 is on top, serve 1. Push 3 onto A. Second pop: B
still holds 2, no flip, serve 2. Third pop: B empty, flip [3], serve 3. Two flips for three
pops, and each pancake was flipped once.
</details>

## Common confusions, cleared

- **"Why not just count openers and closers?"** `([)]` has equal counts and is invalid. A
  closer must match the *most recent* unclosed opener, and "most recent" is a stack.
- **"The `while` inside the `for` makes it n²."** Count pops, not loop iterations. Each item
  is pushed once and popped at most once, so the whole run costs at most 2n.
- **"Why store day numbers instead of temperatures?"** The question asks for a distance. From
  the number 74 alone you cannot tell which day it was.
- **"A list already is a queue. I can `pop(0)`."** It works, but every remaining item shifts
  one slot left, so it costs n each time. `deque.popleft()` is one step. Interviewers notice.

## What to do next

Open `LESSON.md` and read §2 (Valid Parentheses, fully worked); it is the doors story in
code. Then open `exercises.py` and do `valid_parentheses` and `daily_temperatures` with a
30-minute timer each. When both pass, do `MyQueue` to feel the pancake flip, then read §3
for the other costumes the stack wears.
