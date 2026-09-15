import math


def is_prime(n):  # O(sqrt n)
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def sieve(n):  # O(n log log n) time, O(n) space
    if n < 2:
        return []
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, math.isqrt(n) + 1):
        if is_p[i]:
            is_p[i * i::i] = [False] * len(range(i * i, n + 1, i))
    return [i for i, p in enumerate(is_p) if p]


def count_primes(n):
    return len(sieve(n - 1))


def prime_factors(n):  # O(sqrt n)
    out = []
    while n % 2 == 0:
        out.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            out.append(i)
            n //= i
        i += 2
    if n > 1:
        out.append(n)
    return out


def distinct_prime_factor_count(n):
    return len(set(prime_factors(n))) if n > 1 else 0


def nth_prime(k):
    bound = 100
    while True:
        primes = sieve(bound)
        if len(primes) >= k:
            return primes[k - 1]
        bound *= 2
