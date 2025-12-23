'''
Docstring for binary_search.706_binary_search:

704. Binary Search
Easy
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity. 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1
        mid_ptr = len(nums) // 2
        
        while left_ptr <= right_ptr:
            if nums[mid_ptr] == target:
                return mid_ptr
            elif nums[mid_ptr] < target:
                left_ptr = mid_ptr + 1
            else:
                right_ptr = mid_ptr - 1
                
            '''
                Problem does not exist in python as ints are unbounded. If in java, where int would have a max value of 32 bits, 2^31+
                it would cause an integer overflow, and mid_ptr would have an incorrect value, solution for this would be:
                mid_ptr = left_ptr + (right_ptr - left_ptr) // 2
                to get half of difference between right n left and add it to left ptr to prevent overflow.
            '''
            mid_ptr = (left_ptr + right_ptr) // 2
        return -1
    
    
print(Solution().search(
#   [-1,0,3,5,9,12],
    [-1,0,3,5,9,12],
    2
))