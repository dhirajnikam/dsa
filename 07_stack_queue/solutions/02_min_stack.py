class MinStack:
    # O(1) per op, O(n) space
    # Each entry stores (value, min of everything at or below it), so popping restores the
    # previous minimum for free.
    def __init__(self):
        self.stack = []

    def push(self, val):
        cur_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, cur_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]
