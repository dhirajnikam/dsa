def is_isomorphic(s, t):
    # O(n) time, O(1) space
    # A valid replacement is a bijection: enforce s->t and t->s consistency together.
    fwd, back = {}, {}
    for a, b in zip(s, t):
        if fwd.setdefault(a, b) != b or back.setdefault(b, a) != a:
            return False
    return True
