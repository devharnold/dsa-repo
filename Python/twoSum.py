#!/usr/bin/env python3
# Python Two Sum problem

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff] - i]
            prevMap[n] = i
        
        return