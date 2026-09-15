from collections import Counter


def min_window(s, t):
    # O(|s| + |t|) time, O(alphabet) space
    # `have` counts distinct chars whose window count meets need[ch]; the window is valid when
    # have == len(need). Expand r, then shrink l while valid, recording the smallest span.
    need = Counter(t)
    window = Counter()
    have, l = 0, 0
    best = (float("inf"), 0, 0)
    for r, ch in enumerate(s):
        window[ch] += 1
        if ch in need and window[ch] == need[ch]:
            have += 1
        while have == len(need):
            if r - l + 1 < best[0]:
                best = (r - l + 1, l, r)
            left = s[l]
            window[left] -= 1
            if left in need and window[left] < need[left]:
                have -= 1
            l += 1
    return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]
