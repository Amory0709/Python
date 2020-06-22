class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        if n == 1:
            return [0,1,2,3,4,5,6,7,8,9]
            
        ans = []
        for i in range(10**(n-1), 10**n):
            sum, num = 0, i
            while num != 0:
                sum += (num % 10) ** n
                num = num // 10
            # ERROR: compared sum with num, but num is now 0    
            if sum == i:
                ans.append(sum)
        
        return ans
