class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preReq = {i : set() for i in range(numCourses)}

        for a, b in prerequisites:
            preReq[a].add(b)

        cycle = set()
        visited = set()
        order = []
        def dfs(curr):
            if curr in cycle:
                return False

            if curr in visited:
                return True

            cycle.add(curr)
            visited.add(curr)
            for n in preReq[curr]:
                if not dfs(n):
                    return False
            order.append(curr)
            cycle.remove(curr)

            return True

        for start in range(numCourses):
            if not dfs(start):
                return []

        return order

        