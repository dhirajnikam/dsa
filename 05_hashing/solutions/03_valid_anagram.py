from collections import Counter


def is_anagram(s, t):
    # O(n) time, O(1) space (26 keys max)
    # Anagram means identical multisets of characters; Counter compares them directly.
    return len(s) == len(t) and Counter(s) == Counter(t)
