# Phase 03: Complexity & Math

**Goal:** look at code and say how its running time grows, and know the few math tools interviews assume.

## Key idea
Big-O says how work grows as input size n grows. Drop constants and smaller terms: `3n² + 100n` is O(n²).
Loops one after another add. Loops inside loops multiply. A loop that halves each time is O(log n).
Order: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ). If n can be 10⁵, O(n²) is too slow.

## Cheat sheet
```python
for i in range(n):            # n
    for j in range(n): ...    # x n  -> O(n^2)
while i > 1: i //= 2          # halves -> O(log n)

def gcd(a, b):                # Euclid
    while b: a, b = b, a % b
    return a

MOD = 10**9 + 7
(a * b) % MOD                 # take % at every step
pow(a, k, MOD)                # fast power, built in

x & 1                         # odd?
x & (x - 1)                   # clears lowest 1 bit; 0 means power of two (x > 0)
bin(x).count("1")             # number of 1 bits

def fact(n):                  # recursion: base case + smaller call
    return 1 if n <= 1 else n * fact(n - 1)
```

## Common mistakes
- `x in list` inside a loop is a hidden O(n). Use a set.
- `s += ch` in a loop copies the string every time. Collect and `"".join`.
- Recursion depth counts as memory. Python stops around 1000 deep.
- Taking `% MOD` only at the end makes huge slow numbers.

## Problems
- `01_count_operations.py` — count exact loop iterations
- `02_gcd_lcm.py` — Euclid, lcm, reduce fractions
- `03_fast_power_mod.py` — power by squaring, modular inverse
- `04_sieve_primes.py` — primality test, sieve, factorization
- `05_bit_tricks.py` — popcount, XOR single, get/set bits
- `06_recursion_basics.py` — factorial, digit sum, reverse string
- `07_fibonacci_three_ways.py` — naive vs memo vs loop
- `08_complexity_quiz.py` — name the Big-O of ten snippets
