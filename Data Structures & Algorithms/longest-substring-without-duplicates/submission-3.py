class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0

        cur = set()

        m = 0

        while r < len(s):
            while s[r] in cur:
                cur.remove(s[l])
                l += 1
            
            cur.add(s[r])
            m = max(r - l + 1, m)

            r += 1

        return m

        
            
        

        