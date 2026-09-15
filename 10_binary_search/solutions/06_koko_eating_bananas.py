# O(n log(max(piles))) time, O(1) space
# Feasible(k) = total hours at speed k <= h; it is monotonic in k, so find the first feasible k.
def min_eating_speed(piles: list[int], h: int) -> int:
    def hours(k: int) -> int:
        return sum((p + k - 1) // k for p in piles)

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
