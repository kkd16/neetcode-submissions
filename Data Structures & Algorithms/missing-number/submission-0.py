class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n

        for n in range(len(nums) + 1):
            res ^= n

        return res
        