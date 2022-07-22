# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0

        def traverse(root, id):
            if root:
                nonlocal depth
                if id > depth:
                    depth = id

                if root.left:
                    traverse(root.left, id + 1)
                if root.right:
                    traverse(root.right, id + 1)

        traverse(root, 1)
        return depth


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

mySolution = Solution()
print(mySolution.maxDepth(root))
