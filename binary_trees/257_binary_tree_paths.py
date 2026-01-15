# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        current_path = []
        paths = []
        self.dfs(root, current_path, paths)
        
        return paths
    
    def dfs(self, node: Optional[TreeNode], current_path: List[str], paths: List[int]):
        current_path.append(node.val)
        
        if node.left is None and node.right is None:
            paths.append("->".join(str(val) for val in current_path))
        
        if node.left:
            self.dfs(node.left, current_path, paths)
            current_path.pop()
            
        if node.right:
            self.dfs(node.right, current_path, paths)
            current_path.pop()

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
print(solution.binaryTreePaths(root))