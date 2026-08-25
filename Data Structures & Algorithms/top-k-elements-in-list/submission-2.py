class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c = collections.Counter(nums)
        
        counts = [[] for _ in range(len(nums) + 1)]

        for n in c.keys():
            counts[c[n]].append(n)

        ret = []

        for i in range(len(counts) - 1, 0, -1):
            for j in counts[i]:
                ret.append(j)
                if len(ret) == k:
                    return ret

        return ret