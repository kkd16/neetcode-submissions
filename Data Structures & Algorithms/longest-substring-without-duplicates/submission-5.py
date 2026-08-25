class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        curr = set()

        l = 0

        m = 0
        for r in range(len(s)):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1

            curr.add(s[r])

            m = max(m, len(curr))

        return m

                

        