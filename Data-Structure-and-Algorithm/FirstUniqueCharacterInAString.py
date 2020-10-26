class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        ans = []
        twice = set()
        for c in str:
            if c not in ans:
                if c in twice:
                    continue
                ans.append(c)
            else:
                twice.add(c)
                ans.remove(c)
        
                
        return ans[0]
