class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l = [1] * (n + 1)
        r = [1] * (n + 1)
        for i in range(0, n):
            l[i + 1] = l[i] * nums[i]

        for i in range(n - 1, -1, -1):
            r[i - 1] = r[i] * nums[i] 

        return [l[i] * r[i] for i in range(n)] 
        