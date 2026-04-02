class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        max_run = 0
        for i in nums:
            k = i
            if k - 1 not in nums:
                length = 0
                while k + 1 in nums:
                    k += 1
                    length += 1

                max_run = max(max_run, length + 1)

        return max_run

                