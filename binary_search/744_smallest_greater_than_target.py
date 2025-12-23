'''
744. Find Smallest Letter Greater Than Target
Easy
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

'''

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left_ptr = 0
        right_ptr = len(letters) - 1
        smallest = letters[0]
        
        while left_ptr <= right_ptr:
            mid_ptr = (left_ptr + right_ptr) // 2
            '''
                If mid point value is greater than target, we need to bring right ptr to one less than mid point
            '''
            if letters[mid_ptr] > target:
                smallest = letters[mid_ptr]
                right_ptr = mid_ptr - 1
            else:
                left_ptr = mid_ptr + 1
        
        return smallest
    
print(Solution().nextGreatestLetter(
    ["c","f","j"],
    'c'
))