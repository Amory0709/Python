class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        m, n = len(source), len(target)

        if not target:
            return 0
        if m < n:
            return -1
    
        t_hash = self.hashStr(target)
        s_hash = None
        
        for i in range(m - n + 1):
            if s_hash is None:
                s_hash = self.hashStr(source[:n])
            else:
                # ERROR: add and remove char not correct
                s_hash = (s_hash - ord(source[i - 1]) * (31 ** (n-1))) %  1000000
                s_hash = (31 * s_hash + ord(source[i + n - 1])) % 1000000
            
            if s_hash == t_hash:
                return i
                
        return -1   
            
    
    def hashStr(self, s):
        ans = 0
        for c in s:
            ans = (ans * 31 + ord(c)) % 1000000
        
        return ans
        
