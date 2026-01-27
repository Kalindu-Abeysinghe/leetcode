'''

'''
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.pre_order_traversal(root1)
        self.pre_order_traversal(root2)
    
    def pre_order_traversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        stack = [root]
        leaf_nodes = []
        
        while stack:
            node = stack.pop()
            visited.append(node.val)
            if node.left is None and node.right is None:
                leaf_nodes.append(node)
                
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
        
        print(visited)
        print(leaf_nodes)
        return leaf_nodes