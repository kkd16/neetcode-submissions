class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for s in stones:
            heapq.heappush(heap, -1 * s)

        while len(heap) > 1:
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)


            if x == y:
                pass
            elif x < y:
                y = y - x
                heapq.heappush(heap, -1 * y)

        if len(heap) > 0:
            return -1 * heap[0]
        else:
            return 0
        