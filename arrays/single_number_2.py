'''
137. Single Number II
Medium
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memo = {n: 0 for n in nums}
        for num in nums:
            memo[num] += 1
        for num, count in memo.items():
            if count == 1:
                return num
        
print(Solution().singleNumber(
    [0,1,0,1,0,1,99]
))