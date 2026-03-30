class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # bucket sort

        n = len(nums)

        buckets = [[] for _ in range(n)]

        counts = Counter(nums)

        for key, value in counts.items():
            buckets[value - 1].append(key)

        out = []
        for i in range(n - 1, -1, -1):
            for j in range(len(buckets[i])):
                out.append(buckets[i][j])
                if len(out) == k:
                    return out

        return out



