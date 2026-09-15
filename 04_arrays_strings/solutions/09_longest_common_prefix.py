def longest_common_prefix(strs):
    # O(S) time, O(1) extra space
    # zip(*strs) walks columns; stop at the first column with more than one distinct char.
    out = []
    for col in zip(*strs):
        if len(set(col)) > 1:
            break
        out.append(col[0])
    return "".join(out)
