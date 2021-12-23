class Solution:
    
    def minNumCoins(coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        numCoins = []
        
        for coinAmt in coins:
            if coinAmt <= amount:
                subProbMinCoins = Solution.minNumCoins(coins, amount - coinAmt)
                if subProbMinCoins > -1:
                    numCoins.append(subProbMinCoins + 1)
        
        if len(numCoins) == 0:
            return -1
        
        return min(numCoins)
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        return Solution.minNumCoins(coins, amount)
