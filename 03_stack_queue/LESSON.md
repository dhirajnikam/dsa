# 03 · Stack & Queue

> A stack remembers what you have not finished yet. Every time a problem says "the most
> recent unmatched thing," "the nearest one to the left," or "undo the last step," a stack is
> already the answer. You just have to notice.

**Interview frequency:** high. Valid Parentheses and Min Stack are Amazon phone-screen
staples. Google likes the monotonic stack family (Daily Temperatures, Largest Rectangle) as
the harder second problem in a round.

## Part 1 · From zero

*Read this if the chapter title means little to you yet. It explains the idea in plain
language before any code. If it already makes sense, skip to Part 2.*

### In one sentence

A stack is a pile you only touch from the top, a queue is a line you only join at the back
and leave from the front, and the rule "only touch one end" is exactly what makes each of
them useful.

### Start with something you already do

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

### Now the same thing with numbers

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

### The words people use

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

### Why the fast way is fast

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

### Try it in your head

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

### Common confusions, cleared

- **"Why not just count openers and closers?"** `([)]` has equal counts and is invalid. A
  closer must match the *most recent* unclosed opener, and "most recent" is a stack.
- **"The `while` inside the `for` makes it n²."** Count pops, not loop iterations. Each item
  is pushed once and popped at most once, so the whole run costs at most 2n.
- **"Why store day numbers instead of temperatures?"** The question asks for a distance. From
  the number 74 alone you cannot tell which day it was.
- **"A list already is a queue. I can `pop(0)`."** It works, but every remaining item shifts
  one slot left, so it costs n each time. `deque.popleft()` is one step. Interviewers notice.

### What to do next

Scroll down to Part 2 and read §2 (Valid Parentheses, fully worked); it is the doors story in
code. Then open `exercises.py` and do `valid_parentheses` and `daily_temperatures` with a
30-minute timer each. When both pass, do `MyQueue` to feel the pancake flip, then read Part 2 §3
for the other costumes the stack wears.

## Part 2 · The reference

*The worked anchor problem, the templates to memorize, recognition cues, and pitfalls.
This is the part you come back to.*

### 0. Why this matters, and how it works in one picture

**Where it lives in the real world.** Your browser's back button is a stack of pages. Undo in every
editor is a stack of edits. The call stack that runs your Python code is a stack of unfinished
functions, which is why runaway recursion is called a stack overflow. Compilers check that every
bracket in your program is matched with the same stack you will write in this chapter. Queues are
the other half: Amazon SQS holds orders in arrival order so the warehouse processes them fairly,
and every print spooler and message broker is a queue. Stock analytics that ask "how many days
until a higher price" run this chapter's monotonic stack in production.

**The analogy.** A stack is a pile of plates. You add to the top and take from the top, so the last
plate in is the first plate out. A queue is the line at a counter: join at the back, get served at
the front. Both are just lists with the rule "only touch one end." The rule is the power. Because
you cannot reach into the middle, the top of a stack always means something precise: the most
recent thing that is still waiting.

**How it works, in plain words.** When you meet something you cannot resolve yet, push it and move
on. When the thing that resolves it arrives, pop. An opening bracket waits for its closer. A cold
day waits for the next warmer day. An operand waits for its operator. The stack holds exactly the
items still waiting, most recent on top, so "the nearest unmatched thing to the left" is always one
`[-1]` away. A monotonic stack adds one twist: a new arrival may resolve many waiting items at
once, so you pop in a loop until the top is no longer beaten.

**What learning this will feel like.** Valid Parentheses will click quickly. Then Daily
Temperatures will feel like magic, and "pop while the top is smaller" will look like something you
could not have invented. That feeling is normal and temporary. Ask one question of each popped
element: "could this ever be the answer for anything later?" When the answer is "no, the new
element beats it and arrived sooner," the loop stops being magic and becomes obvious. The trap that
bites nearly everyone is storing values instead of indices, then discovering you cannot compute
"how many days" from a temperature alone. Fix it once and your hand will type the index forever.

**You will know you have it when** the phrase "nearest greater to the left" or "most recent
unmatched" makes you reach for `st = []` before you have considered a second loop.

### 1. The core idea

A stack is a list you only touch at one end: `append` to push, `pop` to pop, `[-1]` to peek.
All O(1). Its power is *deferral*. When you see something you cannot resolve yet, push it.
When the thing that resolves it arrives, pop. The stack always holds exactly the items that
are still waiting, in the order they will be resolved (most recent first).

That is the whole chapter in one sentence. Three costumes:

- **Matching.** Opening brackets wait for closing ones. Push opens, pop on close, check the
  pair.
- **Monotonic stack.** Elements wait for the next bigger (or smaller) element. When it
  arrives, it resolves every waiting element that is smaller, all at once.
- **Evaluation.** Operands wait for an operator. Nested strings wait for their `]`.

```
brute force ("next greater")           monotonic stack
for i in range(n):                     st = []                # indices of unresolved elements
    for j in range(i+1, n):            for j in range(n):
        if a[j] > a[i]:                    while st and a[j] > a[st[-1]]:
            ans[i] = a[j]; break               ans[st.pop()] = a[j]   # j resolves them
                                           st.append(j)
O(n²) time                             O(n) time: each index pushed once, popped once
```

The `while` inside the `for` looks quadratic. It is not. Each index enters the stack once and
leaves once, so the total work across all iterations is 2n. Say this in the room; it is the
thing interviewers listen for.

A queue is the other end: first in, first out. In Python use `collections.deque` with
`append` and `popleft`. A plain `list.pop(0)` is O(n) and a red flag.

### 2. Anchor problem: Valid Parentheses, fully worked

**Problem.** Given a string of `()[]{}`, decide whether every opening bracket is closed by
the same type, in the correct order.

**Understand.** Only those six characters appear. Empty string is valid. `"([)]"` is invalid
even though the counts match: order matters, not just count. `"(("` is invalid: unclosed.
`"))"` is invalid: nothing to close.

**Examples.** `"()[]{}" → True`. `"([)]" → False`. `"{[]}" → True`. `"]" → False`.
`"(" → False`.

**Brute force.** Repeatedly delete any adjacent matching pair (`()`, `[]`, `{}`) until none
remain; valid iff the string is empty. Each pass is O(n) and there can be O(n) passes: O(n²).
Correct, and it reveals the insight: a closing bracket always pairs with the *nearest
unmatched* opening bracket to its left.

**Insight.** "Nearest unmatched to the left" is exactly what the top of a stack is. Push
opens. On a close, the top must be its partner; pop it. At the end the stack must be empty.

**Code.**

```python
def valid_parentheses(s):
    pairs = {")": "(", "]": "[", "}": "{"}      # close -> open
    st = []
    for c in s:
        if c in pairs:                          # closing bracket
            if not st or st.pop() != pairs[c]:
                return False
        else:                                   # opening bracket
            st.append(c)
    return not st                               # anything left is unclosed
```

**Test.** `"([)]"`: `(` push → `[(]`. `[` push → `[(, []`. `)` pop gives `[`, need `(` →
`False`. ✓

`"{[]}"`: `{` push. `[` push. `]` pop `[` ✓. `}` pop `{` ✓. Stack empty → `True`. ✓

`"("`: push. End. Stack non-empty → `False`. ✓

**Complexity.** O(n) time, O(n) space (worst case all openers).

**What to say out loud.** "Each closing bracket must match the most recent unmatched opener,
and 'most recent' means a stack. I push openers, and on a closer I pop and compare. Two
failure modes: popping from an empty stack, and a non-empty stack at the end. O(n) time and
space."

### 3. Patterns & templates in this chapter

#### Matching stack

```python
st = []
for c in s:
    if opens(c):
        st.append(c)
    elif not st or not matches(st.pop(), c):
        return False
return not st
```

Brackets, HTML tags, "remove adjacent duplicates," "make the string valid." The two checks
that people forget are the empty pop and the leftover stack.

#### Monotonic stack (next greater element)

```python
ans = [-1] * n
st = []                                # indices; values strictly decreasing bottom -> top
for j, x in enumerate(nums):
    while st and nums[st[-1]] < x:     # x is the answer for everything smaller below it
        ans[st.pop()] = x              # or j - i for "how many days"
    st.append(j)
```

Change `<` to `>` for "next smaller." Sweep right-to-left for "previous greater." Store
indices, not values, so you can compute distances. Daily Temperatures, Next Greater Element,
Stock Span, and Largest Rectangle are all this loop with a different payoff line.

#### Largest rectangle via next smaller on both sides

Every bar `h[i]` wants to know how far it can extend left and right while staying `>= h[i]`.
That is "previous smaller" and "next smaller." One pass of a *non-decreasing* stack finds
both: when you pop bar `i` because a smaller `h[j]` arrived, its right bound is `j` and its
left bound is the new stack top. Append a sentinel `0` to flush the stack at the end.

```python
st = []; best = 0
for j, h in enumerate(heights + [0]):
    while st and heights[st[-1]] >= h:
        i = st.pop()
        width = j if not st else j - st[-1] - 1
        best = max(best, heights[i] * width)
    st.append(j)
```

#### Evaluation stack

```python
st = []
for tok in tokens:
    if tok in "+-*/":
        b, a = st.pop(), st.pop()      # b was pushed last; order matters for - and /
        st.append(apply(tok, a, b))
    else:
        st.append(int(tok))
return st[0]
```

Reverse Polish Notation. Decode String is the same idea with two things saved per level:
the partial string so far and the repeat count.

#### Queue with two stacks

```python
class MyQueue:
    def __init__(self):
        self.inbox, self.outbox = [], []
    def push(self, x):
        self.inbox.append(x)
    def _shift(self):                  # only when outbox is empty: reverse inbox into it
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
    def pop(self):
        self._shift(); return self.outbox.pop()
    def peek(self):
        self._shift(); return self.outbox[-1]
```

Each element is moved from inbox to outbox at most once, so every operation is O(1)
*amortized*. Be ready to say the word "amortized" and explain it: an occasional expensive
shift is paid for by the cheap pushes that preceded it.

#### Stack as a "keep the best sequence" filter

Remove K Digits, Asteroid Collision, Simplify Path: walk the input and maintain a stack of
what survives. A new item may destroy some of the stack top (a bigger digit before a smaller
one, an asteroid moving left into one moving right, `..` eating a directory). Push what is
left.

### 4. Recognition cues

| You see | Think |
|---------|-------|
| brackets, tags, "properly nested," "balanced" | matching stack |
| "next greater / smaller," "days until warmer," "span" | monotonic stack of indices |
| "largest rectangle," "max area under bars" | next smaller on both sides via one stack |
| postfix / RPN, "evaluate expression" | evaluation stack, pop two, push one |
| `k[encoded]`, nested repeats | stack of (partial string, count), resolve at `]` |
| "queue using stacks" or vice versa | two stacks, amortized argument |
| "collisions," "remove adjacent," "cancel out" | stack; new item fights the top |
| "remove k to make smallest/largest" | monotonic stack, then trim or strip zeros |
| `.`, `..`, `//` in a path | split on `/`, stack of directories |
| "cars catch up," "fleets" | sort by position, monotonic stack of arrival times |

### 5. Pitfalls

- **Popping an empty stack.** Always `if not st` before `st.pop()` on a close.
- **Forgetting the leftover check.** `"(("` passes every step and fails only at `return not st`.
- **RPN operand order.** The second pop is the *left* operand. `6 3 /` is `6 / 3`, so
  `b = pop(); a = pop(); a / b`.
- **RPN division.** Truncate toward zero: `int(a / b)`, not `a // b`. `-7 // 2` is `-4`;
  the problem wants `-3`.
- **Monotonic stack: strict vs. non-strict.** "Next *strictly* greater" pops on `<`. For
  Largest Rectangle you pop on `>=` so equal heights merge correctly.
- **Storing values instead of indices.** You cannot compute "how many days" or "how wide"
  from values alone.
- **Sentinel for flushing.** Largest Rectangle needs a final height `0` (or a post-loop drain)
  or the tallest bars at the end never get measured.
- **Two-stack queue: shifting too often.** Shift only when `outbox` is empty, or the
  amortized O(1) claim is false.
- **Remove K Digits: leading zeros and leftover k.** After the loop, drop `k` more from the
  end (the remaining digits are non-decreasing) and strip leading zeros. Return `"0"` if
  nothing is left.
- **Car Fleet: sort by position first,** descending, and reason about arrival time, not speed.
  A faster car behind a slower one becomes part of its fleet, never passes it.

### 6. Exercises

| # | Function | Difficulty | Asked at | One hint |
|---|----------|-----------|----------|----------|
| 1 | `valid_parentheses` | Easy | Amazon, Google | The anchor above. Empty pop and leftover stack are the two failure modes. |
| 2 | `MinStack` | Medium | Amazon, Google | Store `(value, min_so_far)` pairs. The min at each level is fixed forever. |
| 3 | `eval_rpn` | Medium | Amazon | Pop two, apply, push. `int(a / b)` for truncation toward zero. |
| 4 | `daily_temperatures` | Medium | Amazon, Google | Monotonic stack of indices. On pop, answer is `j - i`. |
| 5 | `next_greater_element` | Medium | Amazon | Same loop, answer is the value. Unresolved stay `-1`. |
| 6 | `MyQueue` | Easy | Amazon | Two stacks. Shift only when the outbox is empty. |
| 7 | `simplify_path` | Medium | Amazon, Google | `split("/")`. Skip `""` and `.`; `..` pops if possible; else push. |
| 8 | `decode_string` | Medium | Google, Amazon | On `[` push `(current, count)` and reset. On `]` pop and repeat. |
| 9 | `asteroid_collision` | Medium | Amazon | Only a left-moving newcomer fights a right-moving top. Loop until settled. |
| 10 | `remove_k_digits` | Medium | Google, Amazon | Pop while top > digit and k > 0. Trim leftover k. Strip zeros. |
| 11 | `car_fleet` | Medium | Google, Amazon | Sort by position descending. Time to target = `(target - pos) / speed`. A car slower than the fleet ahead joins it. |
| 12 | `largest_rectangle_histogram` | Hard | Amazon, Google | Non-decreasing stack. Pop on `>=`, width from the new top. Sentinel 0 at the end. |

Solve 1–9 in order. 10–12 are the stretch set; do them when 1–9 pass cold.
