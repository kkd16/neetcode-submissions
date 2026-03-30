class Solution:

    def encode(self, strs: List[str]) -> str:

        out = ""

        for s in strs:
            n = len(s)

            l = f"{n:03d}"

            out = out + l + s

        print(out)
        
        return out



    def decode(self, s: str) -> List[str]:
        idx = 0
        out = []

        while idx < len(s):
            n = int(s[idx:idx+3])
            idx += 3
            out.append(s[idx:idx+n])
            idx += n

        return out

