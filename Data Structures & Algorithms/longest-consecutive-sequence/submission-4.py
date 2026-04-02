class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        max_run = 0
        for i in nums:
            if i - 1 not in nums:
                length = 0
                while i + length in nums:
                    length += 1

                max_run = max(max_run, length)

        return max_run

                