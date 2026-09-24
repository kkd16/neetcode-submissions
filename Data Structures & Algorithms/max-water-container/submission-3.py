class Solution:
    def maxArea(self, heights: List[int]) -> int:


        l = 0
        r = len(heights) - 1

        max_volume = 0

        while l < r:
            volume = (r - l) * min(heights[l], heights[r])
            max_volume = max(max_volume, volume)

            if heights[l] < heights[r]:
                l += 1

            elif heights[r] < heights[l]:
                r -= 1

            else:
                l += 1

        return max_volume





        