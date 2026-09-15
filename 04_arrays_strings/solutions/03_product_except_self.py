def product_except_self(nums):
    # O(n) time, O(1) extra space
    # out[i] = prefix product (forward pass) * suffix product (backward pass, running scalar).
    n = len(nums)
    out = [1] * n
    for i in range(1, n):
        out[i] = out[i - 1] * nums[i - 1]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out
