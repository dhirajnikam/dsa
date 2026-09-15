import time
from functools import wraps


def count_calls(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return f(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def timed(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return f(*args, **kwargs)
        finally:
            wrapper.last_elapsed = time.perf_counter() - start
    wrapper.last_elapsed = 0.0
    return wrapper


def retry(times, exceptions=(Exception,)):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            wrapper.attempts = 0
            last = None
            for _ in range(times):
                wrapper.attempts += 1
                try:
                    return f(*args, **kwargs)
                except exceptions as e:
                    last = e
            raise last
        wrapper.attempts = 0
        return wrapper
    return decorator
