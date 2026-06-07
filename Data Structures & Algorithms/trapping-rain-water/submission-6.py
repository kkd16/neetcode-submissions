class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0

        l = 0
        r = len(height) - 1

        ml = height[l]
        mr = height[r]

        while l < r:
            
            if ml < mr:
                total += ml - height[l]
                l += 1
                ml = max(ml, height[l])
            else:
                total += mr - height[r]
                r -= 1
                mr = max(mr, height[r])

        return total
        