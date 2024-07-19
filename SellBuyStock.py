class Solution(object):
    def maxProfit(self, prices):
        l=len(prices)
        buy_price=prices[0]
        profit=0
        for i in range(l):
            if prices[i]<buy_price:
                buy_price=prices[i]
            else:
                current_profit=prices[i]-buy_price
                profit=max(current_profit,profit)
        return profit
