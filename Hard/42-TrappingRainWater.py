class Solution:
    def trap(self, height: List[int]) -> int:
        # if len(height) is 1, then we can't trap water
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
                leftInd += 1
                # if leftPeak > height[leftInd] then add the new water
                if leftPeak > height[leftInd]:
                    water += leftPeak - height[leftInd]
                else:
                    leftPeak = height[leftInd]
            else:
                rightInd -= 1
                # if rightPeak > height[rightInd] then add the new water
                if rightPeak > height[rightInd]:
                    water += rightPeak - height[rightInd]
                else:
                    rightPeak = height[rightInd]

        return water
