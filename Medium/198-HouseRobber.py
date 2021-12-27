class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        # dp[i] represents the max amount you can rob if you only
        # have the first i+1 houses available to you
        dp = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            # we have two cases - if we include house i or not
            dp.append(max(dp[i - 1], nums[i] + dp[i - 2]))
        
        return dp[-1]
