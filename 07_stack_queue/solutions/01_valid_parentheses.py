def is_valid(s):
    # O(n) time, O(n) space
    # Stack holds unmatched opens; each close must match the most recent open.
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
