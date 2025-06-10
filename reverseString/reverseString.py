from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """Do not return anything, modify s in-place instead."""
        """Solution:
        First convert the string into a list
        Then using the two-pointers approach, set one pointer at the first index of the list then another one at the last index
        Then move the pointers in opposite direction
        """
        left = 0
        right = (len(s) - 1)

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
