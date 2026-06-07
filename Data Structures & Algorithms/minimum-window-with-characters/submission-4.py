class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # count characters in t

        # l and r pointers
        # both start at zero
        # keep increasing r until we find a valid substring
        #     valid if:
        #     check every letter in t in the counter and if the corresponding letter
        #     in s is >= then valid
        #
        # then, keep increasing l until its no longer valid (save the last valid)
        # then, increase l once more and then repeat by increasing r again
        # keep track of the valid MINIMUM length as we go


        #  OUZODYXAZVAAAAXYZ

        n = len(s)

        if n < len(t):
            return ""
        
        t_count = collections.Counter(t)

        l = 0
        s_count = collections.Counter()

        def valid():
            for c in t_count:
                if s_count[c] < t_count[c]:
                    return False

            return True
        
        res_l = -1
        res_r = -1
        for r in range(n):
            s_count[s[r]] += 1

            while valid():

                if res_l == -1 or ((r - l + 1) < (res_r - res_l + 1)):
                    res_l = l
                    res_r = r

                s_count[s[l]] -= 1
                l += 1


           

        return s[res_l : res_r + 1]
        