'''
238. Product of Array Except Self
Medium
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

from typing import List


class Solution:
    
    '''
    Problem: ZERO division error
    '''
    def productExceptSelf_division(self, nums: List[int]) -> List[int]:
        all_product = 1
        answer = [1] * len(nums)
        for num in nums:
            all_product *= num
        
        for i, num in enumerate(nums):
            answer[i] = all_product // num
        
        return answer
    
    '''
    Having two arrays to store prefix and postfix values. Calculate the prefix from left to right, and postfix from right to left
    then get the product of the prefix and postfix values excluding the current index.
    '''
    def productExceptSelf_arr(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * len(nums)
        left_product_arr = [1] * len(nums)
        right_product_arr = [1] * len(nums)
        
        # left to right product
        for i in range(n):
            if i == 0:
                left_product_arr[i] = nums[i]
                continue
            left_product_arr[i] = left_product_arr[i - 1] * nums[i]
        
        # right to left products
        for i in range(n - 1, 0, -1):
            if i == n - 1:
                right_product_arr[i] = nums[i]
                continue
            right_product_arr[i] = right_product_arr[i + 1] * nums[i]
            
        for i in range(n):
            if i == 0:
                answer[i] = right_product_arr[i + 1]
            elif i == n - 1:
                answer[i] = left_product_arr[i - 1]
            else:
                answer[i] = left_product_arr[i - 1] * right_product_arr[i + 1]
        
        return answer
    
    
    '''
    O(n) time complexity. O(1) space complexity.
    Calculate prefix from left to right, and store it in index in answer array, so that when postfix is
    calculate from right to left, we can multiply the current prefix product stored at index of answer array
    with the postfix value.
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * len(nums)
        prefix = 1
        postfix = 1
        
        for i in range(n - 1):
            prefix *= nums[i]
            answer[i + 1] = prefix
     
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer
    
print(f"{Solution().productExceptSelf(
    # [-1,1,0,-3,3]
    [1,2,3,4]
)}")