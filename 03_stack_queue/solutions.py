"""03 · Stack & Queue — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""


def valid_parentheses(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    st: list[str] = []
    for c in s:
        if c in pairs:
            if not st or st.pop() != pairs[c]:
                return False
        else:
            st.append(c)
    return not st
    # O(n) time, O(n) space.


class MinStack:
    def __init__(self) -> None:
        self.st: list[tuple[int, int]] = []     # (value, min of everything at or below)

    def push(self, val: int) -> None:
        cur_min = min(val, self.st[-1][1]) if self.st else val
        self.st.append((val, cur_min))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def get_min(self) -> int:
        return self.st[-1][1]
    # All O(1). The min below any level never changes, so store it once at push time.


def eval_rpn(tokens: list[str]) -> int:
    st: list[int] = []
    for tok in tokens:
        if tok in ("+", "-", "*", "/"):
            b, a = st.pop(), st.pop()           # a is the left operand
            if tok == "+":
                st.append(a + b)
            elif tok == "-":
                st.append(a - b)
            elif tok == "*":
                st.append(a * b)
            else:
                st.append(int(a / b))           # truncate toward zero, unlike //
        else:
            st.append(int(tok))
    return st[0]
    # O(n) time and space.


def daily_temperatures(temps: list[int]) -> list[int]:
    ans = [0] * len(temps)
    st: list[int] = []                          # indices, temps decreasing bottom -> top
    for j, t in enumerate(temps):
        while st and temps[st[-1]] < t:
            i = st.pop()
            ans[i] = j - i                      # j is the first warmer day for i
        st.append(j)
    return ans
    # O(n): each index pushed once, popped at most once. O(n) space.


def next_greater_element(nums: list[int]) -> list[int]:
    ans = [-1] * len(nums)
    st: list[int] = []
    for j, x in enumerate(nums):
        while st and nums[st[-1]] < x:
            ans[st.pop()] = x
        st.append(j)
    return ans
    # O(n) time and space. Same loop as daily_temperatures with a different payoff.


class MyQueue:
    def __init__(self) -> None:
        self.inbox: list[int] = []
        self.outbox: list[int] = []             # reversed inbox; its top is the queue front

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def _shift(self) -> None:
        if not self.outbox:                     # only when empty, or amortization breaks
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def pop(self) -> int:
        self._shift()
        return self.outbox.pop()

    def peek(self) -> int:
        self._shift()
        return self.outbox[-1]

    def empty(self) -> bool:
        return not self.inbox and not self.outbox
    # Each element moves inbox -> outbox at most once: amortized O(1) per operation.


def simplify_path(path: str) -> str:
    st: list[str] = []
    for part in path.split("/"):
        if part == "" or part == ".":
            continue                            # empty from // or trailing /, or "here"
        if part == "..":
            if st:
                st.pop()                        # go up, but never above root
        else:
            st.append(part)
    return "/" + "/".join(st)
    # O(n) time and space.


def decode_string(s: str) -> str:
    st: list[tuple[str, int]] = []              # (string built before '[', repeat count)
    cur, num = "", 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)             # multi-digit counts
        elif c == "[":
            st.append((cur, num))               # defer: finish the inner part first
            cur, num = "", 0
        elif c == "]":
            prev, k = st.pop()
            cur = prev + cur * k
        else:
            cur += c
    return cur
    # O(output length) time; O(nesting depth) stack entries.


def asteroid_collision(asteroids: list[int]) -> list[int]:
    st: list[int] = []
    for a in asteroids:
        alive = True
        while alive and a < 0 and st and st[-1] > 0:    # only right-mover vs left-mover collide
            if st[-1] < -a:
                st.pop()                        # top explodes, keep fighting
            elif st[-1] == -a:
                st.pop()
                alive = False                   # both explode
            else:
                alive = False                   # newcomer explodes
        if alive:
            st.append(a)
    return st
    # O(n): each asteroid pushed once and popped at most once.


def remove_k_digits(num: str, k: int) -> str:
    st: list[str] = []
    for d in num:
        while k and st and st[-1] > d:
            st.pop()                            # a bigger digit before a smaller one: drop it
            k -= 1
        st.append(d)
    if k:
        st = st[:len(st) - k]                   # leftover k: digits are non-decreasing, cut the tail
    out = "".join(st).lstrip("0")
    return out or "0"
    # O(n) time and space.


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)     # closest to target first
    st: list[float] = []                                  # arrival times of fleet leaders
    for pos, spd in cars:
        t = (target - pos) / spd
        if not st or t > st[-1]:
            st.append(t)                        # arrives later than the fleet ahead: new fleet
        # else: catches the fleet ahead and joins it; nothing to push
    return len(st)
    # O(n log n) for the sort, O(n) space.


def largest_rectangle_histogram(heights: list[int]) -> int:
    st: list[int] = []                          # indices, heights non-decreasing bottom -> top
    best = 0
    for j, h in enumerate(heights + [0]):       # sentinel 0 flushes every bar at the end
        while st and heights[st[-1]] >= h:
            i = st.pop()
            width = j if not st else j - st[-1] - 1     # left bound is the new top, right is j
            best = max(best, heights[i] * width)
        st.append(j)
    return best
    # O(n) time and space. Each bar is pushed once and popped once.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
