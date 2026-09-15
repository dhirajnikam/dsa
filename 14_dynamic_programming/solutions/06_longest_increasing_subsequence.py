from bisect import bisect_left


def length_of_lis(nums):
    # O(n log n) time, O(n) space
    # tails[k] = smallest possible tail of an increasing subsequence of length k+1.
    # Each x replaces the first tail >= x (keeps tails minimal) or extends the list.
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def length_of_lis_quadratic(nums):
    # O(n^2) time, O(n) space
    # dp[i] = 1 + max(dp[j] for j < i with nums[j] < nums[i]); answer is max(dp).
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
