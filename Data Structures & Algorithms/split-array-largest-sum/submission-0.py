class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float("inf")] * (n + 1)
        dp[n] = 0

        for m in range(1, k + 1):
            nextDp = [float("inf")] * (n + 1)
            for i in range(n - 1, -1, -1):
                curSum = 0
                for j in range(i, n - m + 1):
                    curSum += nums[j]
                    nextDp[i] = min(nextDp[i], max(curSum, dp[j + 1]))
            dp = nextDp

        return dp[0]