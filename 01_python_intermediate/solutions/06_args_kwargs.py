def total(*args):
    return sum(args)


def build_query(**kwargs):
    return "&".join(f"{k}={v}" for k, v in sorted(kwargs.items()))


def call_with(f, args, kwargs):
    return f(*args, **kwargs)


def merge_dicts(*dicts):
    out = {}
    for d in dicts:
        out.update(d)
    return out


def first_last_middle(seq):
    first, *middle, last = seq
    return first, last, middle


def describe(name, *, age, city="?"):
    return f"{name} ({age}) from {city}"
