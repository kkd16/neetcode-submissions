class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        ret = []


        l = 1
        r = len(nums) - 1

        i = 0   

        # iterate i up, 
        # reduce to 2 sum with sorted arary 

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                if s > 0:
                    r -= 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                if s < 0:
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        return ret    