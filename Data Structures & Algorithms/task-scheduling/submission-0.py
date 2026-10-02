class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # create priority queue (max heap)
        # put max in schedule, then remove from heap
        # put max (taken from heap) into a min heap, keyed on 
        # time it can go back into the system

        # create a time variable
        # iterate thru schedules
        # check if we need to put anything back into the max heap
        # on each schedule go through steps above

        counts = collections.Counter(tasks)

        remain = []
        for j, c in counts.items():
            remain.append([-1 * c, j])

        heapq.heapify(remain)

        time = 0

        restock = []

        while len(remain) > 0 or len(restock) > 0:

            while len(restock) > 0 and restock[0][0] == time:
                heapq.heappush(remain, restock[0][1])
                heapq.heappop(restock)
            
            if len(remain) > 0:
                r = remain[0]
                heapq.heappop(remain)

                r[0] += 1

                if r[0] < 0:
                    heapq.heappush(restock, [time + n + 1, r])
            
            time += 1

        return time       