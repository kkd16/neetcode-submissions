class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if len(nums) < 1:
            return []
        
        out = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            out[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * suffix
            suffix = suffix * nums[i]

        return out