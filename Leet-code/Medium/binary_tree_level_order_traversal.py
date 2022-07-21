# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a Node.
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = deque([[root, 0]])
        val = []

        while queue:
            node, index = queue.popleft()
            if len(val) > index:
                val[index].append(node.val)
            else:
                val.append([node.val])

            if node.left:
                queue.append([node.left, index + 1])
            if node.right:
                queue.append([node.right, index + 1])

        return val


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

mySolution = Solution()
print(mySolution.levelOrder(root))
