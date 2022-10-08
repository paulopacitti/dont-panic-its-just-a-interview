# description: https://leetcode.com/problems/longest-common-prefix


def find_shortest_string(arr):
    min_word = arr[0]

    for word in arr:
        if len(word) < len(min_word):
            min_word = word
    return min_word


def longestCommonPrefix(strs):
    longest_prefix = ""
    shortest = find_shortest_string(strs)

    for i in range(len(shortest)):
        for s in strs:
            if shortest[i] != s[i]:
                return longest_prefix
        longest_prefix += shortest[i]
    return longest_prefix
