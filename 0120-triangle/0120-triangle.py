class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf') for j in range(i)] for i in range(1, len(triangle)+1)]

        dp[0][0] = triangle[0][0]
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][-1] = dp[i-1][-1]+ triangle[i][-1]
        for i in range(1, len(dp)):
            for j in range(1, i):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
        
        return min(dp[-1])