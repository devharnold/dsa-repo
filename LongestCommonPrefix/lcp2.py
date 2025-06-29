# 14 - Longest Common Prefix
# Vertical Search Approach

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        base_word = strs[0]
        for i in range(len(base_word)):
            for word in strs[:1]:
                if (i == len(word) or word(i) != base_word[i]):
                    return base_word[0:i]
                
        return base_word