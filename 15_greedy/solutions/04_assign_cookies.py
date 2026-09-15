def find_content_children(g, s):
    # O(n log n + m log m) time, O(1) extra space
    # Sorted two-pointer scan: each cookie either satisfies the current least-greedy child
    # or is too small for everyone remaining and is skipped.
    g, s = sorted(g), sorted(s)
    child = 0
    for cookie in s:
        if child < len(g) and cookie >= g[child]:
            child += 1
    return child
