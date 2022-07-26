# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]


# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
val = 2

mySolution = Solution()
print(mySolution.searchBST(root, val).val)
