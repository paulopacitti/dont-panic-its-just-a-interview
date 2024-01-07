# https://leetcode.com/problems/ransom-note/description/

def canConstruct(ransomNote, magazine):
    alphabet = {}
    for letter in magazine:
        if letter in alphabet:
            alphabet[letter] += 1
        else:
            alphabet[letter] = 1
    
    for letter in ransomNote:
        if letter not in alphabet:
            return False
        else:
            if alphabet[letter] < 1:
                return False
            else:
                alphabet[letter] -= 1

    return True