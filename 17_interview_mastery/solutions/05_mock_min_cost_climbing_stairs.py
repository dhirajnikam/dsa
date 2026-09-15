# What a strong candidate says:
# "Do I start on stair 0 or 1, and is the top one past the last stair with cost 0? Then
#  the min cost to stand on stair i is cost[i] plus the cheaper of standing on i-1 or i-2.
#  That recurrence has overlapping subproblems, so it is DP, not greedy: a cheap step now
#  can force an expensive one later. O(n) array first, then just two rolling variables."


def min_cost_climbing_stairs(cost):
    # O(n) time, O(1) space
    # a, b = min cost to stand on stairs i-2 and i-1; the top is reachable from either of
    # the last two stairs, so the answer is min of the final pair.
    a, b = cost[0], cost[1]
    for c in cost[2:]:
        a, b = b, c + min(a, b)
    return min(a, b)
