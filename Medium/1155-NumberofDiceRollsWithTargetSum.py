class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dp array
        dp = [[0 for i in range(target)] for j in range(n)]
        
        # initialize with the first die
        for i in range(min(k, target)):
            dp[0][i] = 1
        
        # now do the rest of the dice
        for i in range(2, n + 1):
            for j in range(2, target + 1):
                # dp[i][j] = dp[i-1][j-1] + d[i-1][j-2] + ... + dp[i-1][j-k]
                for val in range(1, k + 1):
                    if j > val:
                        dp[i - 1][j - 1] += dp[i - 2][j - val - 1]
                        dp[i - 1][j - 1] %= 1000000007
                        
        return dp[n - 1][target - 1]
