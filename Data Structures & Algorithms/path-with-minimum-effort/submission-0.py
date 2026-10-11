class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, limit, visited):
            if r == ROWS - 1 and c == COLS - 1:
                return True

            visited.add((r, c))
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR < 0 or newC < 0 or
                    newR >= ROWS or newC >= COLS or
                    (newR, newC) in visited or
                    abs(heights[newR][newC] - heights[r][c]) > limit):
                    continue

                if dfs(newR, newC, limit, visited):
                    return True
            return False

        l, r = 0, 1000000
        res = r

        while l <= r:
            mid = (l + r) // 2
            if dfs(0, 0, mid, set()):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res