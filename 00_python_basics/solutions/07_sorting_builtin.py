def sort_by_length(words):
    return sorted(words, key=len)


def sort_people(people):
    return sorted(people, key=lambda p: (p[1], p[0]))


def top_k_frequent_words(words, k):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return sorted(counts, key=lambda w: (-counts[w], w))[:k]


def sort_by_parity(nums):
    return sorted(nums, key=lambda x: x % 2)
