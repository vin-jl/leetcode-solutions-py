class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxRow = len(grid)
        maxCol = len(grid[0])
        def bfs(row, col):
            if grid[row][col] != 1: return 0
            grid[row][col] = -1
            
            sum = 1
            if row < maxRow-1:
                sum += bfs(row+1, col)
            if row > 0:
                sum += bfs(row-1, col)
            if col < maxCol-1:
                sum += bfs(row, col+1)
            if col > 0:
                sum += bfs(row, col-1)
            return sum

        maximum = 0
        for r in range(maxRow):
            for c in range(maxCol):
                if grid[r][c] == 1:
                    maximum = max(maximum, bfs(r, c)) 
        return maximum
