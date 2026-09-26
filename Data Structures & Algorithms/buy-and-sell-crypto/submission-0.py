class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for price in prices:
            if price < buy: buy = price
            else:
                profit = price - buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit