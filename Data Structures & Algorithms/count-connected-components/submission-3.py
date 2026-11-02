class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            if visited[node]:
                return

            visited[node] = True

            for nei in adj[node]:
                dfs(nei)
        
        res = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                res += 1

        return res
        
