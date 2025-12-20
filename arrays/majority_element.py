'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

'''

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        majority_element = None
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
            if count_dict[num] > (len(nums) / 2):
                majority_element = num
        return majority_element
    
print(f"{Solution().majorityElement(
    [2,2,1,1,1,2,2]
)}")