def can_jump(nums):
    # O(n) time, O(1) space
    # farthest is the max index reachable using indices seen so far; a gap means failure.
    farthest = 0
    for i, step in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + step)
    return True
