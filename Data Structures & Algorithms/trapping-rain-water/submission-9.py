class Solution:
    def trap(self, height: List[int]) -> int:

        l_prefix = [0] * len(height)
        r_prefix = [0] * len(height)

        for i in range(1, len(height)):
            l_prefix[i] = max(l_prefix[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            r_prefix[i] = max(r_prefix[i + 1], height[i + 1])

        total = 0
        for i in range(len(height)):
            c = max(min(l_prefix[i], r_prefix[i]) - height[i], 0)
            total += c

        return total        