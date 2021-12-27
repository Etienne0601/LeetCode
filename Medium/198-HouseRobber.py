class Solution:
    
    def robRecursion(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        included = nums[0] + self.robRecursion(nums[2:])
        notInclu = self.robRecursion(nums[1:])
        return max(included, notInclu)
    
    def rob(self, nums: List[int]) -> int:
        return self.robRecursion(nums)
