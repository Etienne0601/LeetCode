class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # base cases
        if n == 0:
            if target == 0:
                return 1
            else:
                return 0
        
        # recursive case
        numWays = 0
        for i in range(1, k + 1):
            numWays += self.numRollsToTarget(n - 1, k, target - i)
        
        return numWays
