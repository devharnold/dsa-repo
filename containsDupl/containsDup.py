# Contains Duplicate Solution

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution approach
        present_nums = set()
        for i in nums:
            if i in present_nums:
                return True
            present_nums.add(i)
        
        return False


# Create a new Set for the pre-existing numbers
# Loop through the list of numbers, as you search for whether they are distinct or duplicate
# If the index was in the pre-existing set, return True then add the number to the set
# Return False -> This means that it is not duplicate(not present in the set)

#Big O Notation --> O(n)