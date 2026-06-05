class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        trips = []

        for k in range(len(nums) - 2):

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = len(nums) - 1

            while i < j:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    trips.append([nums[k], nums[i], nums[j]])
                    
                    while j > 0 and nums[j] == nums[j - 1]:
                        j -= 1

                    while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                        i += 1

                    i += 1
                    j -= 1

                elif s > 0:
                    j -= 1
                elif s < 0:
                    i += 1



        return trips





        