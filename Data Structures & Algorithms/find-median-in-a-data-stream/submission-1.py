class MedianFinder:

    # partition the stream into two halfs
    # bottom half is a max heap 
    # top half is a min heap
    # when a new num is added, add it to the respective heap
    # rebalance to keep them even 
    # they may be off by at most one at any given time, so the o index
    # on the greater sized heap is the median
    # if they are even take the average of the two [0]
    def __init__(self):
        # left , negative!
        self.maxHeap = []

        # right
        self.minHeap = []
        
    def addNum(self, num: int) -> None:
        if not self.maxHeap and not self.minHeap:
            self.maxHeap.append(-num)

        elif num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)

        elif self.minHeap and num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)

        else:
            heapq.heappush(self.maxHeap, -num)

        if math.fabs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                move = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, move)
            else:
                move = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -move)

                

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        return self.minHeap[0]
        
        