'''
53. Maximum Subarray
Medium
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        
        for i, num in enumerate(nums):
            if curr_sum < 0:
                curr_sum = 0
                
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        
        return max_sum

'''
To get sub array values as well:
'''    
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        start = end = temp_start = 0
        
        for i, num in enumerate(nums):
            if curr_sum < 0:
                curr_sum = 0
                temp_start = i
                
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum >= max_sum:
                start = temp_start
                end = i
        
        return (start, end, max_sum)
    
    
arr = [-2, -11, -3, -4, -1, -2, -1, -5, -4]
print(Solution().maxSubArray(arr))