def find_min_arrow_shots(points):
    # O(n log n) time, O(1) extra space
    # Sort by end; an arrow at the current earliest end bursts every balloon that starts
    # at or before it. The first balloon starting later needs a fresh arrow.
    if not points:
        return 0
    points.sort(key=lambda p: p[1])
    arrows, shot_at = 1, points[0][1]
    for start, end in points[1:]:
        if start > shot_at:
            arrows += 1
            shot_at = end
    return arrows
