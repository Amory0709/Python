#lintcode 109: https://www.lintcode.com/problem/triangle/description
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        if not triangle:
            return None
        
        n = len(triangle)
        min_sum = [0 for i in range(n+1)]
        
        for row in range(n, 0, -1):
            # will not contain 0, just loop to 1
            for col in range(row):
                min_sum[col] = min(min_sum[col],min_sum[col+1]) + triangle[row-1][col]
        
        return min_sum[0]
