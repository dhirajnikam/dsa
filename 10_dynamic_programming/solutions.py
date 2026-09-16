"""10 · Dynamic Programming — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
from bisect import bisect_left
from functools import lru_cache


def climbing_stairs(n: int) -> int:
    a, b = 1, 1                        # ways(i-2), ways(i-1); ways(0) = ways(1) = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
    # O(n) time, O(1) space. Stage 3 (memoized) version, for the record:
    #   @lru_cache(maxsize=None)
    #   def ways(i): return 1 if i <= 1 else ways(i - 1) + ways(i - 2)


def min_cost_climbing_stairs(cost: list[int]) -> int:
    prev2, prev1 = cost[0], cost[1]    # cheapest way to stand on stair i-2, i-1
    for c in cost[2:]:
        prev2, prev1 = prev1, c + min(prev1, prev2)
    return min(prev1, prev2)           # the top is reachable from either of the last two
    # O(n) time, O(1) space.


def house_robber(nums: list[int]) -> int:
    prev2 = prev1 = 0                  # best using houses up to i-2, up to i-1
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)   # skip house i, or take it
    return prev1
    # O(n) time, O(1) space.


def house_robber_ii(nums: list[int]) -> int:
    if len(nums) <= 1:
        return sum(nums)
    return max(house_robber(nums[1:]), house_robber(nums[:-1]))
    # First and last cannot both be taken, so one of them is excluded. O(n).


def longest_palindromic_substring(s: str) -> str:
    best_lo, best_hi = 0, 1            # s[best_lo:best_hi]

    def expand(lo: int, hi: int) -> None:
        nonlocal best_lo, best_hi
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        if hi - lo - 1 > best_hi - best_lo:
            best_lo, best_hi = lo + 1, hi

    for center in range(len(s)):
        expand(center, center)         # odd length, centered on a letter
        expand(center, center + 1)     # even length, centered between two letters
    return s[best_lo:best_hi]
    # O(n^2) time, O(1) space. 2n-1 centers, each expansion up to O(n).


def count_palindromic_substrings(s: str) -> int:
    count = 0
    for center in range(len(s)):
        for lo, hi in ((center, center), (center, center + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                count += 1             # every successful expansion is one more palindrome
                lo -= 1
                hi += 1
    return count
    # O(n^2) time, O(1) space.


def decode_ways(s: str) -> int:
    if not s or s[0] == "0":
        return 0
    prev2, prev1 = 1, 1                # dp[0] = 1 (empty prefix), dp[1] = 1 (first digit valid)
    for i in range(2, len(s) + 1):
        cur = 0
        if s[i - 1] != "0":                       # last digit alone
            cur += prev1
        if 10 <= int(s[i - 2:i]) <= 26:           # last two digits together
            cur += prev2
        prev2, prev1 = prev1, cur
    return prev1
    # dp[i] = ways to decode s[:i]. O(n) time, O(1) space.


def coin_change(coins: list[int], amount: int) -> int:
    INF = float("inf")
    dp = [0] + [INF] * amount          # dp[a] = fewest coins that make a
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1
    # Unbounded knapsack. O(amount * len(coins)) time, O(amount) space.


def coin_change_ii(coins: list[int], amount: int) -> int:
    dp = [1] + [0] * amount            # dp[a] = combinations that make a; one way to make 0
    for c in coins:                    # coins outside so each combination is counted once
        for a in range(c, amount + 1): # upward: the same coin may be reused
            dp[a] += dp[a - c]
    return dp[amount]
    # O(amount * len(coins)) time, O(amount) space.


def max_product_subarray(nums: list[int]) -> int:
    best = cur_max = cur_min = nums[0]
    for x in nums[1:]:
        if x < 0:
            cur_max, cur_min = cur_min, cur_max   # a negative flips biggest and smallest
        cur_max = max(x, cur_max * x)
        cur_min = min(x, cur_min * x)
        best = max(best, cur_max)
    return best
    # Kadane with two running values. O(n) time, O(1) space.


def word_break(s: str, words: list[str]) -> bool:
    ws = set(words)
    dp = [True] + [False] * len(s)     # dp[i]: s[:i] can be segmented
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in ws:
                dp[i] = True
                break
    return dp[len(s)]
    # O(n^2) substring checks, each O(n) to slice -> O(n^3) worst case; fine for interview sizes.
    # Bounding j by the longest word length makes it O(n * L).


def length_of_lis(nums: list[int]) -> int:
    tails: list[int] = []              # tails[k] = smallest tail of an increasing subseq of length k+1
    for x in nums:
        k = bisect_left(tails, x)      # first tail >= x
        if k == len(tails):
            tails.append(x)            # x extends the longest subsequence
        else:
            tails[k] = x               # x is a smaller tail for length k+1
    return len(tails)
    # O(n log n) time, O(n) space. The O(n^2) version is in LESSON.md.


def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)        # dp[s]: some subset sums to s
    dp[0] = True
    for x in nums:
        for s in range(target, x - 1, -1):   # downward: each number used at most once
            if dp[s - x]:
                dp[s] = True
    return dp[target]
    # 0/1 knapsack. O(n * total) time, O(total) space.


def unique_paths(m: int, n: int) -> int:
    row = [1] * n                      # first row: one way to reach each cell
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]       # from above (old row[c]) plus from the left
    return row[-1]
    # O(m * n) time, O(n) space.


def longest_common_subsequence(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]   # dp[i][j] = LCS of s[:i], t[:j]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
    # O(m * n) time and space. Two rows suffice for O(n) space.


def edit_distance(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]   # dp[i][j] = edits to turn s[:i] into t[:j]
    for i in range(m + 1):
        dp[i][0] = i                   # delete everything
    for j in range(n + 1):
        dp[0][j] = j                   # insert everything
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],       # delete s[i-1]
                                   dp[i][j - 1],       # insert t[j-1]
                                   dp[i - 1][j - 1])   # replace
    return dp[m][n]
    # O(m * n) time and space.


def max_profit_with_cooldown(prices: list[int]) -> int:
    hold = float("-inf")               # best profit while holding a share
    sold = 0                           # best profit having sold today (cooldown tomorrow)
    rest = 0                           # best profit with no share and free to buy
    for p in prices:
        hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
    return max(sold, rest)
    # State machine, O(n) time, O(1) space.


def target_sum_ways(nums: list[int], target: int) -> int:
    total = sum(nums)
    if abs(target) > total or (target + total) % 2:
        return 0
    plus = (target + total) // 2       # the '+' subset must sum to exactly this
    dp = [0] * (plus + 1)              # dp[s] = subsets summing to s
    dp[0] = 1
    for x in nums:
        for s in range(plus, x - 1, -1):
            dp[s] += dp[s - x]
    return dp[plus]
    # 0/1 subset counting. O(n * total) time, O(total) space.


def interleaving_string(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]   # dp[i][j]: s1[:i], s2[:j] form s3[:i+j]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            k = i + j - 1
            if i and dp[i - 1][j] and s1[i - 1] == s3[k]:
                dp[i][j] = True
            if j and dp[i][j - 1] and s2[j - 1] == s3[k]:
                dp[i][j] = True
    return dp[m][n]
    # O(m * n) time and space.


def burst_balloons(nums: list[int]) -> int:
    a = [1] + nums + [1]               # virtual 1s at both ends
    n = len(a)
    dp = [[0] * n for _ in range(n)]   # dp[l][r] = best for balloons strictly between l and r
    for length in range(2, n):         # r - l
        for l in range(n - length):
            r = l + length
            for k in range(l + 1, r):  # k is the LAST balloon to burst in (l, r)
                dp[l][r] = max(dp[l][r], a[l] * a[k] * a[r] + dp[l][k] + dp[k][r])
    return dp[0][n - 1]
    # Interval DP. O(n^3) time, O(n^2) space.


def regex_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]   # dp[i][j]: p[:j] matches s[:i]
    dp[0][0] = True
    for j in range(2, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]    # "x*" can match the empty string
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                zero = dp[i][j - 2]                       # use zero copies of p[j-2]
                one_more = dp[i - 1][j] and p[j - 2] in (s[i - 1], ".")   # consume s[i-1]
                dp[i][j] = zero or one_more
            else:
                dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in (s[i - 1], ".")
    return dp[m][n]
    # O(m * n) time and space.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
