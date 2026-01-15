# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        visited = []
        stack = [root]
        leaf_sum = 0
        
        # pre order traversal iterative:
        while stack:
            root = stack.pop()
            visited.append(root.val)
            
            if root.left:
                child = root.left
                if child.left is None and child.right is None:
                    leaf_sum += child.val
            
                stack.append(root.left)
                
            if root.right:
                stack.append(root.right)
                
        return leaf_sum