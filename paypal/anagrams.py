# descritpion: https://leetcode.com/problems/find-all-anagrams-in-a-string/


def findAnagrams(s, p):
    p_map, window_map = {}, {}
    indices = []

    for letter in p:
        if letter in p_map:
            p_map[letter] += 1
        else:
            p_map[letter] = 1

    for i in range(len(p)):
        if s[i] in window_map:
            window_map[s[i]] += 1
        else:
            window_map[s[i]] = 1

    for i in range(len(p), len(s)):
        start_index = i - len(p)
        if window_map == p_map:
            indices.append(start_index)

        window_map[s[start_index]] -= 1
        if window_map[s[start_index]] <= 0:
            window_map.pop(s[start_index])

        if s[i] in window_map:
            window_map[s[i]] += 1
        else:
            window_map[s[i]] = 1
    if window_map == p_map:
        indices.append(len(s) - len(p))

    return indices


# Time complexity: O(n)
# Space complexity: O(n)


s = "abab"
p = "ab"
print(findAnagrams(s, p))
