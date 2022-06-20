class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums):
                if nums[j] == nums[i]:
                    nums.pop(j)
                else:
                    j += 1
        return len(nums)

