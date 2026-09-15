class OutOfStock(Exception):
    def __init__(self, name, available):
        super().__init__(f"{name}: only {available} available")
        self.name = name
        self.available = available


class Inventory:
    def __init__(self):
        self.items = {}  # name -> [qty, price]

    def add(self, name, qty, price):
        if qty <= 0 or price < 0:
            raise ValueError("qty must be > 0 and price >= 0")
        if name in self.items:
            self.items[name][0] += qty
            self.items[name][1] = price
        else:
            self.items[name] = [qty, price]

    def remove(self, name, qty):
        if name not in self.items:
            raise KeyError(name)
        available = self.items[name][0]
        if qty > available:
            raise OutOfStock(name, available)
        self.items[name][0] -= qty
        return self.items[name][0]

    def total_value(self):
        return float(sum(q * p for q, p in self.items.values()))

    def low_stock(self, threshold):
        return sorted((n for n, (q, _) in self.items.items() if q <= threshold),
                      key=lambda n: (self.items[n][0], n))

    def report(self):
        lines = [f"{n:<10}{q:>5}{p:>10.2f}" for n, (q, p) in sorted(self.items.items())]
        lines.append(f"{'TOTAL':<15}{self.total_value():>10.2f}")
        return "\n".join(lines)

    def __len__(self):
        return len(self.items)

    def __contains__(self, name):
        return name in self.items
