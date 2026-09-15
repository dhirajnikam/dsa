def max_area(height):
    # O(n) time, O(1) space
    # Start widest; the shorter side caps the area, so only moving it inward can improve things.
    l, r, best = 0, len(height) - 1, 0
    while l < r:
        best = max(best, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best
