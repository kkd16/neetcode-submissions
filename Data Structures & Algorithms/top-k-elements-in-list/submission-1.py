class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # get counts of each
        counts = collections.Counter(nums)
        

        # map each to bucket
        freqs = [[] for _ in range(len(nums) + 1)]
        for n, c in counts.items():
            freqs[c].append(n)

        # get k most frequent
        ret = []
        for i in range(len(nums), 0, -1):
            for n in freqs[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret
        