class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)

        m = 0
        for c in s:
            if c - 1 not in s:
                curr = c
                count = 1
                while curr + 1 in s:
                    count += 1
                    curr = curr + 1
                m = max(m, count)

        return m


        