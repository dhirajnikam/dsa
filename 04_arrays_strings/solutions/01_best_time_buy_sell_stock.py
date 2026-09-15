def max_profit(prices):
    # O(n) time, O(1) space
    # Cheapest price so far is the only buy worth considering for today's sell.
    lo, best = prices[0], 0
    for p in prices:
        lo = min(lo, p)
        best = max(best, p - lo)
    return best
