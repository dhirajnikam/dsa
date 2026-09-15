from collections import deque


def max_sliding_window(nums, k):
    # O(n) time, O(k) space
    # Deque holds indices with decreasing values; a new element evicts smaller ones from
    # the back (they can never be a future max), the front expires when it leaves the window.
    dq, out = deque(), []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
