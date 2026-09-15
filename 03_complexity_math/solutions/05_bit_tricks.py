def count_bits(x):  # O(number of set bits)
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


def is_power_of_two(x):  # O(1)
    return x > 0 and x & (x - 1) == 0


def lowest_set_bit(x):
    return x & -x


def single_number(nums):  # O(n) time, O(1) space
    acc = 0
    for v in nums:
        acc ^= v
    return acc


def missing_number(nums):  # O(n) time, O(1) space
    acc = len(nums)
    for i, v in enumerate(nums):
        acc ^= i ^ v
    return acc


def get_bit(x, k):
    return (x >> k) & 1


def set_bit(x, k):
    return x | (1 << k)


def clear_bit(x, k):
    return x & ~(1 << k)


def toggle_bit(x, k):
    return x ^ (1 << k)


def count_bits_upto(n):  # O(n)
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits


def subsets_by_mask(items):  # O(2^n * n)
    n = len(items)
    return [[items[i] for i in range(n) if mask >> i & 1] for mask in range(1 << n)]
