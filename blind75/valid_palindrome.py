# https://leetcode.com/problems/valid-palindrome

def isPalindrome(s):
    alphanum_lower_s = "".join(filter(lambda c: isalnum(c), s.lower()))
    l, r = 0, len(alphanum_lower_s) - 1
    while l < r:
        if alphanum_lower_s[l] != alphanum_lower_s[r]:
            return False    
        l += 1
        r -= 1
    return True

def isalnum(c):
    return(ord("A") <= ord("c") and ord("c") <= ord("Z")
        or ord("a") <= ord("c") and ord("c") <= ord("z")
        or ord("0") <= ord("c") and ord("c") <= ord("9"))