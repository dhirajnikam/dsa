def jump(nums):
    # O(n) time, O(1) space
    # [.., end] is the frontier reachable with `jumps` jumps; when we hit end, jump to the
    # farthest index any frontier element can reach. We never need to visit the last index.
    jumps = end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == end:
            jumps += 1
            end = farthest
    return jumps
