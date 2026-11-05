class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = nums[0]
        currMax = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            prevMin = currMin
            prevMax = currMax

            currMax = max(nums[i], prevMin * nums[i], prevMax * nums[i])
            currMin = min(nums[i], prevMin * nums[i], prevMax * nums[i])

            res = max(res, currMax)

        return res
        