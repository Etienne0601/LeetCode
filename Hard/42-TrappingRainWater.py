class Solution:
    def trap(self, height: List[int]) -> int:
        # len(height) is 1, then we can't trap water
        if len(height) == 1:
            return 0
        
        water = 0
        leftInd = 0
        rightInd = len(height) - 1
        leftPeak = height[0]
        rightPeak = height[-1]
        
        while leftInd < rightInd:
            # shift the smaller peak index towards the center
            if leftPeak <= rightPeak:
                # add the water that can be held at the (leftInd + 1) index
                leftInd += 1
                water += max(0, leftPeak - height[leftInd])
                leftPeak = max(leftPeak, height[leftInd])
            else:
                # add the water that can be held at the (rightInd - 1) index
                rightInd -= 1
                water += max(0, rightPeak - height[rightInd])
                rightPeak = max(rightPeak, height[rightInd])
                
        return water
