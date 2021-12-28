class Solution:
    
    def robOne(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # dp[i] represents the max amount you can rob if you only
        # have the first i+1 houses available to you
        dp = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            # we have two cases - if we include house i or not
            dp.append(max(dp[i - 1], nums[i] + dp[i - 2]))
        
        return dp[-1]
    
    
    def rob(self, nums: List[int]) -> int:
        # we examine two cases, the first one is where the house at nums[0]
        # is robbed, and the second is where the house at nums[0] is not robbed
        # if the house at nums[0] is robbed, then we can't include nums[1] or nums[-1]
        # if the house at nums[0] is not robbed, then nums[1] and/or nums[-1] could
        # potentially be included in the optimal solution in this case
        n = len(nums) - 1
        return max(self.robOne(nums[1:]), nums[0] + self.robOne(nums[2:n]))
