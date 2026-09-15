# What a strong candidate says:
# "Can strings contain any character, including whatever separator I pick? Can they be
#  empty? Can the list be empty? Then a plain delimiter is unsafe. I'll length-prefix each
#  string as '<len>#<chars>'; the '#' ends the number unambiguously since digits never
#  contain '#'. This is how HTTP chunked encoding frames data. O(total chars) both ways."


def encode(strs):
    # O(total chars) time, O(total chars) space
    # Length-prefix framing: the decoder never has to search for a separator inside data.
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(s):
    # O(total chars) time, O(total chars) space
    out, i = [], 0
    while i < len(s):
        j = s.index("#", i)
        length = int(s[i:j])
        out.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return out
