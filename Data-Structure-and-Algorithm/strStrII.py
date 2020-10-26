class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # Time O(n+m)
        # Space O(1)
        if source is None or target is None: return -1
        #ERROR: corner case not considerate wrote if target == source:return 0
        if target == '': return 0
        
        t_hash = self.hashStr(target)
        n = len(target)
        
        power = 1
        for i in range(n-1):
            power = power * 31 % 100000000
        
        s_hash = 0
        for i in range(len(source)):
            # ERROR2: TEL: calculate by len(target)
            # FIX: now calculate one by one
            if i >= n:
                s_hash = (s_hash - power * ord(source[i-n]))% 100000000
            s_hash = (31 * s_hash + ord(source[i])) % 100000000
            
            if s_hash == t_hash:
                return i - n + 1
                
        return -1
        
    
    def hashStr(self, s):
        ans = 0
        for c in s:
            ans = (31 * ans + ord(c)) % 100000000
            
        return ans 
