# 13 - Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        i = 0

        """
        Using this example:
        Input s = "MCMXCIV"
        M  C  M  X  C  I  V

        Output = 1994"""

        while i < len(s):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                sum += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2
            else:
                sum += roman_map[s[i]]
                i += 1

        return sum