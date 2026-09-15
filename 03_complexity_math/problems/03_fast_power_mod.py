"""
Problem: Fast exponentiation and modular arithmetic
Difficulty: Easy | Topic: exponentiation by squaring, modular arithmetic, Fermat inverse
Source: LeetCode 50, 372 (variants)

Do NOT use the built-in pow() or ** for 1-3.

1. fast_power(b, e) -> b ** e for integer b and e >= 0, using O(log e) multiplications.
   The tests count multiplications indirectly by requiring fast_power(3, 10**5) to finish quickly.
2. pow_mod(b, e, m) -> (b ** e) % m with m >= 1, taking % m at every step. Handles e == 0 (-> 1 % m).
3. mod_inverse(a, p) -> the x in [0, p) with (a * x) % p == 1, for prime p and a % p != 0.
   Use Fermat: a^(p-2) mod p.
4. mod_divide(a, b, p) -> (a / b) mod p for prime p, i.e. a * inverse(b) mod p.
5. last_k_digits(b, e, k) -> the last k decimal digits of b ** e as a zero-padded string of length k.
   last_k_digits(2, 10, 2) -> "24"; last_k_digits(7, 0, 3) -> "001".
6. power_float(x, n) -> x ** n for float x and any integer n (negative allowed), O(log |n|).
   Answers are checked with a tolerance.

Hints:
1. result = 1; while e: if e & 1: result *= b; b *= b; e >>= 1
2. Same loop, but `result = result * b % m` and `b = b * b % m`.
5. pow_mod(b, e, 10**k) then str().zfill(k).
6. If n < 0: x = 1 / x; n = -n. Then the same loop.
"""


def fast_power(b: int, e: int) -> int:
    raise NotImplementedError


def pow_mod(b: int, e: int, m: int) -> int:
    raise NotImplementedError


def mod_inverse(a: int, p: int) -> int:
    raise NotImplementedError


def mod_divide(a: int, b: int, p: int) -> int:
    raise NotImplementedError


def last_k_digits(b: int, e: int, k: int) -> str:
    raise NotImplementedError


def power_float(x: float, n: int) -> float:
    raise NotImplementedError


if __name__ == "__main__":
    assert fast_power(2, 10) == 1024 and fast_power(5, 0) == 1 and fast_power(0, 5) == 0
    assert fast_power(-2, 3) == -8 and fast_power(-2, 4) == 16
    assert fast_power(3, 10**5) == 3 ** (10**5)
    MOD = 10**9 + 7
    assert pow_mod(2, 10, 1000) == 24 and pow_mod(2, 0, 7) == 1 and pow_mod(5, 3, 1) == 0
    assert pow_mod(3, 10**18, MOD) == pow(3, 10**18, MOD)
    assert pow_mod(123456789, 987654321, MOD) == pow(123456789, 987654321, MOD)
    assert mod_inverse(3, 7) == 5 and mod_inverse(2, MOD) == (MOD + 1) // 2
    for a in range(1, 13):
        assert (a * mod_inverse(a, 13)) % 13 == 1, a
    assert mod_divide(10, 5, 13) == 2 and mod_divide(1, 2, 7) == 4
    assert mod_divide(6, 4, MOD) == (6 * pow(4, MOD - 2, MOD)) % MOD
    assert last_k_digits(2, 10, 2) == "24" and last_k_digits(7, 0, 3) == "001"
    assert last_k_digits(3, 1000, 5) == str(3 ** 1000)[-5:]
    assert abs(power_float(2.0, 10) - 1024.0) < 1e-9
    assert abs(power_float(2.0, -2) - 0.25) < 1e-9
    assert abs(power_float(1.5, 0) - 1.0) < 1e-9
    assert abs(power_float(0.5, 3) - 0.125) < 1e-9
    assert abs(power_float(2.0, -31) - 2.0**-31) < 1e-15
    print("ok")
