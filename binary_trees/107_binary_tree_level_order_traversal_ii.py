'''
107. Binary Tree Level Order Traversal II
Medium
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).
'''
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        queue = [root]
        
        while queue:
            for i in range(len(queue)):
                if i == 0:
                    levels.append([node.val for node in queue])
                
                node = queue.pop()
                
                if node.right:
                    queue.insert(0, node.right)
                    
                if node.left:
                    queue.insert(0, node.left)
                    

        
        levels.reverse()
        return levels
    


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
print(solution.levelOrderBottom(root))