def daily_temperatures(temperatures):
    # O(n) time, O(n) space
    # Stack holds indices with no warmer day yet (temps decreasing). A warmer day resolves
    # every colder index on top; each index is pushed and popped at most once.
    ans = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans
