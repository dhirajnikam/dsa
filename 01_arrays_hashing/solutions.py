"""01 · Arrays & Hashing — reference solutions.

Honor rule: 40 minutes on a problem first. Read one function, close the file, rewrite it cold,
add it to redo.txt. Run `python solutions.py` to prove these pass exercises.py's tests.
"""
import random
from collections import Counter, defaultdict


def contains_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) < len(nums)
    # O(n) time and space. Sorting gives O(n log n) time, O(1) extra space: mention the trade.


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i                   # record after checking, so i is never reused
    return []


def is_anagram(s: str, t: str) -> bool:
    return len(s) == len(t) and Counter(s) == Counter(t)
    # 26-slot list variant: counts[ord(c) - 97] += 1 for s, -= 1 for t, then all zero.


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[tuple, list[str]] = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)   # canonical key; a 26-count tuple is O(k) instead
    return list(groups.values())


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]   # index = frequency
    for x, c in counts.items():
        buckets[c].append(x)
    out: list[int] = []
    for c in range(len(nums), 0, -1):          # walk from highest frequency down
        out.extend(buckets[c])
        if len(out) >= k:
            return out[:k]
    return out
    # O(n). Heap version: heapq.nlargest(k, counts, key=counts.get) -> O(n log k).


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):                 # out[i] = product of everything to the left
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):     # multiply in product of everything to the right
        out[i] *= right
        right *= nums[i]
    return out


def max_subarray(nums: list[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)          # extend, or start fresh at x
        best = max(best, cur)
    return best


def subarray_sum_k(nums: list[int], k: int) -> int:
    seen = {0: 1}                      # the empty prefix sums to 0
    prefix = count = 0
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


def longest_consecutive(nums: list[int]) -> int:
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 in s:                 # not the start of a run; skip
            continue
        length = 1
        while x + length in s:
            length += 1
        best = max(best, length)
    return best
    # Each number is the start of at most one run, and each is stepped over once -> O(n).


def encode(strs: list[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(s: str) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(s):
        j = s.index("#", i)            # digits from i to j are the length
        length = int(s[i:j])
        out.append(s[j + 1: j + 1 + length])
        i = j + 1 + length
    return out


class RandomizedSet:
    def __init__(self) -> None:
        self.vals: list[int] = []
        self.pos: dict[int, int] = {}          # value -> index in vals

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        i, last = self.pos[val], self.vals[-1]
        self.vals[i], self.pos[last] = last, i   # move last element into the hole
        self.vals.pop()
        del self.pos[val]
        return True

    def get_random(self) -> int:
        return random.choice(self.vals)


def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    for i in range(n):
        # keep swapping until slot i holds i+1 or something that cannot be placed
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
    # Each swap places one value in its final slot, so total swaps <= n -> O(n), O(1) space.


if __name__ == "__main__":
    import exercises
    for _k, _v in list(globals().items()):
        if not _k.startswith("_") and _k != "exercises":
            setattr(exercises, _k, _v)
    exercises._check()
