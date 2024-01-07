# https://leetcode.com/problems/longest-palindrome/

def longestPalindrome(s: str) -> int:
    if len(s) == 1:
        return 1
    
    # letters frequency routine
    letters = {}
    lenght = 0
    odd = False
    for letter in s:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    # account the even part of the odd number by calculating
    # the floor of the division, since you can use it for bulding the palindrome
    for k, v in letters.items():
        if v % 2 != 0: 
            odd = True # add 1 to the lenght in the end
            lenght += (v // 2) * 2
        else:
            lenght += v
    
    return lenght + 1 if odd else lenght