class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        if len(s) < len(t):
            return ""
        
        s_count = collections.Counter()
        t_count = collections.Counter(t)

        need = len(t_count)
        have = 0
        
        best_start = 0
        best_len = float('inf')

        l = 0
        for r, ch in enumerate(s):
            s_count[ch] += 1

            if ch in t_count and s_count[ch] == t_count[ch]:
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
        