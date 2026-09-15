def find_maximum_xor(nums):
    # O(31 n) time, O(31 n) space
    # Insert every number into a bit trie (MSB first). For each number walk the trie
    # preferring the opposite bit at each level: a higher differing bit always beats
    # any combination of lower bits.
    root = {}
    for x in nums:
        node = root
        for b in range(30, -1, -1):
            node = node.setdefault(x >> b & 1, {})

    best = 0
    for x in nums:
        node, cur = root, 0
        for b in range(30, -1, -1):
            bit = x >> b & 1
            if 1 - bit in node:
                cur |= 1 << b
                node = node[1 - bit]
            else:
                node = node[bit]
        best = max(best, cur)
    return best
