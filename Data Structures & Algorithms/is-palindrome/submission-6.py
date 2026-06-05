class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        s = s.strip()

        l = 0
        r = len(s) - 1
        while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            # if not l < r:
            #     return True

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
        