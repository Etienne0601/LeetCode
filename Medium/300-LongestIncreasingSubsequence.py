class Solution:
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] represent the LIS starting at index i in nums
        # dp[i] is always going to be at minimum 1, which is just the one element
        dp = [1] * len(nums)
        # fill dp in backwards order
        for i in range(len(nums) - 1, -1, -1):
            # potentially all the indices that come after i could be the next element
            for j in range(i + 1, len(nums)):
                # the element at j could come after the element at i
                # in the LIS only if nums[i] < nums[j]
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        # then we just want to return the max value in dp, since
        # the LIS can start at any index in nums
        return max(dp)
