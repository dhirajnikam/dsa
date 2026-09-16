"""
Problem: Count the operations
Difficulty: Warm-up | Topic: analyzing loops, exact counts, Big-O

Each function below is given a code snippet. Return the EXACT number of times the line marked
`# count me` executes for the given n, without running the loops: the tests use n up to 10**9,
so your answer must be a formula (O(1)) or a short loop (O(log n)).

1. nested_square(n):
       for i in range(n):
           for j in range(n):
               x += 1          # count me

2. triangle(n):
       for i in range(n):
           for j in range(i):
               x += 1          # count me

3. halving(n):                 # n >= 1
       while n > 1:
           n //= 2
           x += 1              # count me

4. n_log_n(n):                 # n >= 1
       for i in range(n):
           j = n
           while j > 1:
               j //= 2
               x += 1          # count me

5. two_loops(n, m):
       for i in range(n): x += 1     # count me
       for j in range(m): x += 1     # count me

6. stepping(n, k):             # k >= 1
       for i in range(0, n, k):
           x += 1              # count me

7. doubling(n):                # n >= 1
       i = 1
       while i < n:
           i *= 2
           x += 1              # count me

Hints:
2. 0 + 1 + ... + (n-1) = n(n-1)/2
3. Number of halvings until n hits 1 is floor(log2 n) == n.bit_length() - 1.
6. Ceiling division: (n + k - 1) // k, but 0 when n <= 0.
7. Smallest p with 2**p >= n. Careful: doubling(1) == 0, doubling(2) == 1, doubling(3) == 2.
"""


def nested_square(n: int) -> int:
    raise NotImplementedError


def triangle(n: int) -> int:
    raise NotImplementedError


def halving(n: int) -> int:
    raise NotImplementedError


def n_log_n(n: int) -> int:
    raise NotImplementedError


def two_loops(n: int, m: int) -> int:
    raise NotImplementedError


def stepping(n: int, k: int) -> int:
    raise NotImplementedError


def doubling(n: int) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    def brute_halving(n):
        c = 0
        while n > 1:
            n //= 2
            c += 1
        return c

    def brute_doubling(n):
        i, c = 1, 0
        while i < n:
            i *= 2
            c += 1
        return c

    assert nested_square(0) == 0 and nested_square(3) == 9 and nested_square(10**9) == 10**18, 'Check: nested_square(0) == 0 and nested_square(3) == 9 and nested_square(10**9) == 10**18'
    assert triangle(0) == 0 and triangle(1) == 0 and triangle(4) == 6 and triangle(10**9) == 499999999500000000, 'Check: triangle(0) == 0 and triangle(1) == 0 and triangle(4) == 6 and triangle(10**9) == 499999999500000000'
    for n in [1, 2, 3, 4, 7, 8, 9, 1000, 1023, 1024]:
        assert halving(n) == brute_halving(n), n
        assert doubling(n) == brute_doubling(n), n
        assert n_log_n(n) == n * brute_halving(n), n
    assert halving(2**40) == 40 and doubling(2**40) == 40 and doubling(2**40 + 1) == 41, 'Check: halving(2**40) == 40 and doubling(2**40) == 40 and doubling(2**40 + 1) == 41'
    assert n_log_n(10**9) == 10**9 * 29, 'Check: n_log_n(10**9) == 10**9 * 29'
    assert two_loops(3, 5) == 8 and two_loops(0, 0) == 0 and two_loops(10**9, 10**9) == 2 * 10**9, 'Check: two_loops(3, 5) == 8 and two_loops(0, 0) == 0 and two_loops(10**9, 10**9) == 2 * 10**9'
    assert stepping(10, 3) == 4 and stepping(9, 3) == 3 and stepping(0, 5) == 0 and stepping(1, 100) == 1, 'Check: stepping(10, 3) == 4 and stepping(9, 3) == 3 and stepping(0, 5) == 0 and stepping(1, 100) == 1'
    assert stepping(10**9, 7) == len(range(0, 10**9, 7)), 'Check: stepping(10**9, 7) == len(range(0, 10**9, 7))'
    # Boundary and misconception checks: predict each result before running.
    assert triangle(2) == 1, 'Check: triangle(2) == 1'
    assert halving(15) == 3 and doubling(15) == 4, 'Check: halving(15) == 3 and doubling(15) == 4'
    assert stepping(12, 4) == 3 and stepping(13, 4) == 4, 'Check: stepping(12, 4) == 3 and stepping(13, 4) == 4'
    assert two_loops(0, 8) == 8, 'Check: two_loops(0, 8) == 8'
    print("ok")
