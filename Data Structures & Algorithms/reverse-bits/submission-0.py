class Solution:
    def reverseBits(self, n: int) -> int:
        # after reversal bit i is now 31 - i
        res = 0
        for i in range(32):
            b = (n >> i) & 1
            res |= (b << (31 - i))

        return res