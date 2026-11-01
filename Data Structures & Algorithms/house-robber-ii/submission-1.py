class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def house_rob(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                new = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = new

            return rob2

        return max(nums[0], house_rob(nums[1:]), house_rob(nums[:-1]))

        