class Solution:
    def idx(self, c: str) -> bool:
        return ord(c) - ord('a')
    
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_count = [0] * 26

        for c in s1:
            s1_count[self.idx(c)] += 1

        n = len(s1)

        s2_count = [0] * 26

        l = 0
        for r in range(len(s2)):

            s2_count[self.idx(s2[r])] += 1

            while r - l + 1 > n:
                s2_count[self.idx(s2[l])] -= 1
                l += 1

            if s1_count == s2_count:
                return True


        return False        