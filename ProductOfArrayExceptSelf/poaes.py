# 238 - Product of Array Except Self
from typing import List

"""
Example 1
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

At index 0, it will be product of 2, 3, 4
At index 1, it will be product of 1, 3, 4
At index 2, it will be product of 1, 2, 4
At index 3, it will be product of 1, 2, 3

At the index i, we store the product of all numbers except of that at that index
When i = "", exclude nums[""] but multiply the rest

You can decide to use O(n2) but this is going to be a slow brute force solution
Basically have two variables i, j i will be set to the current index then j will be the secondary indeces
if i = j don't do anything to that index, but then move j, if i != j then multiply the indeces

Aother thing is to set the current index at position 2 of the array,
then multiply elements on the left, then multiply all elements on the right
Afterwards multiply the product of elements of left and right



"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_ind = 1
        r_ind = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        

        for i in range(n):
            j = -i -1
            l_ind = l_arr
            r_ind = r_arr
            l_ind * nums[0] * n
            r_ind * nums[0] * n
            
