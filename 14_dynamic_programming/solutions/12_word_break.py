def word_break(s, word_dict):
    # O(n * W * L) time, O(n) space (W words, L max word length)
    # dp[i] = s[:i] is segmentable = any(dp[i - len(w)] and s ends with w at i).
    words = set(word_dict)
    lengths = {len(w) for w in words}
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        dp[i] = any(dp[i - L] and s[i - L:i] in words for L in lengths if L <= i)
    return dp[-1]
