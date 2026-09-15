def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))


def is_palindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    return sum(c in "aeiouAEIOU" for c in s)


def capitalize_words(s: str) -> str:
    return " ".join(w[:1].upper() + w[1:] for w in s.split())
