"""
Problem: Three decorators
Difficulty: Easy | Topic: decorators, functools.wraps, decorators with arguments

1. count_calls(f): decorator. The wrapped function gets a .calls attribute counting invocations.
2. timed(f): decorator. After each call, wrapper.last_elapsed holds the seconds the call took
   (a float >= 0). Use time.perf_counter(). The return value must pass through unchanged.
3. retry(times, exceptions=(Exception,)): decorator WITH arguments. Call f up to `times` times;
   return the first successful result. If every attempt raises one of `exceptions`, re-raise the
   last one. Exceptions not in `exceptions` propagate immediately (no retry).
   The wrapped function gets .attempts = number of calls made during the most recent invocation.

All three must preserve the original __name__ and __doc__ (use functools.wraps).

Hints:
1. Set wrapper.calls = 0 after defining wrapper, increment inside it.
3. Structure: def retry(times, exceptions=...): def decorator(f): def wrapper(*a, **k): ... return wrapper; return decorator
3. Keep the last exception in a variable and `raise last` after the loop.
"""
import time
from functools import wraps


def count_calls(f):
    raise NotImplementedError


def timed(f):
    raise NotImplementedError


def retry(times: int, exceptions=(Exception,)):
    raise NotImplementedError


if __name__ == "__main__":
    @count_calls
    def add(a, b):
        """Add two numbers."""
        return a + b

    assert add.calls == 0, 'Check: add.calls == 0'
    assert add(1, 2) == 3 and add(3, 4) == 7, 'Check: add(1, 2) == 3 and add(3, 4) == 7'
    assert add.calls == 2, 'Check: add.calls == 2'
    assert add.__name__ == "add" and add.__doc__ == "Add two numbers.", 'Check: add.__name__ == "add" and add.__doc__ == "Add two numbers."'

    @timed
    def slow(n):
        return sum(range(n))

    assert slow(1000) == 499500, 'Check: slow(1000) == 499500'
    assert isinstance(slow.last_elapsed, float) and slow.last_elapsed >= 0, 'Check: isinstance(slow.last_elapsed, float) and slow.last_elapsed >= 0'
    assert slow.__name__ == "slow", 'Check: slow.__name__ == "slow"'

    state = {"fails": 2}

    @retry(3, exceptions=(ValueError,))
    def flaky():
        """Fails twice then works."""
        if state["fails"] > 0:
            state["fails"] -= 1
            raise ValueError("not yet")
        return "done"

    assert flaky() == "done" and flaky.attempts == 3, 'Check: flaky() == "done" and flaky.attempts == 3'
    assert flaky() == "done" and flaky.attempts == 1, 'Check: flaky() == "done" and flaky.attempts == 1'
    assert flaky.__name__ == "flaky" and flaky.__doc__ == "Fails twice then works.", 'Check: flaky.__name__ == "flaky" and flaky.__doc__ == "Fails twice then works."'

    @retry(2)
    def always_fails():
        raise KeyError("nope")

    try:
        always_fails()
        assert False, 'Check: False'
    except KeyError:
        assert always_fails.attempts == 2, 'Check: always_fails.attempts == 2'

    calls = []

    @retry(5, exceptions=(ValueError,))
    def wrong_kind():
        calls.append(1)
        raise TypeError("no retry for me")

    try:
        wrong_kind()
        assert False, 'Check: False'
    except TypeError:
        assert len(calls) == 1, 'Check: len(calls) == 1'
    print("ok")
