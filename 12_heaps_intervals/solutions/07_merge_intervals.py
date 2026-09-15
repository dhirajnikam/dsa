def merge(intervals):
    # O(n log n) time, O(n) space
    # After sorting by start, each interval either extends the last merged one or starts a new one.
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
