from collections import defaultdict


def group_anagrams(strs):
    # O(n * k) time, O(n * k) space
    # Canonical key = tuple of 26 letter counts; anagrams collide on it, nothing else does.
    groups = defaultdict(list)
    for w in strs:
        key = [0] * 26
        for ch in w:
            key[ord(ch) - 97] += 1
        groups[tuple(key)].append(w)
    return list(groups.values())
