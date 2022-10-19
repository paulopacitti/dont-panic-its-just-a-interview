def longest_substring(s: str) -> int:
    current_chars = {}
    i = 0
    max_substring = 0

    while i < len(s):
        if s[i] in current_chars:
            max_substring = max(max_substring, len(current_chars))
            i = current_chars[s[i]] + 1
            current_chars = {}
        else:
            current_chars[s[i]] = i
            i += 1
    return max(max_substring, len(current_chars))


def longest_substring(s: str) -> int:
    current_chars = {}
    i = 0
    max_substring = 0

    while i < len(s):
        if s[i] in current_chars:
            max_substring = max(max_substring, len(current_chars))
            i = current_chars[s[i]] + 1
            current_chars = {}
        else:
            current_chars[s[i]] = i
            i += 1
    return max(max_substring, len(current_chars))


print(longest_substring("dvdf"))
