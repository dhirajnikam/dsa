import heapq


def min_meeting_rooms(intervals):
    # O(n log n) time, O(n) space
    # Sort by start; a min-heap of end times is the set of busy rooms. Free the earliest-ending
    # room if it ends by this start, then occupy one. Peak heap size is the answer.
    ends = []
    best = 0
    for start, end in sorted(intervals):
        if ends and ends[0] <= start:
            heapq.heapreplace(ends, end)
        else:
            heapq.heappush(ends, end)
        best = max(best, len(ends))
    return best
