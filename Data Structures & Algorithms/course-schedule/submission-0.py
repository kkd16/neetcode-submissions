class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mp = {i:[] for i in range(numCourses)}

        for p in prerequisites:
            mp[p[0]].append(p[1])

        path = set()
        def dfs(c):
            if c in path:
                return False

            if mp[c] == []:
                return True

            path.add(c)
            for p in mp[c]:
                if not dfs(p): return False
            mp[c] = []
            path.remove(c)

            return True

        for c in range(numCourses):
            if not dfs(c): return False
        
        return True



        

        

        

        