# 2239 Find Closest Number to 0
from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0] # initialize with the first element
        for x in nums: # iterate through all numbers
            if abs(x) < abs(closest): # if x is closer to the absolute number
                closest = x

        # here if the closest number is negative and we have a positive in the list, return the positive one
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest