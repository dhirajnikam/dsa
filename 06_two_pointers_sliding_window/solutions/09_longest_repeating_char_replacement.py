from collections import Counter


def character_replacement(s, k):
    # O(n) time, O(1) space
    # Window is valid iff len - max_freq <= k. max_freq is a historical max: it never needs to
    # shrink because the answer only grows when a window with a higher max_freq appears.
    counts = Counter()
    l = max_freq = best = 0
    for r, ch in enumerate(s):
        counts[ch] += 1
        max_freq = max(max_freq, counts[ch])
        while (r - l + 1) - max_freq > k:
            counts[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best
