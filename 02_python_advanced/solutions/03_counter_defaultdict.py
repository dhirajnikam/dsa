from collections import Counter, defaultdict


def top_k_words(words, k):  # O(n log n) time, O(n) space
    ranked = sorted(Counter(words).items(), key=lambda kv: (-kv[1], kv[0]))
    return [w for w, _ in ranked[:k]]


def group_anagrams(words):  # O(n * L log L) time
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())


def missing_letters(word, magazine):
    return Counter(word) - Counter(magazine)


def first_unique_char(s):  # O(n) time, O(1) space (alphabet-bounded)
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1


def group_by_length(words):
    groups = defaultdict(set)
    for w in words:
        groups[len(w)].add(w)
    return {k: sorted(v) for k, v in groups.items()}
