# description: https://leetcode.com/problems/range-sum-of-bst

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    queue = [root]
    numbers_in_range = 0
    
    while len(queue) > 0:
        current = queue.pop(0)
        if current == None:
            continue
        if current.val >= low and current.val <= high:
            numbers_in_range += current.val
        if current.val > low:
            queue.append(current.left)
        if current.val < high:
            queue.append(current.right)
    return numbers_in_range

# Time complexity: O(n), where n is the number of nodes
# Space complexity: O(n/2) = O(n), queue size