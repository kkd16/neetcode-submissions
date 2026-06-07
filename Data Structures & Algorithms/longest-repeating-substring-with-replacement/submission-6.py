class Solution:
    def idx(self, c: str) -> int:
        return ord(c) - ord('A')

    def characterReplacement(self, s: str, k: int) -> int:

        # loop through the string
        # keep a l and r pointer
        # it will be a sliding window
        # keep a count of all the characters in the window
        # take the most frequent element's COUNT
        # its a valid assignment if the window length - count <= k
        # keep a counter of the max VALID window length we've seen so far
        
        l = 0

        count = [0] * 26

        res = 0
        for r, c in enumerate(s):
            count[self.idx(c)] += 1

            while (r - l + 1) - max(count) > k:
                count[self.idx(s[l])] -= 1
                l += 1

            res = max(r - l + 1, res)

        return res

            

                






        