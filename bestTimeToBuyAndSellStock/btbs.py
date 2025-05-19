# 121 - Best Time To Buy And Sell Stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0

        for i in range(0, len(prices) -1): # ook for the buying price
            for j in range(i + 1, len(prices)): # look for the selling price
                curr_profit = max(curr_profit, prices[j] - prices[i]) # return the max value interms of profit

        return curr_profit