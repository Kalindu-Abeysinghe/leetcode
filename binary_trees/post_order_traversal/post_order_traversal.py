# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        
        self.__post_order_recursive(root, visited)
        return visited
    
    def __post_order_recursive(self, root: Optional[TreeNode], visited: List[int]):
        if root is None:
            return
        
        self.__post_order_recursive(root.left, visited)
        self.__post_order_recursive(root.right, visited)
        visited.append(root.val)
    
        
    # TODO: Fix this!!!
    def post_order_iterative(self, root: Optional[TreeNode]) -> List[int]:
        visited = []
        stack = []

        while True:
            if root is not None:
                stack.append(root.left)
                root = root.left
            else:
                if not stack:
                    break
                
                root = stack.pop()
                if root.right:
                    root = root.right
                visited.append(root.val)
                root = root.right
                
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

print(Solution().postorderTraversal(root))