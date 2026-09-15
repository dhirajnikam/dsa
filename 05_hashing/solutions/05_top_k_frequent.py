from collections import Counter


def top_k_frequent(nums, k):
    # O(n) time, O(n) space
    # Bucket sort on frequency: a value's count is at most n, so buckets[count] is bounded.
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for v, c in counts.items():
        buckets[c].append(v)
    out = []
    for c in range(len(nums), 0, -1):
        out.extend(buckets[c])
        if len(out) >= k:
            return out[:k]
    return out
