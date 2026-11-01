class Solution:
    def rob(self, nums: List[int]) -> int:
        # go thru the nums and decide to rob this house or not
        # dp array at each dp[i] its the highest value robbery at this point
        # base cases, 
        # dp[0] = nums[0] because robbing first house is just nums[0] 
        # dp[1] = max(nums[0], nums[1])

        # dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        # return dp[n - 1

        n = len(nums)

        if n == 1:
            return nums[0]
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]

        