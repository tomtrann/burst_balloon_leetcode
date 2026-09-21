class Solution(object):
    def maxProfit(self, prices):
       l = 0 
       maxP = 0
       for r in range(1, len(prices)): 
        profit = prices[r] - prices[l]
        if prices[l] > prices[r]:
            l = r
        maxP = max(maxP, profit)
       return maxP