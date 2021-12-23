class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # if amount is zero then you don't need any coins
        if amount == 0:
            return 0
        
        # initialize dynamic programming array
        dp = [10001] * (amount + 1)
        
        dp[0] = 0 # zero coins to add up to zero
        
        # populate the dp array
        for i in range(1, amount + 1):
            # iterate through the different coin denominations and take the minimum
            for coin in coins:
                # it's only possible to use this coin if it's less than or equal to i,
                # since i is the current amount
                if coin <= i:
                    # update dp[i] if we find a way to use fewer coins
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        if dp[amount] == 10001:
            return -1
        
        return dp[amount]
