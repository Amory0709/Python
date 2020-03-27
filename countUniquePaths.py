class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        countPath = [[0 for _ in range(n)] for _ in range(m)]
        # initiate value
        countPath[0][0] = 1
        
        # for i in range(n):
        #     countPath[0][i] = 1
        # for i in range(m):
        #     countPath[i][0] = 1 #error1 wrote i as m
            
        # # m =  1, [1][1], [1][2] m = 2...
        # for row in range(1, m):
        #     for col in range(1, n):
        #         countPath[row][col] = countPath[row-1][col] + countPath[row][col-1]
        
        # make initiation in the loop
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    countPath[row][col] = 1
                else:
                    countPath[row][col] = countPath[row-1][col] + countPath[row][col-1]
        
        return countPath[m-1][n-1] # wrote m, n instead of m-1, n-1
