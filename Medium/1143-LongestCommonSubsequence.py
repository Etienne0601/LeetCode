class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        
        if text1[0] == text2[0]:
            return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])

        branch1 = self.longestCommonSubsequence(text1[1:], text2)
        branch2 = self.longestCommonSubsequence(text1, text2[1:])
        
        return max(branch1, branch2)
