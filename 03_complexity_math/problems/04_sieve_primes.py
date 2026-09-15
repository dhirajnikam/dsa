"""
Problem: Primes
Difficulty: Easy | Topic: trial division, sieve of Eratosthenes, factorization
Source: LeetCode 204, 2521 (variants)

1. is_prime(n) -> bool in O(sqrt n). Negative numbers, 0 and 1 are not prime.
2. sieve(n) -> sorted list of all primes <= n. sieve(1) == []. Must handle n = 10**6 in well
   under a second (use slice assignment, start marking at i*i).
3. count_primes(n) -> number of primes strictly less than n (LeetCode 204 definition).
4. prime_factors(n) -> list of prime factors with multiplicity, ascending, for n >= 2.
   prime_factors(360) -> [2, 2, 2, 3, 3, 5].
5. distinct_prime_factor_count(n) -> number of distinct primes dividing n. n >= 1 (returns 0 for 1).
6. nth_prime(k) -> the k-th prime (1-indexed): nth_prime(1) == 2, nth_prime(6) == 13, nth_prime(10001) == 104743.

Hints:
1. Handle n < 2, then even numbers, then odd divisors while i * i <= n.
2. is_p = [True] * (n + 1); is_p[0] = is_p[1] = False; for i in range(2, isqrt(n) + 1): if is_p[i]: is_p[i*i::i] = [False] * len(range(i*i, n+1, i))
4. Divide out 2s, then odd i while i*i <= n; if n > 1 at the end, n itself is prime.
6. Sieve up to a bound; for k <= 10001, 120000 is enough (or grow the bound and retry).
"""
import math


def is_prime(n: int) -> bool:
    raise NotImplementedError


def sieve(n: int) -> list[int]:
    raise NotImplementedError


def count_primes(n: int) -> int:
    raise NotImplementedError


def prime_factors(n: int) -> list[int]:
    raise NotImplementedError


def distinct_prime_factor_count(n: int) -> int:
    raise NotImplementedError


def nth_prime(k: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    assert [n for n in range(-2, 30) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert is_prime(10**9 + 7) and not is_prime(10**9 + 8)
    assert is_prime(999983) and not is_prime(999983 * 3)
    assert sieve(1) == [] and sieve(2) == [2] and sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    primes = sieve(10**6)
    assert len(primes) == 78498 and primes[-1] == 999983
    assert count_primes(10) == 4 and count_primes(0) == 0 and count_primes(2) == 0 and count_primes(3) == 1
    assert count_primes(10**6) == 78498
    assert prime_factors(360) == [2, 2, 2, 3, 3, 5] and prime_factors(2) == [2] and prime_factors(97) == [97]
    assert prime_factors(2**20) == [2] * 20 and prime_factors(999983 * 999983) == [999983, 999983]
    assert distinct_prime_factor_count(360) == 3 and distinct_prime_factor_count(1) == 0 and distinct_prime_factor_count(64) == 1
    assert nth_prime(1) == 2 and nth_prime(6) == 13 and nth_prime(100) == 541 and nth_prime(10001) == 104743
    print("ok")
