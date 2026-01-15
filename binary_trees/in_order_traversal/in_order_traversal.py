# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        
        self.__in_order_recursive(root, visited)
        return visited
    
    def __in_order_recursive(self, root: Optional[TreeNode], visited: List[int]):
        if root is None:
            return
        
        self.__in_order_recursive(root.left, visited)
        visited.append(root.val)
        self.__in_order_recursive(root.right, visited)
        
    def in_order_iterative(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        stack = []
        
        while True:
            # Keep adding left nodes to stack
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                root = stack.pop()
                visited.append(root.val)
                root = root.right
                
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

print(Solution().in_order_iterative(root))