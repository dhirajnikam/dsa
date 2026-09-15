def is_palindrome(s):
    # O(n) time, O(1) space
    # Pointers walk inward from both ends, skipping non-alphanumerics, comparing lowercase.
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
    return True
