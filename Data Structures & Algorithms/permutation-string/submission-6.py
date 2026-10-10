class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) == 0 or len(s2) == 0 or len(s2) < len(s1):
            return False


        count_1 = [0] * 26
        for c in s1:
            count_1[ord(c) - ord('a')] += 1

        n = len(s1) 

        count_2 = [0] * 26

        for i, c in enumerate(s2):
            if i > n - 1:
                count_2[ord(s2[i - n]) - ord('a')] -= 1

            count_2[ord(c) - ord('a')] += 1

            if count_1 == count_2:
                return True

        return False


        