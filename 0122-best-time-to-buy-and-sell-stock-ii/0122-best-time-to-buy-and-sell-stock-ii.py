class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: # edge case
            return 0
        

        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit