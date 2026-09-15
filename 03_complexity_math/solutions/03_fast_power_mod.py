def fast_power(b, e):  # O(log e) multiplications
    result = 1
    while e:
        if e & 1:
            result *= b
        b *= b
        e >>= 1
    return result


def pow_mod(b, e, m):  # O(log e)
    result = 1 % m
    b %= m
    while e:
        if e & 1:
            result = result * b % m
        b = b * b % m
        e >>= 1
    return result


def mod_inverse(a, p):  # Fermat: a^(p-1) = 1 mod p, so a^(p-2) is the inverse
    return pow_mod(a, p - 2, p)


def mod_divide(a, b, p):
    return a % p * mod_inverse(b, p) % p


def last_k_digits(b, e, k):
    return str(pow_mod(b, e, 10**k)).zfill(k)


def power_float(x, n):  # O(log |n|)
    if n < 0:
        x, n = 1 / x, -n
    result = 1.0
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result
