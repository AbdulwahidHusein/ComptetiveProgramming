class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def count_islands(matrix):
            count = 0
            row = len(matrix)
            col = len(matrix[0])
            def is_island(i, j, arr, reffered=False):
                nonlocal count
                if i <0 or j <0 or i>=row or j>= col:
                    return False
                if arr[i][j] == '0':
                    return False
                matrix[i][j] = '0'
                is_island(i-1, j, arr, True)
                is_island(i, j-1, arr, True)
                #is_island(i-1, j-1, arr,False)#exclude diagonals
                is_island(i+1, j, arr, True)
                is_island(i, j+1, arr, True)
                #is_island(i+1, j+1, arr, False)#exclude diagonals
                if not reffered:
                    count += 1
                return True
            for i in range(row):
                for j in range(col):
                    is_island(i, j, matrix)
            return count
        return count_islands(grid)