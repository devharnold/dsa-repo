class Solution {
    public int binaryGap(int n) {
        int lastPos = -1;
        int curPos = 0;
        int res = 0;

        while (n != 0) {
            if ((n & 1) == 1) {
                if (lastPos != -1) {
                    int distance = curPos - lastPos;
                    // raw difference in bit positions : different from Codility
                    res = Math.max(res, curPos - lastPos);
                }
                lastPos = curPos;
            }
            curPos++;
            n >>= 1;
        }
        return res;
    }
}


