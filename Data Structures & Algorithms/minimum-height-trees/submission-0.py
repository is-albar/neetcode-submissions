class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            hgt = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                hgt = max(hgt, 1 + dfs(nei, node))
            return hgt

        minHgt = n
        res = []
        for i in range(n):
            curHgt = dfs(i, -1)
            if curHgt == minHgt:
                res.append(i)
            elif curHgt < minHgt:
                res = [i]
                minHgt = curHgt

        return res