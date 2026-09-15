def largest_rectangle_area(heights):
    # O(n) time, O(n) space
    # Increasing stack of indices. Popping bar j when a shorter bar i arrives fixes j's right
    # edge at i and left edge at the new stack top; a trailing 0 sentinel flushes the stack.
    stack, best = [], 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            top = heights[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, top * (i - left - 1))
        stack.append(i)
    return best
