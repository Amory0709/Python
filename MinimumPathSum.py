class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    Time O(nm)
    Space O(1)
    Link: https://www.lintcode.com/problem/minimum-path-sum/description
    """
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        for row in range(n):
            for col in range(m):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    grid[0][col] += grid[0][col-1]
                elif col == 0:
                    grid[row][0] += grid[row-1][0]
                else:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        
        return grid[n-1][m-1]
