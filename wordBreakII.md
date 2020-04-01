# LintCode 582. Word Break II
[link](https://www.lintcode.com/problem/word-break-ii/description)

*Method*: Memoization

*Time Complexity*: O(2<sup>n</sup>)  
*Space Complexity*: O(n)

## Analysis
![alt text](https://github.com/Amory0709/Data-Structure-and-Algorithm/blob/master/wordBreakii.jpeg)

## Code as below:
```python
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        
        return self.dfs(s, wordDict, {})
    
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if len(s) == 0:
            return []
        
        partitions = []
        
        for i in range(1, len(s)):
            front = s[:i]
            if front not in wordDict:
                continue
            
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for sub_partition in sub_partitions:
                partitions.append(front + ' ' + sub_partition)
        
        if s in wordDict:
            partitions.append(s)
        
        memo[s] = partitions
        
        return memo[s]
```
