# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def is_anagram(s: str, t: str) -> bool:
    i = 0
    j = len(s)-1
    if len(s.strip()) != len(t.strip()):
        return False
    for c in s:
        if c == t[j]:
            j -= 1
        return True
    return False

s = "kayak"
t = "kayak"

print(is_anagram(s, t))