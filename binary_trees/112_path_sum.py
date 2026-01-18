# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum, 0, False)
    
    def dfs(self, node: Optional[TreeNode], targetSum: int, current_sum: int, target_found: bool) -> bool:
        current_sum += node.val
        
        if node.left is None and node.right is None:
            if current_sum == targetSum:
                target_found = True
                return True
        
        if node.left:
            target_found = target_found or self.dfs(node.left, targetSum, current_sum, target_found)
            current_sum -= node.val
            
        if node.right:
            target_found = target_found or self.dfs(node.right, targetSum, current_sum, target_found)
            current_sum -= node.val
        
        return target_found
        


#           1
#        /     \
#       2       3
#      / \     / \
#     4   5   6   7
#    / \ / \ / \ / \
#   8  9 10 11 12 13 14 15
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)
solution = Solution()
print(solution.hasPathSum(root, 10000))