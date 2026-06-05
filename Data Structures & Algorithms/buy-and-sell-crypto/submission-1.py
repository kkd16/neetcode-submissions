class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        m = prices[0]

        for p in prices:
            m = min(m, p)

            profit = max(profit, p - m)

            

        return profit


        