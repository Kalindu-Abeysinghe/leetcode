'''
Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

Example

Function Description

Complete the pairs function below.

pairs has the following parameter(s):

int k: an integer, the target difference
int arr[n]: an array of integers
Returns

int: the number of pairs that satisfy the criterion
Input Format

The first line contains two space-separated integers  and , the size of  and the target value.
The second line contains  space-separated integers of the array.
'''


def pairs(k, arr):
    counter = 0
    set_arr = set(arr)
    for val in arr:
        if val + k in set_arr:
            counter += 1
    return counter

print(pairs(2, [1, 5, 3, 4, 2]))