'''
1022. Sum of Root To Leaf Binary Numbers
Easy
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
'''
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        current_path = []
        paths = []
        self.dfs(root, paths, current_path)
        
        int_sum = sum(int(str(bin_val), 2) for bin_val in paths)
        return int_sum
    
    def dfs(self, node: Optional[TreeNode], paths: List[int], current_path: List[int]):
        current_path.append(node.val)
        
        if node.left is None and node.right is None:
            paths.append(int("".join(str(val) for val in current_path)))
            
        if node.left:
            self.dfs(node.left, paths, current_path)
            
        if node.right:
            self.dfs(node.right, paths, current_path)
            
        current_path.pop()