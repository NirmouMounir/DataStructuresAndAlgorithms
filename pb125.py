# Palindrome

def is_palindrome(s: str, t: str) -> bool:
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

print(is_palindrome(s, t))