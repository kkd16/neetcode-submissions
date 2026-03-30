class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort the array
        # iterate the first element 

        # it reduces to 2 sum


        nums.sort()

        ret = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l = l + 1

                    while l < r and nums[l] == nums[l - 1]:
                        l = l + 1
                
                elif s < 0:
                    l = l + 1
                
                elif s > 0:
                    r = r - 1

        
        return ret





        