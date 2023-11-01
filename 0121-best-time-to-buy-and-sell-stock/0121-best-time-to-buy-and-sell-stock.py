class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =0
        right =1
        p = 0
        while right < len(prices):
            curp = prices[right] - prices[left] 

            if prices[left] < prices[right]:
                p = max(curp, p) 
            else:
                left = right
            right += 1
        return p