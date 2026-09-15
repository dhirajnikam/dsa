def length_of_longest_substring(s):
    # O(n) time, O(min(n, alphabet)) space
    # last[ch] = most recent index; when ch repeats inside the window, jump l past it.
    # max() guards against jumping backwards (e.g. "abba").
    last, l, best = {}, 0, 0
    for r, ch in enumerate(s):
        if ch in last and last[ch] >= l:
            l = last[ch] + 1
        last[ch] = r
        best = max(best, r - l + 1)
    return best
