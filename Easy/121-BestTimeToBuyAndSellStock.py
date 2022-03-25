class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProf = 0
        
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                maxProf = max(maxProf, prices[j] - prices[i])
        
        return maxProf
