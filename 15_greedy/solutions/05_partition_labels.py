def partition_labels(s):
    # O(n) time, O(1) space
    # Each part must reach the last occurrence of every letter it contains; close a part
    # the moment the index catches up with that required end.
    last = {c: i for i, c in enumerate(s)}
    sizes, start, end = [], 0, 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            sizes.append(end - start + 1)
            start = i + 1
    return sizes
