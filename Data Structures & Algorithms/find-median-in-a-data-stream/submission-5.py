class MedianFinder:

    def __init__(self):
        # left , negative!
        self.maxHeap = []

        # right
        self.minHeap = []
        
    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            move = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, move)
        
        elif len(self.minHeap) > len(self.maxHeap):
            move = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -move)    
                

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        