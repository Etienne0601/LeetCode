# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # initialize queue which holds tuples to keep track
        # of the level-order (heap) index of nodes
        queue = deque([(root, 0)])
        
        maxWidth = 1
        
        while len(queue) != 0:
            levelNodeLength = len(queue)
            # iterate through the current level and store the first index
            # of this level to determine the width and the last index
            firstInd = queue[0][1]
            lastInd = 0
            for i in range(levelNodeLength):
                # pop these nodes on this level off the stack and add their children
                currNode = queue.popleft()
                lastInd = currNode[1]
                if currNode[0].left:
                    queue.append((currNode[0].left, (2 * lastInd + 1)))
                if currNode[0].right:
                    queue.append((currNode[0].right, (2 * lastInd + 2)))
            # then check if we've found a larger width
            maxWidth = max(maxWidth, lastInd - firstInd + 1)
            
        return maxWidth
