class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for a, b in zip(s, t):
            counts[ord(a) - ord('a')] += 1
            counts[ord(b) - ord('a')] -= 1

        return all(c == 0 for c in counts)


        