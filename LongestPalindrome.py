class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # Time complexity: O(n)
        # Space complexity: O(n)
        if not s:
            return 0
            
        occurred = set() 
        ans = 0
        
        for c in s:
            if c not in occurred:
                occurred.add(c)
            else:
                occurred.remove(c)
                ans += 2
                
        if occurred:
            ans += 1
        
        return ans
