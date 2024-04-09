# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for char in t:
        if char in s:
            s.replace(char, "", 1)
        else:
            return False
    return True


word_one = "cat"  # "nagaram"
word_two = "car"  # "anagram"


print(is_anagram(word_one, word_two))
