class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dp array
        dp = [0 for i in range(target)]
        
        # initialize with the first die
        for i in range(min(k, target)):
            dp[i] = 1
        
        # now do the rest of the dice
        for i in range(n - 1):
            for j in range(target, 0, -1):
                # count the number of possibilites for this number of
                # dice and target j
                dp[j - 1] = 0
                for val in range(1, k + 1):
                    if j > val:
                        dp[j - 1] += dp[j - val - 1]
                        
        return dp[-1] % 1000000007
