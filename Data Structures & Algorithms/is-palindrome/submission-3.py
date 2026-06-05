class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        s = s.strip()

        l = 0
        r = len(s) - 1
        while l < r:

            while not s[l].isalnum() and l < len(s) - 1:
                l += 1

            while not s[r].isalnum() and r > 0:
                r -= 1

            if not l < r:
                return True

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
        