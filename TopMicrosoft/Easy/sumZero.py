# 1304 - Find N Unique Integers Sum Upto Zero
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        sum = []

        # first lets check if n is odd
        if n % 2:
            sum.append(0)
        
        # check upto the last bound inclusive
        for i in range(1, n // 2 + 1):
            sum.append(i)
            sum.append(-i)

        return sum
