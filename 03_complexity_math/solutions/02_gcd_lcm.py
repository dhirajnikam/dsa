from functools import reduce


def gcd(a, b):  # O(log min(a, b))
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return a // gcd(a, b) * b


def gcd_list(nums):
    return reduce(gcd, nums)


def lcm_list(nums):
    return reduce(lcm, nums)


def are_coprime(a, b):
    return gcd(a, b) == 1


def reduce_fraction(num, den):
    if den < 0:
        num, den = -num, -den
    g = gcd(abs(num), den)
    return num // g, den // g
