# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return
        
        left_height = self.get_height(root.left, 0)
        right_height = self.get_height(root.right, 0)
        
        return abs(left_height - right_height) <= 1
    
    def dfs(self, root) -> Tuple[bool, int]:
        if root is None:
            return [True, 0]
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        is_balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1
        
        return [is_balanced, 1 + max(left[1], right[1])]
        

            

#       1
#      / \
#     2   3
#    / \
#   4   5
#  / \   \
# 6   7   8
#    / \   \
#   9  10   11
#           /
#          12
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.left.left.right = TreeNode(7)
root.left.right.right = TreeNode(8)
root.left.left.right.left = TreeNode(9)
root.left.left.right.right = TreeNode(10)
root.left.right.right.right = TreeNode(11)
root.left.right.right.right.left = TreeNode(12)

print(Solution().isBalanced(root))