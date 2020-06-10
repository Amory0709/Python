class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # Time O(n^2) Space O(n^2)
        if not s:
            return ''
            
        n = len(s) 
        left, right, maxLength =  0, 0, 1
        # isPalindrome = [[False for _ in range(n)] for _ in range(n)]
        # error: difference between the above method and [[False]*n]*n
        isPalindrome = [[False] * n for _ in range(n)]
        
        for i in range(1, n):
            isPalindrome[i][i-1] = True
        for i in range(n):
            isPalindrome[i][i] = True
        
        for step in range(1, n):
            for start in range(n - step):
                end = start+step
                isPalindrome[start][end] = (s[start] == s[end]) and (isPalindrome[start + 1][end - 1])
                if isPalindrome[start][end] and step + 1 > maxLength:
                    left, right, maxLength = start, end, step+1
                    
        return s[left:right+1]
