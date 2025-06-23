#58 - Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:
            return 0
        return len(words[-1])
    

"""First split the sentence into words
Then check if not words
(words[-1]) is the last word within that sentence
len(words[-1]) determines the length of a word"""