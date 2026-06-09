class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # start by building intitial k window
        # have a MAX heap which the top is the current max value in the window
        # max heap should store its index where the value was from
        # max heap is -1 * val (heapq is min heap)
        # clean the heap by while top value is invalid (index out of window), pop it

        h = []

        for i in range(k):
            heapq.heappush(h, (-1 * nums[i], i))

        res = []
        
        res.append(-1 * h[0][0])

        for r in range(k, len(nums)):
            heapq.heappush(h, (-1 * nums[r], r))
            while h[0][1] <= (r - k):
                heapq.heappop(h)
            
            res.append(-1 * h[0][0])

        return res



        