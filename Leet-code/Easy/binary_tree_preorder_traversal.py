# from typing import List, Optional
# Given the root of a binary tree, return the preorder traversal of its nodes' values.


# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]

# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        val = []

        def traverse(node):
            if node == None:
                return

            val.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return val


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

mySolution = Solution()
print(mySolution.preorderTraversal(root))
