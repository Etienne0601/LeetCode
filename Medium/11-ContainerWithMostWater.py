class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left and right indices
        left = 0
        right = len(height) - 1
        
        maxWater = 0
        while left < right:
            if height[left] < height[right]:
                maxWater = max(maxWater, (right - left) * height[left])
                left += 1
            else:
                maxWater = max(maxWater, (right - left) * height[right])
                right -= 1
        
        return maxWater
