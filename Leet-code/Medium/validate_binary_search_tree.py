# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        # if root.left and not root.right: return False
        # if root.right and not root.left: return False
        if root == None:
            return False

        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.val >= root.right.val:
            return False

        if root.left and root.left.left != None:
            self.isValidBST(root.left)
        if root.right and root.right.right != None:
            self.isValidBST(root.right)

        return True


root = TreeNode(5, TreeNode(1), TreeNode(9, TreeNode(7), TreeNode(10)))

mySolution = Solution()
print(mySolution.isValidBST(root))
