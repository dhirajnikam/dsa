def count_bits(n):
    # O(n) time, O(n) space
    # i >> 1 has one fewer bit and is already computed; add back the dropped lowest bit.
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits
