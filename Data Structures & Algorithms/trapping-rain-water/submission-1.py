class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l_height = [0] * n
        r_height = [0] * n

        for i in range(1, n):
            l_height[i] = max(l_height[i-1], height[i-1])

        for i in range(n - 2, -1, -1):
            r_height[i] = max(r_height[i+1], height[i+1])

        print(l_height)
        print(r_height)


        total = 0

        for i in range(n):
            c = min(l_height[i], r_height[i]) - height[i]
            if c > 0:
                total += c

        return total
            
        