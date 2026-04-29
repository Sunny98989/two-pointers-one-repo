class Solution:
    def maximumScore(self, grid):
        n = len(grid)

        preSum = [[0] * (n + 1) for _ in range(2)]
        for i in range(n):
            preSum[0][i + 1] = preSum[0][i] + grid[i][0]

        dp = [[[0] * 2 for _ in range(n + 1)] for _ in range(2)]

        prev, curr = 0, 1

        for col in range(n - 1):

            for i in range(n):
                preSum[curr][i + 1] = preSum[curr][i] + grid[i][col + 1]

            preMax = dp[prev][0][1]

            for k in range(1, n + 1):
                best = max(
                    dp[prev][k][0],
                    preMax + preSum[prev][k]
                )

                dp[curr][k][0] = best
                dp[curr][k][1] = best

                preMax = max(
                    preMax,
                    dp[prev][k][1] - preSum[prev][k]
                )

            sufMax = dp[prev][n][0] + preSum[curr][n]

            for k in range(n - 1, 0, -1):
                dp[curr][k][0] = max(
                    dp[curr][k][0],
                    sufMax - preSum[curr][k]
                )

                sufMax = max(
                    sufMax,
                    dp[prev][k][0] + preSum[curr][k]
                )

            dp[curr][0][0] = sufMax
            dp[curr][0][1] = max(
                dp[prev][0][0],
                dp[prev][n][0]
            )

            prev, curr = curr, prev

        ans = 0
        for k in range(n + 1):
            ans = max(
                ans,
                dp[prev][k][0],
                dp[prev][k][1]
            )

        return ans
