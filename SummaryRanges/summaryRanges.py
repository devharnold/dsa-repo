# 228 - Summary Ranges

from typing import List

# start a value then loop again to see how many times
# a number is the increment of the start

# First find the start point
# then afterwards check if the current index i is equal to the next digit
# we are doing this to find the breakpoint
# if equal, increment else: that's the break point.
# move the starting point to the position of i at that point

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        i = 0

        while i < n:
            start_point = nums[i]
            #this is where we are to find the breakpoint
            while i < n - 1 and nums[i] + 1 == nums[i+1]:
                i += 1

            # check for whether the start point is equal to the current index of i
            # if not then break and move the start point to collect another sequence
            # when returning the answer, include the arrow(breakpoint)
            if start_point != nums[i]:
                ans.append(str(start_point) + '->' + str(nums[i]))
            else:
                ans.append(str(nums[i]))

            i += 1

        return ans