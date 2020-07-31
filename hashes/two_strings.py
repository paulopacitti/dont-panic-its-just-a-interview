# problem link: https://www.hackerrank.com/challenges/two-strings/problem
# Difficulty: Easy

def twoStrings(s1, s2):
    result = 0
    # create a set of letters of each string
    s1_letters = set(list(s1))
    s2_letters = set(list(s2))

    # check if the sets of letters of each string intersect
    if s1_letters & s2_letters:
        return 'YES'
    else:
        return 'NO'

p = int(input())
for i in range(p):
    s1 = input()
    s2 = input()

    result = twoStrings(s1, s2)
    print(result)