class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        l = 0
        r = n - 1

        res = 0
        while l < r:
            curr = (r - l) * min(heights[l], heights[r])

            res = max(res, curr)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res






        