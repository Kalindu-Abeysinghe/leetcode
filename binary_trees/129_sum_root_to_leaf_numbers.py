# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []
        self.dfs(root, paths, [])
        return sum(paths)
    
    def dfs(self, node: Optional[TreeNode], paths: List[int], current_path: List[int]):
        current_path.append(node.val)
        print(f'at node: {node.val}')
        
        if node.left is None and node.right is None:
            rtl_sum = int("".join(str(val) for val in current_path))
            print(f'rtl_sum: {rtl_sum}')
            paths.append(rtl_sum)
        
        if node.left:
            self.dfs(node.left, paths, current_path)
            
        if node.right:
            self.dfs(node.right, paths, current_path)
        
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
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
solution = Solution()
print(solution.sumNumbers(root))