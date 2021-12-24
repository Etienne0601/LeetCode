class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # hashmap stores the previous values we've seen and their indices
        # the keys are the numbers and the values are their indices
        # we initialize it with the number at index 0
        hashmap = {nums[0] : 0}
        
        # this will contain the two indices that give us the solution
        indices = []
        
        for i in range(1, len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                # we've found the solution, so append the two indices and return it
                indices.append(hashmap[complement])
                indices.append(i)
                return indices
            # we haven't yet found a solution with indices i and j<i,
            # so add nums[i] to the hashmap
            hashmap[nums[i]] = i
                
        return None
