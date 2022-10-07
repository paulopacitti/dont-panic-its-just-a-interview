# descrpition: https://leetcode.com/problems/longest-string-chain/
# tags: "dynamic programming", "strings"
# Solution:
# - We can solve this using dynamic programming. First, we create
# a dictionary to store the words as keys and the current longest string
# chain that he is the last member of.
# - For each word, we check if any of their subwords (removing one letter
# of that word), exist on the table. If not exists, then we know the word
# is new, so it's the first of their long string chain. If exists, we
# update the longest string chain variable, checking if this predecessor
# is longer than any predecessor that produce the same subword. Finally,
# we add the word to the table with the longest string chain value found.
# - The result will be the maximum value on the table (plus one because the
# longest string chain starts with 0)


def longestStrChain(words):
    table = {}
    sorted_words = sorted(words, key=lambda e: len(e))
    for word in sorted_words:
        longest = 0
        for i in range(len(word)):
            sub_word = word[0:i] + word[i + 1 :]
            if sub_word in table:
                longest = max(longest, table[sub_word] + 1)
        table[word] = longest
    return max(table.values()) + 1


chain = ["a", "b", "ba", "bca", "bda", "bdca"]
print(longestStrChain(chain))

# Time complexity: O(n log n) + O(n * w) = O(n * w), where w is the longest string size
# Space complexity: O(n) to build the table
