class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = float('-inf')
        curr = float('-inf')
        for i in nums:
            curr = max(curr + i, i)
            res = max(curr, res)

        return res

        