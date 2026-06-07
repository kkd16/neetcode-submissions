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
        
        s_count = collections.Counter()
        t_count = collections.Counter(t)

        l = 0

        need = len(set(t))
        have = 0
        
        best_start = 0
        best_len = float('inf')

        for r in range(n):
            s_count[s[r]] += 1

            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < best_len:
                    best_len = r - l + 1
                    best_start = l

                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    have -= 1
            
                l += 1


        return "" if best_len == float('inf') else s[best_start : best_start + best_len]
        