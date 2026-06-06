class Solution:

    def idx(self, c: str) -> int:
        return ord(c) - ord('A')
    
    def characterReplacement(self, s: str, k: int) -> int:

        counts = [0] * 26

        l = 0

        res = 0
        
        for r in range(len(s)):
            c = s[r]
            idx = self.idx(c)

            counts[idx] +=1

            wlen = r - l + 1
            if wlen - max(counts) > k:
                counts[self.idx(s[l])] -= 1

                l += 1
                wlen -= 1
                
            res = max(res, wlen)



        return res

            





        