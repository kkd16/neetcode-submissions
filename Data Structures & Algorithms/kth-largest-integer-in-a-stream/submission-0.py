class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self._heap = list(nums)
        heapq.heapify(self._heap)
        self._k = k

        while len(self._heap) > k:
            heapq.heappop(self._heap)
        

    def add(self, val: int) -> int:

        heapq.heappush(self._heap, val)
        if len(self._heap) > self._k:
            heapq.heappop(self._heap)
    

        return self._heap[0]
        
