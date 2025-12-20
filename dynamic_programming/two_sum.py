from typing import List

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

class Solution:
    '''
    Biggest possible time complexity: O(n x n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
                
    '''
    Time complexity is O(n)
    '''
    def two_sum_hash_map(self, nums: List[int], target: int):
        hash_map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map and i != hash_map.get(nums[i]):
                return [hash_map.get(difference), i]
            else:
                hash_map[nums[i]] = i
                
print(f"Output: {Solution().two_sum_hash_map(
    [3,2,4],
    6
)}")