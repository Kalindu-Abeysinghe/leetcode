'''
367. Valid Perfect Square
Easy
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        divisor = 1
        sqrt = num // divisor
        
        while sqrt * sqrt > num:
            divisor += 1
            sqrt = num // divisor
            
        if sqrt * sqrt == num:
            return True
        else:
            return False

'''
Solution which follows binary search exactly:
'''
def isPerfectSquare(self, num: int) -> bool:
    left, right = 1, num

    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 == num:
            return True
        elif mid ** 2 < num:
            left = mid + 1
        else:
            right = mid - 1

    return False
        
print(Solution().isPerfectSquare(
    1
))

import math
math.sqrt = lambda x: "No square roots allowed"
print(math.sqrt(9))

test1 = lambda x: x + 4
print(test1(2))

print(Solution.__mro__)

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "red"]
fruit_colors = {key: value for key, value in zip(fruits, colors)}
print(fruit_colors)

print(repr(fruits))