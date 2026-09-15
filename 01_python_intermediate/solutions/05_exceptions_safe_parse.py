def safe_int(s, default=None):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default


def parse_ints(strs):
    ints, bad = [], []
    for i, s in enumerate(strs):
        try:
            ints.append(int(s))
        except ValueError:
            bad.append(i)
    return ints, bad


class NegativeError(ValueError):
    def __init__(self, value):
        super().__init__(f"cannot take sqrt of negative number {value}")
        self.value = value


def checked_sqrt(x):
    if x < 0:
        raise NegativeError(x)
    return x ** 0.5


def divide_all(pairs, log):
    out = []
    try:
        for a, b in pairs:
            try:
                out.append(a / b)
            except ZeroDivisionError:
                out.append(None)
    finally:
        log.append("done")
    return out


def first_failure(funcs):
    for i, f in enumerate(funcs):
        try:
            f()
        except Exception:
            return i
    return -1
