# 1768 Merge Strings ALternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        result = ""

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]
                i += 1
            if j < len(word2):
                result += word2[j]
                j += 1

        return result

# Explanation
"""
First set 2 different pointers, 
one will point of the first character of word1 and the other will point to the last character of word2
Then while on both word1 and word2,
Take both characters alternately between word1 and word2 until both strings are done
Then return the merged string.
"""