class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0

        l = 0
        r = len(height) - 1

        ml = height[l]
        mr = height[r]

        while l < r:   
            if ml < mr:
                l += 1
                ml = max(ml, height[l])
                total += ml - height[l]
            else:
                r -= 1
                mr = max(mr, height[r])
                total += mr - height[r]

        return total
        