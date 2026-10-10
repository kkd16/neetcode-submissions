class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) == 0 or len(s2) == 0 or len(s2) < len(s1):
            return False


        count_1 = [0] * 26
        count_2 = [0] * 26
        
        for c1, c2 in zip(s1, s2):
            count_1[ord(c1) - ord('a')] += 1
            count_2[ord(c2) - ord('a')] += 1

        if count_1 == count_2:
            return True

        n = len(s1)

        for r in range(n, len(s2)):
            count_2[ord(s2[r]) - ord('a')] += 1
            count_2[ord(s2[r - n]) - ord('a')] -= 1

            if count_1 == count_2:
                return True

        return False


        