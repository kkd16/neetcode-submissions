class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((v, t))

        visited = set()
        minHeap = [(0, k)]
        t = 0

        while minHeap:
            w1, u = heapq.heappop(minHeap)
            if u in visited:
                continue

            visited.add(u)
            t = max(t, w1)

            for v, w2 in edges[u]:
                if v not in visited:
                    heapq.heappush(minHeap, (w1 + w2, v))

        return t if len(visited) == n else -1



        
            


        