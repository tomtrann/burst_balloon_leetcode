class Solution(object):
    def maxProfit(self, prices):
       l = 0 
       maxP = 0
       for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r
       return maxP
            
