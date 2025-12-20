'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 10
'''

def get_binary(number):
    base = 2
    val = ''
    curr = number
    while curr >= 1:
        rem = curr % base
        curr = curr // base
        val = str(rem) + val
        
    return val

def count_ones(binary_val):
    count = 0
    for char in binary_val:
        if char == '1':
            count += 1
    return count

def countBits(n: int):
    ans = []
    for i in range(n + 1):
        ans.append(count_ones(get_binary(i)))
        
    return ans

print(countBits(5))