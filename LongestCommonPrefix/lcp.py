#14 - Longest Common Prefix
from typing import List

# Binary Search Approach

# First check if we have strings, if not then return empty string
# Break the string into two parts i.e (find the midpoint, we'll work with the first half, thats the left part)
# Find the midpoint,min length and the low, high values
# If you find midpoint and the helper function is true, calculate the
# length of the longest prefix from the first index of the string upto the midpoint
# we're dealing with the first-half of the string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_length = min(len(s) for s in strs)
        low, high = 1, min_length

        while low <= high:
            mid = (low + high) // 2
            if self.isCommonPrefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][: (low + high) // 2]
    
    def isCommonPrefix(self, strs: List[str], length: int) -> bool:
        prefix = strs[0][:length]
        return all(s.startswith(prefix) for s in strs)

# More solutions include using Brute Force, Divide and Conquer or even a Trie