"""
Problem: Mock interview 1 - Encode and Decode Strings
Difficulty: Medium | Pattern: String design (length-prefix framing)
Source: LeetCode 271

Interviewer says:
  "We have a service that sends a list of strings over the network as a single string.
   Write the two sides: something that turns the list into one string, and something
   that turns that string back into the original list. Make it round-trip exactly."

That is all you get. Before reading the hints, ask yourself (out loud) at least four
clarifying questions and write down two examples including an edge case.

Hints (contain the constraints you should have asked about):
1. Strings may contain ANY character, including separators you might pick and digits.
   Strings may be empty. The list may be empty. Up to 200 strings of length up to 200.
2. A delimiter alone fails when the delimiter appears in a string. Escaping works but is
   fiddly. The clean approach is length-prefix framing: "<len>#<string>" for each item.
3. Decoding: read digits until '#', parse the length, slice exactly that many characters,
   repeat. The '#' after the digits is unambiguous because digits never contain '#'.
4. Chunked-transfer encoding in HTTP works this way; say so, it shows breadth.

Expected: O(total characters) time for both directions, O(total characters) space
"""


def encode(strs: list[str]) -> str:
    raise NotImplementedError


def decode(s: str) -> list[str]:
    raise NotImplementedError


if __name__ == "__main__":
    def roundtrip(strs):
        return decode(encode(strs)) == strs

    assert roundtrip(["hello", "world"])
    assert roundtrip([])
    assert roundtrip([""])
    assert roundtrip(["", "", ""])
    assert roundtrip(["a#b", "#", "12#34"])
    assert roundtrip(["3#abc", "0#"])
    assert roundtrip(["multi\nline", "tab\there", "unicode: é中"])
    assert roundtrip(["x" * 200] * 200)
    assert isinstance(encode(["a"]), str)
    assert decode(encode(["only"])) == ["only"]
    print("ok")
