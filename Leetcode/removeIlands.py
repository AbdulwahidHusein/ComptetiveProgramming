def RemoveIland(Matrix):
    def dfs(r, c):
        row = len(Matrix)-1
        col = len(Matrix[0])-1
    
        if Matrix[r][c]!=1:
            return
        Matrix[r][c]==2# mark borders as 2
        if r>row or r<0 or c>col or c<0:
            return
        if Matrix[r][c-1]==1:
            dfs(r,c-1)
        if Matrix[r-1][c]==1:
            dfs(r-1,c)
        if Matrix[r][c+1]==1:
            dfs(r,c+1)
        if Matrix[r+1][c]==1:
            dfs(r+1,c)
        return
    row = len(Matrix)
    col = len(Matrix[0])
    for i in range(col):
        if Matrix[0][i] == 1:
            dfs(0,i)
        if Matrix[row-1][i]==1:
            dfs(row-1,i)
    for j in range(row):
        if Matrix[j][0]==1:
            dfs(j,0)
        if Matrix[j][col-1] ==1:
            dfs(j, col-1)
    return Matrix

Matrix = [
    [1,  0,  0 ,  1 , 0],
    [1,  1,  1  , 0   ,1],
    [0,  1,  0,    1,   1],
    [1,   1,  0,    1,   0],
    [0,   1,   0,   1,   0]
]
print(RemoveIland(Matrix))