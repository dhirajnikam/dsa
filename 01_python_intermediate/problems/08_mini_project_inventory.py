"""
Problem: Inventory manager (mini project)
Difficulty: Medium | Topic: classes + exceptions + sorting + formatting together

class OutOfStock(Exception) with attributes .name and .available.

class Inventory:
  .add(name, qty, price) -> None. Adds qty units. If the item exists, qty accumulates and the
       price is replaced. qty must be > 0 and price >= 0, else ValueError.
  .remove(name, qty) -> remaining qty. Unknown item -> KeyError. qty > available ->
       OutOfStock(name, available) and nothing changes. When qty reaches 0 the item stays
       with qty 0.
  .total_value() -> sum of qty * price over all items (float).
  .low_stock(threshold) -> list of names with qty <= threshold, sorted by (qty, name).
  .report() -> multi-line string, one line per item sorted by name, formatted as
       f"{name:<10}{qty:>5}{price:>10.2f}"   then a final line f"{'TOTAL':<15}{total:>10.2f}"
       For an empty inventory the report is just the TOTAL line.
  len(inv) -> number of distinct items.
  name in inv -> membership.

Example report for add("bolt", 100, 0.25), add("nut", 3, 0.10):
  "bolt        100      0.25\nnut           3      0.10\nTOTAL               25.30"

Hints:
1. Store a dict name -> [qty, price] or name -> a small dataclass.
2. Build report lines in a list and "\n".join them.
3. Check every precondition before mutating anything.
"""


class OutOfStock(Exception):
    def __init__(self, name: str, available: int):
        raise NotImplementedError


class Inventory:
    def __init__(self):
        raise NotImplementedError

    def add(self, name: str, qty: int, price: float) -> None:
        raise NotImplementedError

    def remove(self, name: str, qty: int) -> int:
        raise NotImplementedError

    def total_value(self) -> float:
        raise NotImplementedError

    def low_stock(self, threshold: int) -> list[str]:
        raise NotImplementedError

    def report(self) -> str:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, name: str) -> bool:
        raise NotImplementedError


if __name__ == "__main__":
    inv = Inventory()
    assert len(inv) == 0 and inv.report() == f"{'TOTAL':<15}{0:>10.2f}", 'Check: len(inv) == 0 and inv.report() == f"{\'TOTAL\':<15}{0:>10.2f}"'
    inv.add("bolt", 100, 0.25)
    inv.add("nut", 3, 0.10)
    assert len(inv) == 2 and "nut" in inv and "screw" not in inv, 'Check: len(inv) == 2 and "nut" in inv and "screw" not in inv'
    assert abs(inv.total_value() - 25.30) < 1e-9, 'Check: abs(inv.total_value() - 25.30) < 1e-9'
    assert inv.report() == "bolt        100      0.25\nnut           3      0.10\nTOTAL               25.30", 'Check: inv.report() == "bolt 100 0.25\\nnut 3 0.10\\nTOTAL 25.30"'
    inv.add("nut", 2, 0.20)  # qty accumulates, price replaced
    assert abs(inv.total_value() - 26.0) < 1e-9, 'Check: abs(inv.total_value() - 26.0) < 1e-9'
    assert inv.remove("nut", 4) == 1, 'Check: inv.remove("nut", 4) == 1'
    try:
        inv.remove("nut", 5)
        assert False, 'Check: False'
    except OutOfStock as e:
        assert e.name == "nut" and e.available == 1, 'Check: e.name == "nut" and e.available == 1'
    try:
        inv.remove("screw", 1)
        assert False, 'Check: False'
    except KeyError:
        pass
    try:
        inv.add("x", 0, 1.0)
        assert False, 'Check: False'
    except ValueError:
        pass
    inv.add("washer", 1, 0.05)
    assert inv.remove("washer", 1) == 0 and "washer" in inv, 'Check: inv.remove("washer", 1) == 0 and "washer" in inv'
    assert inv.low_stock(1) == ["washer", "nut"], 'Check: inv.low_stock(1) == ["washer", "nut"]'
    assert inv.low_stock(0) == ["washer"], 'Check: inv.low_stock(0) == ["washer"]'
    assert inv.low_stock(1000) == ["washer", "nut", "bolt"], 'Check: inv.low_stock(1000) == ["washer", "nut", "bolt"]'
    print("ok")
