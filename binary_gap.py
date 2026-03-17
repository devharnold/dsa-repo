class Solution:
    def binaryGap(self, n: int) -> int:
        curPos = 0
        lastPos = -1
        res = 0

        while n != 0:
            if (n & 1) == 1:
                if lastPos != -1:
                    res = max(res, curPos - lastPos)
                lastPos = curPos
            curPos += 1
            n >>= 1
        return res