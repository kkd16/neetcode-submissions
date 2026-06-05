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
                c = m_l - height[l]
                l += 1
                m_l = max(m_l, height[l])
            else:
                c = m_r - height[r]
                r -= 1
                m_r = max(m_r, height[r])
            
            if c > 0:
                total += c
                
            

        return total
            
        