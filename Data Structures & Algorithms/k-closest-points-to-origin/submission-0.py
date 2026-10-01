class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        closest = []
        for p in points:
            x = p[0]
            y = p[1]
            d = -1 * math.sqrt(x ** 2 + y ** 2)

            heapq.heappush(closest, (d, x, y))
            if len(closest) > k:
                heapq.heappop(closest)

        res = []
        for c in closest:
            res.append([c[1], c[2]])

        return res

        