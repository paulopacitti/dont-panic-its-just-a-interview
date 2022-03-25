# description: https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    if root is None: # empty node
        return None

    if root.val == p.val or root.val == q.val: # found node p or found node q
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right: # this is the common ancestor, p and q are in different subtrees
        return root
    
    if left != None:
        return left # p and q are in the left subtree
    else:
        return right # p and q are in the right subtree

# Time complexity: O(n), where n is the number of nodes on the tree
# Space complexity: O(n)