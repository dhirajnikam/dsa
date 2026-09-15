def nested_square(n):  # O(n^2) loop -> exact count n*n
    return n * n


def triangle(n):  # O(n^2) loop -> exact count n(n-1)/2
    return n * (n - 1) // 2


def halving(n):  # O(log n) loop -> floor(log2 n)
    return n.bit_length() - 1


def n_log_n(n):  # O(n log n) loop
    return n * halving(n)


def two_loops(n, m):  # O(n + m)
    return n + m


def stepping(n, k):  # O(n / k)
    return max(0, (n + k - 1) // k)


def doubling(n):  # O(log n): smallest p with 2**p >= n
    return (n - 1).bit_length() if n > 1 else 0
