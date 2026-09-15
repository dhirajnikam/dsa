def compress(chars):
    # O(n) time, O(1) space
    # Read pointer i scans a run; write pointer w emits char + optional count. w <= i always,
    # so writes never clobber unread input.
    w = i = 0
    n = len(chars)
    while i < n:
        ch, start = chars[i], i
        while i < n and chars[i] == ch:
            i += 1
        chars[w] = ch
        w += 1
        if i - start > 1:
            for d in str(i - start):
                chars[w] = d
                w += 1
    return w
