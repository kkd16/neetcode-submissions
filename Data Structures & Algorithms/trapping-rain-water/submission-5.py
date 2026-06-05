class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0

        n = len(height)

        l = 0
        r = n - 1

        m_l = height[0]
        m_r = height[n-1]

        total = 0
        while l < r:
            c = 0
            if m_l < m_r:
                l += 1
                m_l = max(m_l, height[l])
                total += m_l - height[l]
            else:
                r -= 1
                m_r = max(m_r, height[r])
                total += m_r - height[r]

        return total
        