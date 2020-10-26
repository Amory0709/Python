# LintCode 582. Wildcard Matching
[link](https://www.lintcode.com/problem/wildcard-matching/description)

*Method*: Memoization

*Time Complexity*: O(nm)

(参考令狐冲的解答：使用了记忆化搜索以后（memoization），时间复杂度是 O(nm)，n和m是两个字符串的长度。因为对于我们要记忆的东西（也就是搜索函数里的参数组合）一共就 O(nm) 种可能性。每种参数组合的可能性往下递归的时候，是 O(1) 的处理时间)

*Space Complexity*: O(nm)

## Analysis
![alt text](https://github.com/Amory0709/Data-Structure-and-Algorithm/blob/master/wildcardMatching.jpeg)

## Code as below:
```python

class Solution1:
# beat 99.1%
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        memo = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        self.dfs(s, p, 0, 0, memo)
        return memo[0][0]
        
    def dfs(self, s, p, i, j, memo):
        #memoization
        if memo[i][j] is not None:
            return
            
        # string reached end
        if i == len(s):
            #pattern not end
            for char in p[j:]:
                if char != '*':
                    memo[i][j] = False
                    return
            memo[i][j] = True
            return
        
        # pattern reached end
        if j == len(p):
            # string also ended
            if i == len(s):
                memo[i][j] = True
                return
            memo[i][j] = False
            return
        
        if p[j] == '?' or s[i] == p[j]:
            self.dfs(s, p, i+1, j+1, memo)
            memo[i][j] = memo[i+1][j+1]
        elif p[j] == '*':
            # match one more char
            self.dfs(s, p, i+1, j, memo)
            self.dfs(s, p, i, j+1, memo)
            memo[i][j] = memo[i][j+1] or memo[i+1][j]
        else:
            memo[i][j] = False
            
class Solution2:
# more clean edition, beat 91%
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        memo = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        return self.dfs(s, p, 0, 0, memo)
        
    def dfs(self, s, p, i, j, memo):
        #memoization
        if memo[i][j] is not None:
            return memo[i][j]
            
        # string reached end
        if i == len(s):
            #pattern not end
            for char in p[j:]:
                if char != '*': 
                    return False
            return True
        
        # pattern reached end, implies string did not end
        if j == len(p):
            return False
        
        if p[j] != '*':
            memo[i][j] =  (p[j] == '?' or s[i] == p[j]) and self.dfs(s, p, i+1, j+1, memo)
        else:
            memo[i][j] = self.dfs(s, p, i+1, j, memo) or self.dfs(s, p, i, j+1, memo)
        
        return memo[i][j]
```
