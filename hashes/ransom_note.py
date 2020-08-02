# problem link: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# Difficulty: Easy

def checkMagazine(magazine, note):
    magazine_dict = {} # hash containing all the words in the magazine
    # not creating a hash for note - it costs too much time

    # creating the hash without 'magazine.count()' -> it costs too much time 
    for e in magazine:
        if e in magazine_dict:
            magazine_dict[e] += 1
        else:
            magazine_dict[e] = 1

        
    # Check if exist the word in the hash
    for word in note:
        if word not in magazine_dict or magazine_dict[word] == 0:
            return False
        else:
            # subtract occurence of word in the hash
            magazine_dict[word] -= 1
    return True

m, n = int(input().split())
magazine = input().rstrip().split()
note = input().rstrip().split()
if checkMagazine(magazine, note):
    print('Yes')
else:
    print('No')