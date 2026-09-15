class MyQueue:
    # amortised O(1) per op, O(n) space
    # Pushes land in `inbox`; pops come from `outbox`. Only when `outbox` runs dry do we pour
    # `inbox` into it (reversing order). Each element crosses over once.
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def push(self, x):
        self.inbox.append(x)

    def _shift(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def pop(self):
        self._shift()
        return self.outbox.pop()

    def peek(self):
        self._shift()
        return self.outbox[-1]

    def empty(self):
        return not self.inbox and not self.outbox
