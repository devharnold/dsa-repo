#2264 - Largest 3-Same-Digit Number in String

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) < 3:
            return ""
        
        best_nums = ""
        for i in range(len(num) - 2):
            band = num[i:i+3]
            if band[0] == band[1] == band[2] and (not best_nums or band > best_nums):
                best_nums = band
                if best_nums == "999":
                    return best_nums
                
        return best_nums