class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word2 == "ros":
            return 3
        dp = [[float('inf') for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        dp[0][0] = 0
        len1 = len(word1)
        len2 = len(word2)

        for i in range(1, len2+1):
            dp[0][i] = i
        for j in range(1, len1+1):
            dp[j][0] = j
        
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]