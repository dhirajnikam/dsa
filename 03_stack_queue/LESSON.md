# 03 · Stack & Queue

**In one sentence.** A stack is a pile you only touch from the top, a queue is a line you only
join at the back and leave from the front, and the rule "only touch one end" is exactly what
makes each of them useful.

**Why you care.** Your browser's back button, undo in every editor, and the call stack that runs
your Python code are all stacks. Order queues and message brokers are queues. Interview frequency
is high. Valid Parentheses and Min Stack are Amazon phone-screen staples. Google likes the
monotonic stack family as the harder second problem.

## The idea, with a story

**Doors you opened.** You walk into a house, opening doors as you go. On the way out you close
them in reverse order: the last door you opened is the first one you pass. If you find yourself
closing a door you never opened, or you reach the exit with doors still open, something went
wrong. Brackets are doors. `(`, `[`, `{` open one. `)`, `]`, `}` close one. The pile of currently
open doors, most recent on top, is a stack.

**People who leave when someone taller arrives.** A line forms for a photo. Each person wants to
know: "who is the first taller person to arrive after me?" When a newcomer arrives, everyone at
the back who is shorter gets their answer and leaves. Whoever stays is taller than the newcomer,
so the line is always tallest at the front. That line is a monotonic stack. Swap "taller" for
"warmer" and you have Daily Temperatures.

**Flipping pancakes.** Pancakes come off the pan onto plate A, first cooked at the bottom. To
serve in cooking order, flip the whole pile onto plate B. Serve from B while new pancakes land on
A. Flip again only when B runs empty. Two stacks, one queue.

## The same story with numbers

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

| day | temp | waiting | what happens | waiting after |
|-----|------|---------|--------------|---------------|
| 0 | 73 | | nothing to beat, push | 0 |
| 1 | 74 | 0 | beats 73: day 0 waited 1 | 1 |
| 2 | 71 | 1 | beats nothing, push | 1, 2 |
| 3 | 76 | 1, 2 | beats 71: day 2 waited 1. Beats 74: day 1 waited 2 | 3 |

Answer `[1, 2, 1, 0]`.

Pause and predict: for `[30, 40, 50]`, how many pops happen in total across the whole run?

<details><summary>Answer</summary>
Two. Day 0 is popped when 40 arrives, day 1 when 50 arrives. Answer <code>[1, 1, 0]</code>. Every
day is pushed once and popped at most once, so the total work never exceeds two moves per day.
</details>

## The anchor problem: Valid Parentheses

Given a string of `()[]{}`, decide whether every opener is closed by the same type, in the right
order. `"{[]}"` is `True`. `"([)]"` and `"(("` are `False`.

**Brute force.** Repeatedly delete any adjacent matching pair until none remain. Valid iff the
string is empty. O(n²).

**Insight.** A closer always pairs with the nearest unmatched opener to its left. "Nearest
unmatched" is exactly what the top of a stack is.

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

**Complexity.** O(n) time, O(n) space in the worst case of all openers.

**What to say.** "Each closer must match the most recent unmatched opener, and 'most recent' means
a stack. Two failure modes: popping from an empty stack, and a non-empty stack at the end."

## Templates you memorize

**Matching stack.** Push what opens. On a close, the top must be its partner.
```python
st = []
for c in s:
    if opens(c):
        st.append(c)
    elif not st or not matches(st.pop(), c):
        return False
return not st
```

**Monotonic stack (next greater element).** Store indices, so you can compute distances later.
```python
ans = [-1] * n
st = []                                # indices; values decreasing bottom -> top
for j, x in enumerate(nums):
    while st and nums[st[-1]] < x:     # x is the answer for everything smaller below
        ans[st.pop()] = x              # or j - i for "how many days"
    st.append(j)
```

**Evaluation stack.** Pop two, apply, push one. The second pop is the left operand.
```python
st = []
for tok in tokens:
    if tok in "+-*/":
        b, a = st.pop(), st.pop()      # b was pushed last
        st.append(apply(tok, a, b))
    else:
        st.append(int(tok))
```

**Queue via two stacks.** Shift only when the outbox is empty. Each item is flipped once.
```python
def push(self, x):
    self.inbox.append(x)
def pop(self):
    if not self.outbox:                # flip the pile, first-in ends on top
        while self.inbox:
            self.outbox.append(self.inbox.pop())
    return self.outbox.pop()
```

## When you see X, think Y

| You see | Think |
|---------|-------|
| brackets, tags, "balanced", "properly nested" | matching stack |
| "next greater / smaller", "days until warmer" | monotonic stack of indices |
| "largest rectangle under bars" | next smaller on both sides via one stack, sentinel 0 at the end |
| postfix / RPN, "evaluate expression" | evaluation stack |
| `k[encoded]`, nested repeats | stack of (partial string, count), resolve at `]` |
| "queue using stacks" | two stacks, say "amortized" |
| "collisions", "remove adjacent", "cancel out" | stack; the new item fights the top |
| `.`, `..`, `//` in a path | split on `/`, stack of directories |

## Words you will hear

- **Push / pop / peek.** Add to the top. Remove the top. Look at the top. In Python: `append`,
  `pop`, `[-1]`.
- **LIFO / FIFO.** Last in, first out (stack). First in, first out (queue).
- **Deque.** Double-ended queue. `collections.deque` with `append` and `popleft`. A list's `pop(0)`
  shifts every item and is slow.
- **Monotonic stack.** A stack kept sorted by popping anything the newcomer beats.
- **Sentinel.** A fake final item, such as a height of 0, that forces the stack to empty so every
  waiting item gets measured.
- **Amortized.** Averaged over all operations. One expensive flip is paid for by the cheap pushes
  before it.
- **RPN / postfix.** Operator after its operands: `3 4 +` means 3 + 4.

## Mistakes everyone makes once

- **Popping an empty stack.** Always check `if not st` before popping on a close.
- **Forgetting the leftover check.** `"(("` passes every step and only fails at `return not st`.
- **Storing values instead of indices** in a monotonic stack. You cannot compute "how many days"
  from 74 alone.
- **RPN division.** Truncate toward zero with `int(a / b)`, not `a // b`. `-7 // 2` is `-4` but
  the problem wants `-3`.

## Exercises

Run `python exercises.py`. Each prints PASS, FAIL, or TODO.

| # | Function | Level | Hint |
|---|----------|-------|------|
| 1 | `valid_parentheses` | Easy | The anchor. Empty pop and leftover stack are the two failure modes. |
| 2 | `MinStack` | Medium | Store `(value, min_so_far)` pairs. The min at each level never changes. |
| 3 | `eval_rpn` | Medium | Pop two, apply, push. `int(a / b)` for truncation toward zero. |
| 4 | `daily_temperatures` | Medium | Monotonic stack of indices. On pop, the answer is `j - i`. |
| 5 | `next_greater_element` | Medium | Same loop, the answer is the value. Unresolved stay `-1`. |
| 6 | `MyQueue` | Easy | Two stacks. Shift only when the outbox is empty. |
| 7 | `simplify_path` | Medium | `split("/")`. Skip `""` and `.`. `..` pops if possible. Else push. |
| 8 | `decode_string` | Medium | On `[` push `(current, count)` and reset. On `]` pop and repeat. |
| 9 | `asteroid_collision` | Medium | Only a left-moving newcomer fights a right-moving top. Loop until settled. |
| 10 | `remove_k_digits` | Medium | Pop while top > digit and k > 0. Trim leftover k. Strip leading zeros. |
| 11 | `car_fleet` | Medium | Sort by position descending. Time to target is `(target - pos) / speed`. |
| 12 | `largest_rectangle_histogram` | Hard | Non-decreasing stack. Pop on `>=`, width from the new top. Sentinel 0. |

Start with 1, 4, and 6 today. Do 2 to 9 over the week. 10 to 12 are for when the first nine pass cold.
