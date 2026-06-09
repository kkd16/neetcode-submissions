class MinStack:

    def __init__(self):
        self.s = []
        self.heap = []

    def _clean(self):
        while self.heap[0] not in self.s:
            heapq.heappop(self.heap)

        
    def push(self, val: int) -> None:
        self.s.append(val)
        heapq.heappush(self.heap, val)

    def pop(self) -> None:
        return self.s.pop()
        
    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        self._clean()
        return self.heap[0]
        
