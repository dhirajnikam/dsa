def rob(nums):
    # O(n) time, O(1) space
    # Circle means house 0 and house n-1 cannot both be robbed: solve the linear problem
    # on nums[1:] and on nums[:-1] and take the better one.
    def linear(houses):
        prev2 = prev1 = 0
        for x in houses:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1

    if len(nums) == 1:
        return nums[0]
    return max(linear(nums[1:]), linear(nums[:-1]))
