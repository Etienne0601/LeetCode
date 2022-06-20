class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = nums[0]
        currInd = 0
        for i in range(1, len(nums)):
            if nums[i] != curr:
                curr = nums[i]
                currInd += 1
                nums[currInd] = curr
        return currInd + 1

