class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        l = 0
        r = 0

        max_size = 0
        curr = set()

        while r < len(s):

            while s[r] in curr:
                curr.remove(s[l])
                l = l + 1

            curr.add(s[r])

            max_size = max(max_size, r - l  + 1)
            r = r + 1

        return max_size 


        
        