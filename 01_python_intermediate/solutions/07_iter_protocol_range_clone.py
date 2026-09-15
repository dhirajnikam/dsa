class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("step must not be zero")
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        x = self.start
        while (x < self.stop) if self.step > 0 else (x > self.stop):
            yield x
            x += self.step

    def __len__(self):  # O(1)
        if self.step > 0:
            return max(0, (self.stop - self.start + self.step - 1) // self.step)
        return max(0, (self.start - self.stop - self.step - 1) // -self.step)

    def __contains__(self, x):  # O(1)
        if self.step > 0:
            in_bounds = self.start <= x < self.stop
        else:
            in_bounds = self.stop < x <= self.start
        return in_bounds and (x - self.start) % self.step == 0

    def __getitem__(self, i):
        n = len(self)
        if i < 0:
            i += n
        if not 0 <= i < n:
            raise IndexError("Range index out of range")
        return self.start + i * self.step

    def __repr__(self):
        return f"Range({self.start}, {self.stop}, {self.step})"
