# 1822 - Sign of the product of an Array

from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # first initialize result to 1
        # then if n = 0, then the product will automatically be 0
        # if n < 0: this means that n is negative, multiply the result by -1
        # return the result
        result = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                result *= -1
        return result