class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Build max heap of tasks
        # take highest off
        # put into deque wiht some form of start time
        # iterate a time value each tick

        time = 0

        count = collections.Counter(tasks)
        
        maxHeap = [ -c for c in count.values()]

        heapq.heapify(maxHeap)
        q = collections.deque()

        while maxHeap or q:
            time += 1
            while q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap)
                if c != 0:
                    q.append((c, time + n + 1))

        return time