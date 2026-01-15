# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree_values = self.in_order_traversal(root)
        tree_values.sort()
        
        return tree_values[k - 1]
    
    def in_order_traversal(self, root:Optional[TreeNode]) -> List[int]:
        visited = []
        stack = []
        
        while True:
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
print(solution.kthSmallest(root, 4))