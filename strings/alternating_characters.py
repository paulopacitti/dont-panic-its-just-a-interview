# problem link: https://www.hackerrank.com/challenges/alternating-characters/problem
# Difficulty: Easy

def alternatingCharacters(s):
    s_characters = list(s)
    count = 0

    for i in range(len(s_characters) - 1):
        if s_characters[i] == s_characters[i+1]: # if the current character is equal to the next, then you must increase
            count += 1                           # the number of characters removed
    return count

q = int(input())
for i in range(q):
    s = input()

    result = alternatingCharacters(s)
    print(result)