def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq


def first_unique_char(s):
    freq = char_frequency(s)
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1


def common_elements(a, b):
    return sorted(set(a) & set(b))


def invert_dict(d):
    return {v: k for k, v in d.items()}
