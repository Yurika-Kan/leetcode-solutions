# Last updated: 3/23/2026, 1:26:40 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        maxP = 0
4        minBuy = prices[0]
5
6        for sell in prices: 
7            # max price = prev max or sell current price from our min buy
8            maxP = max(maxP, sell - minBuy)
9            # min buy = prev min buy or current price
10            minBuy = min(minBuy, sell)
11        return maxP
12    
13    # Time: O(n)
14    # Space: O(1)