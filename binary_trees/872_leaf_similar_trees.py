'''
872. Leaf-Similar Trees
Easy
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
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