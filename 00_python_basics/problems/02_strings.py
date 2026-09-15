"""
Problem: String basics
Difficulty: Warm-up | Topic: slicing, methods, immutability

1. reverse_words("the sky is blue") -> "blue is sky the"
   Collapse multiple spaces, strip leading/trailing spaces.
2. is_palindrome("A man, a plan, a canal: Panama") -> True
   Ignore case and non-alphanumeric characters. (LeetCode 125)
3. count_vowels("Hello World") -> 3
4. capitalize_words("hello big world") -> "Hello Big World"
   Do not use str.title() (it breaks on apostrophes); use split/join.

Hints:
1. split() with no argument handles multiple spaces and strips ends.
2. Build a cleaned string with a list comprehension and str.isalnum(), then compare with its reverse.
"""


def reverse_words(s: str) -> str:
    list_word = s.split()
    return " ".join(list_word[::-1])
    
        


def is_palindrome(s: str) -> bool:
    words = ""
    for ch in s:
        if ch.isalnum():
            words += ch.lower()
    return words == words[::-1]



def count_vowels(s: str) -> int:
    count = 0
    for vowel in s:
        if vowel in "aeiouAEIOU":
            count += 1
    return count  



def capitalize_words(s: str) -> str:
    list_word = s.split()
    result = []
    for w in list_word:
        result.append(w[0].upper() + w[1:])
    return " ".join(result)



if __name__ == "__main__":
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello   world  ") == "world hello"
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("race a car")
    assert is_palindrome(" ")
    assert count_vowels("Hello World") == 3
    assert count_vowels("xyz") == 0
    assert capitalize_words("hello big world") == "Hello Big World"
    assert capitalize_words("don't stop") == "Don't Stop"
    print("ok")
