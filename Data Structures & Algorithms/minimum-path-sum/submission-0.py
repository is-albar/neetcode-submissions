class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if r == m or c == n:
                return float('inf')
            if dp[r][c] != -1:
                return dp[r][c]

            dp[r][c] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return dp[r][c]

        return dfs(0, 0)