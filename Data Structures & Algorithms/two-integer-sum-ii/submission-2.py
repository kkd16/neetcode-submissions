class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        r = len(numbers) - 1
        l = 0

        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else: 
                return [l + 1, r + 1]

        return []


        