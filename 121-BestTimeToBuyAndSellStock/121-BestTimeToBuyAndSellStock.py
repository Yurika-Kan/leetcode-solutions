# Last updated: 6/9/2025, 5:25:47 PM
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit

        """
        :type prices: List[int]
        :rtype: int
        """
        