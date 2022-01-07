class Solution:
    def maxArea(self, height: List[int]) -> int:
        # the brute force solution
        maxWater = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                water = (j - i) * min(height[i], height[j])
                maxWater = max(maxWater, water)
                
        return maxWater
