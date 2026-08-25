class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sc = collections.Counter(s)
        tc = collections.Counter(t)

        return sc == tc
        