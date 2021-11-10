# description: https://leetcode.com/problems/search-suggestions-system/
def suggestedProducts(products, searchWord):
    results = []
    for i in range(1, len(searchWord) + 1):
        current_result = []
        for product in products:
            if product[0:i] == searchWord[0:i]:
                current_result.append(product)
        current_result.sort()
        results.append(current_result[0:3])
    return results

# Time complexity: O(m*n), where m is the length of searchWord and n is the number of products
# Space complexity: O(n*2), where all products match all the substrings
# How to improve: this could be improved using a trie (not exactly, just the search would be improved)