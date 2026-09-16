# 03 · Stack & Queue

*New to this topic? Read `THEORY.md` in this folder first. It explains the idea from zero.*

> A stack remembers what you have not finished yet. Every time a problem says "the most
> recent unmatched thing," "the nearest one to the left," or "undo the last step," a stack is
> already the answer. You just have to notice.

**Interview frequency:** high. Valid Parentheses and Min Stack are Amazon phone-screen
staples. Google likes the monotonic stack family (Daily Temperatures, Largest Rectangle) as
the harder second problem in a round.

## 0. Why this matters, and how it works in one picture

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

## 1. The core idea

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

## 2. Anchor problem: Valid Parentheses, fully worked

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

## 3. Patterns & templates in this chapter

### Matching stack

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

### Monotonic stack (next greater element)

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

### Largest rectangle via next smaller on both sides

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

### Evaluation stack

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

### Queue with two stacks

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

### Stack as a "keep the best sequence" filter

Remove K Digits, Asteroid Collision, Simplify Path: walk the input and maintain a stack of
what survives. A new item may destroy some of the stack top (a bigger digit before a smaller
one, an asteroid moving left into one moving right, `..` eating a directory). Push what is
left.

## 4. Recognition cues

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

## 5. Pitfalls

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

## 6. Exercises

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
