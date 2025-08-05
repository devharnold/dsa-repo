# 15 - 3Sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            # check for duplicates of i and skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # convert the problem to a simple 2sum problem
            # in the equation move nums[i] to the other side then use -nums[i] as the target
            # so we'll check if nums[j] + nums[k] == -nums[i]
            target = -nums[i]
            j, k = i + 1, n - 1

            while j < k:
                two_sum = nums[j] + nums[k]
                if two_sum == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # check for the duplicates of j then skip
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # check for the duplicates of k then skip
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif two_sum < target:
                    j += 1
                else:
                    k -= 1

        return result