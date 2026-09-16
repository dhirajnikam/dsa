"""02 · Two Pointers & Sliding Window — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
from collections import Counter, deque


def valid_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
    # O(n) time, O(1) space. Each pointer only moves inward.


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l + 1, r + 1]
        if s < target:
            l += 1                    # too small: no pair using l can work, discard it
        else:
            r -= 1
    return []
    # O(n) time, O(1) space.


def remove_duplicates_sorted(nums: list[int]) -> int:
    if not nums:
        return 0
    write = 1                         # nums[0] always stays
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write
    # O(n) time, O(1) space. write <= read always, so we never overwrite unread data.


def best_time_stock(prices: list[int]) -> int:
    lowest = float("inf")
    best = 0
    for p in prices:
        lowest = min(lowest, p)       # cheapest buy so far
        best = max(best, p - lowest)  # sell today against that buy
    return best
    # O(n) time, O(1) space. Two pointers in spirit: buy day trails, sell day leads.


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    out: list[list[int]] = []
    for i in range(n - 2):
        if nums[i] > 0:
            break                     # everything after is positive: no zero sum possible
        if i > 0 and nums[i] == nums[i - 1]:
            continue                  # same first element as before -> same triplets
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                out.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1            # skip duplicate second elements
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1            # skip duplicate third elements
    return out
    # O(n^2) time (sort O(n log n) + n two-pointer sweeps), O(1) extra beyond the output.


def container_most_water(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        best = max(best, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1                    # shorter wall limits the area; it is done
        else:
            r -= 1
    return best
    # O(n) time, O(1) space.


def longest_substring_no_repeat(s: str) -> int:
    seen: set[str] = set()
    left = best = 0
    for right, c in enumerate(s):
        while c in seen:              # shrink until c is no longer duplicated
            seen.discard(s[left])
            left += 1
        seen.add(c)
        best = max(best, right - left + 1)
    return best
    # O(n) time: left and right each move at most n times. O(min(n, alphabet)) space.


def longest_repeating_char_replacement(s: str, k: int) -> int:
    counts: dict[str, int] = {}
    left = best = max_count = 0
    for right, c in enumerate(s):
        counts[c] = counts.get(c, 0) + 1
        max_count = max(max_count, counts[c])
        if (right - left + 1) - max_count > k:   # too many letters to replace
            counts[s[left]] -= 1
            left += 1                 # one step is enough: window size never needs to shrink
        best = max(best, right - left + 1)
    return best
    # O(n) time, O(26) space. max_count may be stale but never too low for a valid window,
    # so the window length only grows when a genuinely valid longer window appears.


def check_permutation_in_string(s1: str, s2: str) -> bool:
    k = len(s1)
    if k > len(s2):
        return False
    need = Counter(s1)
    window: Counter = Counter()
    for right, c in enumerate(s2):
        window[c] += 1                # one in
        if right >= k:
            out = s2[right - k]       # one out
            window[out] -= 1
            if window[out] == 0:
                del window[out]
        if right >= k - 1 and window == need:
            return True
    return False
    # O(n * 26) -> O(n) time, O(26) space. Fixed window of size k.


def min_window_substring(s: str, t: str) -> str:
    if not t or len(t) > len(s):
        return ""
    need = Counter(t)
    window: dict[str, int] = {}
    have, required = 0, len(need)     # how many distinct letters are currently satisfied
    best = (float("inf"), 0, 0)       # (length, left, right)
    left = 0
    for right, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        if c in need and window[c] == need[c]:
            have += 1
        while have == required:       # valid: record, then shrink to find a shorter one
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)
            out = s[left]
            window[out] -= 1
            if out in need and window[out] < need[out]:
                have -= 1
            left += 1
    return "" if best[0] == float("inf") else s[best[1]: best[2] + 1]
    # O(|s| + |t|) time, O(alphabet) space.


def trapping_rain_water(height: list[int]) -> int:
    if not height:
        return 0
    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    water = 0
    while l < r:
        if left_max <= right_max:     # the left side's water level is settled by left_max
            l += 1
            left_max = max(left_max, height[l])
            water += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            water += right_max - height[r]
    return water
    # O(n) time, O(1) space. Water at i = min(max_left, max_right) - h[i]; the smaller
    # running max is already the binding one, so that side can be finalized.


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    dq: deque[int] = deque()          # indices; nums values decreasing front -> back
    out: list[int] = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()                  # older and not bigger: never a future max
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()              # front left the window
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
    # O(n) time: each index is pushed and popped at most once. O(k) space.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
