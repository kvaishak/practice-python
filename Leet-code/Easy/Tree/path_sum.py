# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.


# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, cumSum=None) -> bool:

        if not root:
            return False

        cumSum = root.val if cumSum == None else cumSum + root.val

        if not root.left and not root.right and cumSum == targetSum:
            return True

        return self.hasPathSum(root.left, targetSum, cumSum) or self.hasPathSum(root.right, targetSum, cumSum)


root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
targetSum = 22

mySolution = Solution()
print(mySolution.hasPathSum(root, targetSum))


# Another way of doing it without an extra variable for storing the cumilative sum
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root: return False
#         if not root.left and not root.right and root.val == targetSum: return True
#         return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
