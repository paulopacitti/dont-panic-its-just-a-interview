# description: https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self, value = None, end = False):
        self.end = end
        self.value = value
        self.children = {}

def suggestedProducts(products, searchWord):
    trie = build_trie(products)
    results = []
    for i in range(1, len(searchWord) + 1):
        suggestions = dfs(trie, searchWord[0:i])
        results.append(suggestions)

    return results

def dfs(root, word):
    string = ""
    current = root
    for char in word:
        if char not in current.children:
            return []
        string += char
        current = current.children[char]

    stack = [(string, current)]
    matched_words = []

    while len(stack) > 0:
        string, node = stack.pop()
        if node.end:
            matched_words.append(string)
        for next_node in node.children.values():
            if next_node is not None:
                stack.append((string + next_node.value, next_node))

    # sort the products array
    sorted_words = sorted(matched_words)
    if len(sorted_words) < 3:
        return sorted_words
    return sorted_words[:3]

def build_trie(words):
    root = TrieNode()
    for word in words:
        current = root
        for i in range(0, len(word)):
            if word[i] not in current.children:
                current.children[word[i]] = TrieNode(word[i])
            current = current.children[word[i]]
        current.end = True
    return root


p = ["mobile","mouse","moneypot","monitor","mousepad"]
w = "mouse"
print(suggestedProducts(p,w))

# Time complexity:
#   - Initialization: Sum(len(products[i]))
#   - Query: O(len(searchWord))
# Space complexity: Sum(len(products[i])), to store the trie