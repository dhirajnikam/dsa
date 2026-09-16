"""
Problem: Exceptions as control flow done right
Difficulty: Easy | Topic: try/except/else/finally, custom exceptions, exception chaining

1. safe_int(s, default=None): int(s) or default if it cannot be parsed. Must accept " 42 ".
   Never raises. safe_int(None) -> default.
2. parse_ints(strs) -> (ints, bad_indexes). Parse every string; collect successes in order and
   the indexes of failures. ["1", "x", "3"] -> ([1, 3], [1])
3. class NegativeError(ValueError) with attribute .value set to the offending number.
   checked_sqrt(x): return x ** 0.5, raise NegativeError(x) if x < 0.
4. divide_all(pairs, log) -> list of a / b for each (a, b). On ZeroDivisionError append None
   instead. Whatever happens, log must get the string "done" appended exactly once per call,
   even if a pair contains non-numbers and the TypeError propagates out.
5. first_failure(funcs) -> index of the first zero-arg function that raises, or -1 if none does.
   Functions after the first failure must not be called.

Hints:
1. try: return int(s) except (ValueError, TypeError): return default
3. class NegativeError(ValueError): def __init__(self, value): super().__init__(f"..."); self.value = value
4. Put the log append in a `finally` block.
"""


def safe_int(s, default=None):
    raise NotImplementedError


def parse_ints(strs: list[str]) -> tuple[list[int], list[int]]:
    raise NotImplementedError


class NegativeError(ValueError):
    def __init__(self, value):
        raise NotImplementedError


def checked_sqrt(x: float) -> float:
    raise NotImplementedError


def divide_all(pairs: list[tuple], log: list[str]) -> list:
    raise NotImplementedError


def first_failure(funcs: list) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert safe_int("42") == 42 and safe_int(" 42 ") == 42, 'Check: safe_int("42") == 42 and safe_int(" 42 ") == 42'
    assert safe_int("4.2") is None and safe_int("x", 0) == 0 and safe_int(None, -1) == -1, 'Check: safe_int("4.2") is None and safe_int("x", 0) == 0 and safe_int(None, -1) == -1'
    assert parse_ints(["1", "x", "3", ""]) == ([1, 3], [1, 3]), 'Check: parse_ints(["1", "x", "3", ""]) == ([1, 3], [1, 3])'
    assert parse_ints([]) == ([], []), 'Check: parse_ints([]) == ([], [])'
    assert checked_sqrt(9) == 3.0, 'Check: checked_sqrt(9) == 3.0'
    try:
        checked_sqrt(-4)
        assert False, 'Check: False'
    except NegativeError as e:
        assert e.value == -4 and isinstance(e, ValueError), 'Check: e.value == -4 and isinstance(e, ValueError)'
    log = []
    assert divide_all([(6, 3), (1, 0), (5, 2)], log) == [2.0, None, 2.5], 'Check: divide_all([(6, 3), (1, 0), (5, 2)], log) == [2.0, None, 2.5]'
    assert log == ["done"], 'Check: log == ["done"]'
    try:
        divide_all([(1, "a")], log)
        assert False, 'Check: False'
    except TypeError:
        pass
    assert log == ["done", "done"], 'Check: log == ["done", "done"]'
    calls = []
    fs = [lambda: calls.append(0), lambda: 1 / 0, lambda: calls.append(2)]
    assert first_failure(fs) == 1 and calls == [0], 'Check: first_failure(fs) == 1 and calls == [0]'
    assert first_failure([lambda: 1]) == -1, 'Check: first_failure([lambda: 1]) == -1'
    assert first_failure([]) == -1, 'Check: first_failure([]) == -1'
    print("ok")
