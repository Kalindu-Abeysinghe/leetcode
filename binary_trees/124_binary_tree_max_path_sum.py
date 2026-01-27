'''
124. Binary Tree Maximum Path Sum
Hard
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

'''


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]
            
        def dfs(node):
            if node is None:
                return 0
        
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            result[0] = max(result[0], node.val + left_max + right_max)
            
            return node.val + max(left_max, right_max)
        
        dfs(root)
        return result[0]

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# root.left.left.left = TreeNode(8)
# root.left.left.right = TreeNode(9)
# root.left.right.left = TreeNode(10)
# root.left.right.right = TreeNode(11)
# root.right.left.left = TreeNode(12)
# root.right.left.right = TreeNode(13)
# root.right.right.left = TreeNode(14)
# root.right.right.right = TreeNode(15)
solution = Solution()
print(solution.maxPathSum(root))