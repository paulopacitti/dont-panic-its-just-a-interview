# description: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        count = 0

        # while current node can be visited or stack is not empty
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            # node does not have left child
            current = stack.pop()
            count += 1
            if count == k: # found kth smallest
                return current.val
            current = current.right # check right subtree
        return 0