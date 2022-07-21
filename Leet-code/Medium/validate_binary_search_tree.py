# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:


# Input: root = [2,1,3]
# Output: true

# https://leetcode.com/problems/validate-binary-search-tree/

# https://www.youtube.com/watch?v=s6ATEkipzow

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, left, right):
            if not node:
                return True
            if not(node.val < right and node.val > left):
                return False

            return (validate(node.left, left, node.val) and validate(node.right, node.val, right))

        return validate(root, float("-inf"), float("inf"))


root = TreeNode(5, TreeNode(1), TreeNode(9, TreeNode(7), TreeNode(10)))

mySolution = Solution()
print(mySolution.isValidBST(root))
