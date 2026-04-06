class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l is buy
        #r is sell 
        l, r = 0, 1
        max_profit = 0 

        while r < len(prices):
            if prices[l] < prices[r]:
                #buy is less than sell = profit 
                current_profit = prices[r] - prices[l]
                if current_profit > max_profit:
                    max_profit = current_profit
            else: 
                #if prices[l] > prices[r]
                #this means buy is larger than r, we set l = r 
                #we want to buy at r since r is cheaper 
                l = r 
            r += 1
        return max_profit
