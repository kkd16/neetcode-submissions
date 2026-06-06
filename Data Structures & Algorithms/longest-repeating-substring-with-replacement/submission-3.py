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

            window_len = r - l + 1

            if (window_len - max(count)) > k:
                count[self.idx(s[l])] -= 1
                l += 1

            window_len = r - l + 1
            res = max(res, window_len)
 


        return res

            





        