class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        nums.sort(reverse=True)
        target = total // k
        n = len(nums)
        dp = [None] * (1 << n)

        def backtrack(i, k, subsetSum, mask):
            if dp[mask] != None:
                return dp[mask]
            if k == 0:
                dp[mask] = True
                return True
            if subsetSum == target:
                dp[mask] = backtrack(0, k - 1, 0, mask)
                return dp[mask]

            for j in range(i, n):
                if (mask & (1 << j)) == 0 or subsetSum + nums[j] > target:
                    continue
                if backtrack(j + 1, k, subsetSum + nums[j], mask ^ (1 << j)):
                    dp[mask] = True
                    return True
                if subsetSum == 0:
                    dp[mask] = False
                    return dp[mask]
            dp[mask] = False
            return False

        return backtrack(0, k, 0, (1 << n) - 1)