import unittest
from in_order_traversal import Solution, TreeNode


class TestInOrderTraversal(unittest.TestCase):
    
    def test_complete_binary_tree_inorder(self):
        """Complete binary tree with 15 nodes - in-order traversal"""
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
        in_order_traversed = solution.inorderTraversal(root)
        print(in_order_traversed)
        self.assertEqual(
            solution.inorderTraversal(root),
            [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]
        )
        
        
if __name__ == '__main__':
    unittest.main()