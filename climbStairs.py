class Solution:
    """
    @param n: An integer
    @return: An integer
    Time O(n)
    Space O(n)
    link: lintcode.com/problem/climbing-stairs/description
    """
    def climbStairs(self, n):
        #error1: does not consider n == 0
        if not n:
            return 0
            
        stepCount = [0 for _ in range(n+1)]
        stepCount[0] = 1
        
        for i in range(1, n + 1):
            stepCount[i] = stepCount[i-1] * (i - 1 >= 0) + stepCount[i - 2] * (i - 2 >= 0)
        
        return stepCount[n]
        
        
# clever and flexible rolling array
class Solution2:
    """
    Time O(n)
    Space O(1)
    """
    def climbStairs(self, n):
        if not n: return 0 
        
        down, this = 0, 1 
        for _ in range(n):
            down, this = this, down + this
        return this
