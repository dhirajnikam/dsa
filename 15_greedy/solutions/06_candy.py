def candy(ratings):
    # O(n) time, O(n) space
    # Pass 1 satisfies every "higher than left neighbour" constraint; pass 2 satisfies
    # "higher than right neighbour" and takes max so pass 1's result is never lowered.
    n = len(ratings)
    res = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            res[i] = res[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            res[i] = max(res[i], res[i + 1] + 1)
    return sum(res)
