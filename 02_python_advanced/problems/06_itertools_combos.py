"""
Problem: itertools toolbox
Difficulty: Easy | Topic: combinations, product, permutations, accumulate, groupby, chain

1. pairs_with_sum(nums, target) -> number of index pairs i < j with nums[i] + nums[j] == target.
   Use combinations. [1,2,3,4,3], 6 -> 2 pairs ((2,4) and (3,3)).
2. dice_sum_counts(dice, sides) -> dict sum -> number of ways when rolling `dice` dice.
   Use product(range(1, sides+1), repeat=dice). dice_sum_counts(2, 6)[7] == 6.
3. prefix_maxes(nums) -> list of running maximums using accumulate with max.
4. run_length_encode(s) -> "aaabcc" -> [("a", 3), ("b", 1), ("c", 2)] using groupby.
5. flatten_all(lists) -> one list from a list of lists using chain.from_iterable.
6. distinct_permutations(s) -> sorted list of distinct strings from permuting s.
   distinct_permutations("aab") -> ["aab", "aba", "baa"].

Hints:
1. sum(1 for a, b in combinations(nums, 2) if a + b == target)
3. list(accumulate(nums, max))
4. [(ch, len(list(g))) for ch, g in groupby(s)]
6. sorted(set("".join(p) for p in permutations(s)))  (fine for len(s) <= 8)
"""
from itertools import accumulate, chain, combinations, groupby, permutations, product


def pairs_with_sum(nums: list[int], target: int) -> int:
    raise NotImplementedError


def dice_sum_counts(dice: int, sides: int) -> dict[int, int]:
    raise NotImplementedError


def prefix_maxes(nums: list[int]) -> list[int]:
    raise NotImplementedError


def run_length_encode(s: str) -> list[tuple[str, int]]:
    raise NotImplementedError


def flatten_all(lists: list[list]) -> list:
    raise NotImplementedError


def distinct_permutations(s: str) -> list[str]:
    raise NotImplementedError


if __name__ == "__main__":
    assert pairs_with_sum([1, 2, 3, 4, 3], 6) == 2
    assert pairs_with_sum([3, 3, 3], 6) == 3 and pairs_with_sum([], 1) == 0
    d = dice_sum_counts(2, 6)
    assert d[2] == 1 and d[7] == 6 and d[12] == 1 and sum(d.values()) == 36
    assert dice_sum_counts(1, 4) == {1: 1, 2: 1, 3: 1, 4: 1}
    assert prefix_maxes([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5] and prefix_maxes([]) == []
    assert run_length_encode("aaabcc") == [("a", 3), ("b", 1), ("c", 2)]
    assert run_length_encode("") == [] and run_length_encode("abab") == [("a", 1), ("b", 1), ("a", 1), ("b", 1)]
    assert flatten_all([[1, 2], [], [3]]) == [1, 2, 3] and flatten_all([]) == []
    assert distinct_permutations("aab") == ["aab", "aba", "baa"]
    assert distinct_permutations("") == [""] and len(distinct_permutations("abcd")) == 24
    print("ok")
