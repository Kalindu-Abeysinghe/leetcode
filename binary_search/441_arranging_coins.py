'''
441. Arranging Coins
Easy
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
'''


class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        
        while low < high:
            mid_ptr = (low + high) // 2 
            k = (mid_ptr * (mid_ptr + 1)) // 2
            
            if k < n:
                low = mid_ptr + 1
            elif k > n:
                high = mid_ptr - 1
            else:
                return mid_ptr
            
        return high
    

print(Solution().arrangeCoins(
    8
))