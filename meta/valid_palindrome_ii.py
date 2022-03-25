# description: https://leetcode.com/problems/valid-palindrome-ii/
def validPalindrome(s):
    i = 0
    j = len(s) - 1
    count = 0

    while i < j:
        if s[i] != s[j]:
            return is_palindrome(s, i + 1, j) or is_palindrome(s, i, j -1)
        else:
            i += 1
            j -= 1

    return True

def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

s = 'eedede'
print(validPalindrome(s))

# Time Complexity: O(l), where l is the lenght of the string
# Space Complexity: O(1)