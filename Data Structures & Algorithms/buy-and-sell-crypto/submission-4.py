class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        b = prices[0]

        for p in prices:
            profit = max(profit, p - b)
            if p < b:
                b = p

        return profit


        