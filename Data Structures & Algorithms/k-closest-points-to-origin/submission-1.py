class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for p in points:
            x = p[0]
            y = p[1]
            d = x ** 2 + y ** 2
            heapq.heappush(heap, (-1 * d, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        ret = []
        for p in heap:
            ret.append([p[1], p[2]])

        return ret