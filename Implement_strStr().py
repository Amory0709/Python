class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # hash function
        # Time Complexity: O(nm)
        # Space Complexity: O(1)
        if source == target: return 0
        if source is None or target is None: return -1
 
        m = len(source)
        n = len(target)
        target_code = self.hashFunc(target)
        
        for i in range(m-n+1):
            if self.hashFunc(source[i:i+n]) == target_code:
                return i
                
        return -1
        
    def hashFunc(self, s):
        ans = 0
        for c in s:
            # wrong ans = 31 * (ans + ord) return ans//1000000
            # ans = (ans * 31 + ord(c)) % 1000000
            ans = (ans + 17 * ord(c)) % 1000000
            
        return ans
