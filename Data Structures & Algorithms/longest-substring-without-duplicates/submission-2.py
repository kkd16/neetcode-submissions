class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0

        curr = set()

        max_length = 0
        for r, c in enumerate(s):
            while c in curr:
                curr.remove(s[l])
                l = l + 1

            curr.add(c)
            max_length = max(max_length, r - l + 1)



        return max_length






        
        