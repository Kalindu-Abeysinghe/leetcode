import unittest
from pre_order_traversal import Solution, TreeNode


class TestPreOrderTraversal(unittest.TestCase):
    
    def test_deep_left_heavy_tree(self):
        """Tree heavily weighted to the left with 12 nodes"""
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
        solution = Solution()
        traversed_values = solution.pre_order_iterative(root)
        print(traversed_values)
        self.assertEqual(
            traversed_values,
            [1, 2, 4, 6, 7, 9, 10, 5, 8, 11, 12, 3]
        )
        
        
if __name__ == '__main__':
    unittest.main()