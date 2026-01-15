from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_height(root, 0)

    def get_height(self, node: Optional[TreeNode], height: int) -> int:    
        if node is None:
            return height

        height = height + 1
        left_height = self.get_height(node.left, height)
        right_height = self.get_height(node.right, height)
        
        return max(left_height, right_height)