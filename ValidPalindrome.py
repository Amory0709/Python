class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # Time O(n) Space O(1)
        left, right =  0, len(s)-1 
        
        while left < right:
            while left < right and not self.validString(s[left]):
                left += 1
            while left < right and not self.validString(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1  
    
        return True
        
    
    def validString(self, s):
        if s.isalpha() or s.isdigit():#error: wrote isalpha() as isalpha
            return True
        return False
