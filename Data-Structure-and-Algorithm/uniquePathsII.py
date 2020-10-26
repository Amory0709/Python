class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    Time  complexity: O(nm)
    Space complexity: O(nm)
    But we can use O(1) space
    link: lintcode.com/problem/unique-paths-ii/description
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        pathNums = [[0 for _ in range(m)] for _ in range(n)]
        
        #initialization
        if obstacleGrid[0][0] == 0:
            pathNums[0][0] = 1 
        
        for row in range(1, n):
            if obstacleGrid[row][0]:
                continue
            pathNums[row][0] = pathNums[row - 1][0]
        
        for col in range(1, m):
            if obstacleGrid[0][col]:
                continue
            pathNums[0][col] = pathNums[0][col - 1]
            #error1: when copy code from above, did not change it
        
        for row in range(1, n):
            for col in range(1, m):
                # error2: did not consider when this is a obstacle
                if obstacleGrid[row][col]:
                    continue
                pathNums[row][col] = pathNums[row-1][col] * (1 - obstacleGrid[row-1][col]) + \
                                    pathNums[row][col-1] * (1 - obstacleGrid[row][col-1])
        
        return pathNums[n-1][m-1]
