class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        current_chars = set()

        l = 0
        
        m = 0
        for r in range(len(s)):
            
            while s[r] in current_chars:
                current_chars.remove(s[l])
                l +=1

            current_chars.add(s[r])

            m = max(m, r - l + 1)

        return m


        