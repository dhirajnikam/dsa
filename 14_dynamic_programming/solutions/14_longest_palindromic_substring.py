def longest_palindrome(s):
    # O(n^2) time, O(1) space
    # Every palindrome has a center (one char or a gap between two). Expand from each of
    # the 2n-1 centers while the ends match; keep the earliest longest.
    best_start, best_len = 0, 0
    for center in range(len(s)):
        for lo, hi in ((center, center), (center, center + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            if hi - lo - 1 > best_len:
                best_start, best_len = lo + 1, hi - lo - 1
    return s[best_start:best_start + best_len]
