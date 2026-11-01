class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # can start at 0 or 1
        # iterate up to len(cost) + 1

        # each entry in dp array is the min cost to get to this step
        # base cases:
        # dp[0] = 0
        # dp[1] = 0 

        # at each step
        # take min of
        # dp[i - 2] + cost[i - 2]
        # dp[i - 1] + cost[i - 1]

        # T(i) = min(T(i - 1) + cost[i - 1], T(i - 2) + cost[i - 2]

        n = len(cost) + 1
        dp = [0] * n

        dp[0] = 0
        dp[1] = 0
        for i in range(2, n):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n - 1]
        