class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i : set() for i in range(numCourses)}

        for a, b in prerequisites:
            preReq[b].add(a)

        def dfs(curr, seen):
            if curr in seen:
                return False

            seen.add(curr)
            for n in preReq[curr]:
                if not dfs(n, seen):
                    return False
            seen.remove(curr)
            preReq[curr] = []

            return True

        for start in range(numCourses):
            seen = set()
            if not dfs(start, seen):
                return False

        return True
            

        