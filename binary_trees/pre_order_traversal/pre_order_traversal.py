# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        
        self.__pre_order_recursive(root, visited)
        return visited
    
    def __pre_order_recursive(self, root: Optional[TreeNode], visited: List[int]):
        if root is None:
            return
        
        visited.append(root.val)
        self.__pre_order_recursive(root.left, visited)
        self.__pre_order_recursive(root.right, visited)
        
    def pre_order_iterative(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        stack = [root]
        
        if root is None:
            return []
        
        while stack:
            root = stack.pop()
            visited.append(root.val)
            
            # right pushed first so that it is visited after left for pre order traversal
            if root.right:
                stack.append(root.right)
    
            if root.left:
                stack.append(root.left)
        
        return visited
    
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().pre_order_iterative(root))