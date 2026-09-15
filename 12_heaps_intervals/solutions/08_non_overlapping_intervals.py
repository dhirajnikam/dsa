def erase_overlap_intervals(intervals):
    # O(n log n) time, O(1) extra space
    # Sort by end; greedily keep every interval that starts after the last kept end.
    # Removed = total - kept.
    intervals.sort(key=lambda iv: iv[1])
    kept, last_end = 0, float("-inf")
    for start, end in intervals:
        if start >= last_end:
            kept += 1
            last_end = end
    return len(intervals) - kept
