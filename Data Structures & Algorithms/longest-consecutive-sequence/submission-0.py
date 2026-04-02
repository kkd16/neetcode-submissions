class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        max_run = 0
        for i in nums:
            k = i
            if k - 1 not in nums:
                run = []
                while k + 1 in nums:
                    run.append(k)
                    k += 1
                run.append(k)

                max_run = max(max_run, len(run))

        return max_run

                