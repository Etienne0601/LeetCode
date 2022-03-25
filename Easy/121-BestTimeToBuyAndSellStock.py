class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 0
        maxProf = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[right]:
                right = i
                maxProf = max(maxProf, prices[right] - prices[left])
            elif prices[i] < prices[left]:
                left = i
                right = i
        
        return maxProf
