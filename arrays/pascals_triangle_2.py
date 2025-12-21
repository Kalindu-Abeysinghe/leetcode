'''
119. Pascal's Triangle II
Easy
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

'''
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]: # 2
        prev_arr = [1] # for rowIndex > 1
        
        for i in range(rowIndex):
            arr = [0] * (len(prev_arr) + 1)
            for j in range(len(prev_arr)):
                    arr[j] += prev_arr[j]
                    arr[j + 1] += prev_arr[j]
            print(prev_arr)
            prev_arr = arr
        
        return arr
            
print(Solution().getRow(4))