class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

        dfs(0, -1)

        return len(visited) == n
        