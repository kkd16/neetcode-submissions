class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i : set() for i in range(numCourses)}

        for a, b in prerequisites:
            preReq[b].add(a)

        seen = set()
        def dfs(curr):
            if curr in seen:
                return False

            seen.add(curr)
            for n in preReq[curr]:
                if not dfs(n):
                    return False
            seen.remove(curr)
            preReq[curr] = []

            return True

        for start in range(numCourses):
            if not dfs(start):
                return False

        return True
            

        