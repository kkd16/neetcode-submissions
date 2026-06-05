class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)

        m = 0
        for c in s:
            if c - 1 not in s:
                length = 0
                while c + length in s:
                    length += 1
                m = max(m, length)

        return m


        