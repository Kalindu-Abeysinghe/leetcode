# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# [1, 2, 3]

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left_ptr = 1
        right_ptr = n

        while left_ptr < right_ptr:
           mid_ptr = (left_ptr + right_ptr) // 2
           if isBadVersion(mid_ptr):
                right_ptr = mid_ptr
           else:
               left_ptr = mid_ptr + 1

        return left_ptr