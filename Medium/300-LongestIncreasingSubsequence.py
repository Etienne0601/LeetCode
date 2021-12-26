class Solution:
    
    def lenOfLISWithMax(self, nums: List[int], maxVal: int) -> int:
        # if there's only one element, return one if it's strictly less than maxVal
        # else, return 0
        if len(nums) == 1:
            return int(nums[0] < maxVal)
        lastInd = len(nums) - 1
        # we have two cases - if we include the last element or if we don't
        # we can only include the last element if it's strictly less than maxVal
        includedMaxLen = -1
        if nums[lastInd] < maxVal:
            includedMaxLen = 1 + self.lenOfLISWithMax(nums[:lastInd], nums[lastInd])
        
        return max(includedMaxLen, self.lenOfLISWithMax(nums[:lastInd], maxVal))
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.lenOfLISWithMax(nums, 10001)
