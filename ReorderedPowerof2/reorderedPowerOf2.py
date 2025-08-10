# 869 - Reordered power of 2

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = {"".join(sorted(str(1 << i))) for i in range(31)} # range between 2^0 - 2^30

        return "".join(sorted(str(n))) in powers