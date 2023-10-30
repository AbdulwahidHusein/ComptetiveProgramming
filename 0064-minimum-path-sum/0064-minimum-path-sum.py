class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Create a dynamic programming array with dimensions similar to the grid
        # Initialize each cell with infinity as a placeholder
        dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        # Set the minimum path sum for the top left corner as the value in the grid
        dp[0][0] = grid[0][0]
        
        # Calculate the minimum path sum for the leftmost column
        # The only possible movement is to go down
        # The minimum path sum at each cell is the sum of the previous cell's path sum and the value in the current cell
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Calculate the minimum path sum for the top row
        # The only possible movement is to go right
        # The minimum path sum at each cell is the sum of the previous cell's path sum and the value in the current cell
        for i in range(1, len(grid[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]  

        # Calculate the minimum path sum for the remaining cells
        # For each cell, the minimum path sum is the sum of the current cell's value and the minimum of the path sums from the cell above and the cell to the left
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        # Return the minimum path sum for the bottom right corner of the grid
        return dp[-1][-1]