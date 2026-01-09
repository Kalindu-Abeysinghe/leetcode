'''
228. Summary Ranges
Easy
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
'''


from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        sub_range = []
        strt = 0
        
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i] + 1:
                # sub_range.append(nums[i])
                strt += 1
                if i == strt:
                    output.append(str(nums[i]))
                else:
                    output.append(f'{nums[strt]}->{nums[i]}')
            # else:
            #     print(sub_range)
            #     sub_range.append(nums[i])
            #     output.append(sub_range)
            #     sub_range = []
            
            # if i == len(nums):
            #     output.append(sub_range)
                
        return output
    
    
print(Solution().summaryRanges(
    [0,2,3,4,6,8,9]
))