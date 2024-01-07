# https://leetcode.com/problems/valid-anagram/

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_s, hash_t = {}, {}
    for c in s:
        if c in hash_s:
            hash_s[c] += 1
        else:
            hash_s[c] = 1
    for c in t:
        if c in hash_t:
            hash_t[c] += 1
        else:
            hash_t[c] = 1
    return hash_s == hash_t

def is_anagram_2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hash_s, hash_t = {}, {}
    for i in range(len(s)):
        hash_s[s[i]] = hash_s.get(s[i], 0) + 1
        hash_t[t[i]] = hash_t.get(t[i], 0) + 1
    return hash_s == hash_t