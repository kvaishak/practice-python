# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true

# https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def compare(left, right):

            if left == None and right == None:
                return True

            if left == None or right == None or left.val != right.val:
                return False

            return compare(left.left, right.right) and compare(left.right, right.left)

        return compare(root.left, root.right)


root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3)))

mySolution = Solution()
print(mySolution.isSymmetric(root))
