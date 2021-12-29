class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # the result list containing all possible permutations of nums
        result = []
        
        # base case
        if len(nums) == 1:
            result.append([nums[0]])
            return result
        
        for i in range(len(nums)):
            # remove nums[i] and make the recursive call
            subPermutations = self.permute(nums[:i] + nums[i+1:])
            # then append nums[i] to each returned permutation
            for subPermutation in subPermutations:
                subPermutation.append(nums[i])
            # finally add them to the result
            result.extend(subPermutations)
        
        return result
