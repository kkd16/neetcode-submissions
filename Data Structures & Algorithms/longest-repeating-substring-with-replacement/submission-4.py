class Solution:

    def idx(self, c: str) -> int:
        return ord(c) - ord('A')
    
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        count = [0] * 26

        l = 0
        res = 0 
        for r in range(n):
            count[self.idx(s[r])] += 1

            while (r - l + 1 - max(count)) > k:
                count[self.idx(s[l])] -= 1
                l += 1

            res = max(res, r - l + 1)
 


        return res

            





        