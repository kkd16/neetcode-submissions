class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = 0

        profit = 0

        for i in range(len(prices)):
            if prices[i] < prices[min]:
                min = i

            sale = prices[i] - prices[min]

            if sale > profit:
                profit = sale


        return profit

            
        