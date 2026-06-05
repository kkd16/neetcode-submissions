class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        m = 0

        for n in nums:
            length = 0
            if n - 1 not in s:
                while n + length in s:
                    length += 1
                m = max(m, length)

        return m


        