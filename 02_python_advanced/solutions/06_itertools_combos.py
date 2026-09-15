from itertools import accumulate, chain, combinations, groupby, permutations, product


def pairs_with_sum(nums, target):  # O(n^2)
    return sum(1 for a, b in combinations(nums, 2) if a + b == target)


def dice_sum_counts(dice, sides):  # O(sides^dice)
    counts = {}
    for roll in product(range(1, sides + 1), repeat=dice):
        s = sum(roll)
        counts[s] = counts.get(s, 0) + 1
    return counts


def prefix_maxes(nums):
    return list(accumulate(nums, max))


def run_length_encode(s):
    return [(ch, len(list(g))) for ch, g in groupby(s)]


def flatten_all(lists):
    return list(chain.from_iterable(lists))


def distinct_permutations(s):  # O(n! * n)
    return sorted(set("".join(p) for p in permutations(s)))
