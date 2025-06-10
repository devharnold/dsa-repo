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

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pass
        
