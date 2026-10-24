class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        memo = {}

        def dfs(i, sign):
            if i == n - 1:
                return 1
            if (i, sign) in memo:
                return memo[(i, sign)]

            res = 1
            if ((sign and arr[i] > arr[i + 1]) or
                (not sign and arr[i] < arr[i + 1])
            ):
                res = 1 + dfs(i + 1, not sign)

            memo[(i, sign)] = res
            return res

        max_len = 1
        for i in range(n):
            max_len = max(max_len, dfs(i, True), dfs(i, False))

        return max_len