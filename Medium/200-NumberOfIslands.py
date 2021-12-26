class Solution:
    
    # index 0 in the tuple represents which row,
    # index 1 in the tuple represents which column
    def dfs(self, curr: Tuple[int], grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        currRow = curr[0]
        currCol = curr[1]
        
        # since curr is a 1, then set it to 0 and recurse on the neighbors
        grid[currRow][currCol] = '0'
        # recurse up if in bounds
        if currRow >= 1 and grid[currRow - 1][currCol] == '1':
            self.dfs(tuple((currRow - 1, currCol)), grid)
        # recurse left if in bounds
        if currCol >= 1 and grid[currRow][currCol - 1] == '1':
            self.dfs(tuple((currRow, currCol - 1)), grid)
        # recurse down if in bounds
        if currRow <= m - 2 and grid[currRow + 1][currCol] == '1':
            self.dfs(tuple((currRow + 1, currCol)), grid)
        # recurse right if in bounds
        if currCol <= n - 2 and grid[currRow][currCol + 1] == '1':
            self.dfs(tuple((currRow, currCol + 1)), grid)
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        # technically n can be zero, so we check for that
        if n == 0:
            return 0
        
        # basically you have to keep calling dfs on each 1 over and over until
        # there are no more 1's in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(tuple((i, j)), grid)
                    
        return count
