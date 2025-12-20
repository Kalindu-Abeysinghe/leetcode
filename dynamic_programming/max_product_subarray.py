from typing import List

'''
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr_len = len(nums)
        max_product = - float("inf")
        cache = {}
        sub_arr = []
        if(arr_len == 1):
            return nums[0]
        
        for sub_arr_len in range(1, arr_len + 1):
            start = 0
            end = start + (arr_len - sub_arr_len + 1)
            for i in range(start, end):
                product = 1
                sub_problem = tuple(nums[i: i + sub_arr_len])
                print(f"subproblem: {sub_problem}")
                if cache.get(sub_problem) is not None:
                    continue
                for num in sub_problem:
                    product = product * num
                cache[sub_problem] = product
                if product > max_product:
                    sub_arr = nums[i: i + sub_arr_len]
                    max_product = product
        return max_product
    
    def max_product_optimised(selff, nums):
        result = max(nums)
        currMin, currMax = 1, 1
        
        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
                continue
            
            temp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(temp, num * currMin, num)
            
            result = max(result, currMax, currMin)
        
        return result
    
print(Solution().max_product_optimised(
    # [-4,-3]
    [2,3,-2,4]
))