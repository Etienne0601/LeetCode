class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)
        if length1 == 0 or length2 == 0:
            return 0
        
        dp = [[0 for i in range(length2 + 1)] for j in range(length1 + 1)]
        
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                # what is the longest common subsequence of the
                # first i characters in text1 and the first j
                # characters in text2
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[length1][length2]

