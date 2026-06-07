class Solution:
    def idx(self, c: str) -> int:
        return ord(c) - ord('a')
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        s1_count = [0] * 26

        for c in s1:
            s1_count[self.idx(c)] += 1

        s2_count = [0] * 26

        for i in range(n):
            s2_count[self.idx(s2[i])] += 1

        if s1_count == s2_count:
            return True

        for i in range(n, len(s2)):
            s2_count[self.idx(s2[i])] += 1
            s2_count[self.idx(s2[i - n])] -= 1

            if s1_count == s2_count:
                return True

        return False        