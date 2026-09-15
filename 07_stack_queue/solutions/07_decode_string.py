def decode_string(s):
    # O(output) time, O(depth + output) space
    # '[' saves the outer (prefix, count) frame; ']' pops it and splices the repeated inner
    # string onto the prefix. Digits accumulate into num until the next '['.
    stack, cur, num = [], "", 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur, num))
            cur, num = "", 0
        elif ch == "]":
            prev, k = stack.pop()
            cur = prev + cur * k
        else:
            cur += ch
    return cur
