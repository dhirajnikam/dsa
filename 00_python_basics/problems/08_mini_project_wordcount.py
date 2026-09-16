"""
Problem: Word count report (mini project)
Difficulty: Easy | Topic: strings + dicts + sorting together

word_report(text, top=3) -> dict with keys:
  "words": total word count
  "unique": number of distinct words (case-insensitive)
  "top": list of (word, count) tuples, most frequent first, ties alphabetical, at most `top` items
  "longest": the longest word (first one encountered on ties)

Tokenize: lowercase everything, strip punctuation .,!?;:'" from both ends of each token,
drop empty tokens.

Example:
  word_report("The cat. The dog! the END", top=2)
  -> {"words": 6, "unique": 4, "top": [("the", 3), ("cat", 1)], "longest": "the"}

Hints:
1. tokens = [t.strip(".,!?;:'\"") for t in text.lower().split()]
2. Reuse ideas from 04 and 07.
"""


def word_report(text: str, top: int = 3) -> dict:
    raise NotImplementedError


if __name__ == "__main__":
    r = word_report("The cat. The dog! the END", top=2)
    assert r == {"words": 6, "unique": 4, "top": [("the", 3), ("cat", 1)], "longest": "the"}, 'Check: r == {"words": 6, "unique": 4, "top": [("the", 3), ("cat", 1)], "longest": "the"}'
    r = word_report("", top=3)
    assert r == {"words": 0, "unique": 0, "top": [], "longest": ""}, 'Check: r == {"words": 0, "unique": 0, "top": [], "longest": ""}'
    r = word_report("a bb ccc bb", top=5)
    assert r["top"] == [("bb", 2), ("a", 1), ("ccc", 1)] and r["longest"] == "ccc", 'Check: r["top"] == [("bb", 2), ("a", 1), ("ccc", 1)] and r["longest"] == "ccc"'
    print("ok")
