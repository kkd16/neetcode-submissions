class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            n = len(s)
            ret = ret + str(n) + "#" + s
        
        return ret


    def decode(self, s: str) -> List[str]:
        ret = []

        l = len(s)

        i = 0

        while i < l:
            n = ""
            while s[i] != '#':
                n = n + s[i]
                i += 1

            i += 1
            
            n = int(n)

            st = ""
            for j in range(n):
                st = st + s[i]
                i += 1

            
            ret.append(st)

                
        return ret
