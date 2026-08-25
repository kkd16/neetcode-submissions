class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in seen:
                return [seen[need], i]

            else:
                seen[n] = i

        return []
        