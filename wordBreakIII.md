# LintCode 191. Maximun Product Subarray
[link](https://www.lintcode.com/problem/word-break-iii/description)
*Method*: DP

*Time Complexity*: O(n<sup>2</sup>)  

(动态规划的时间复杂度 = 状态数 * 状态转移代价)

(Time Complexity of DP = number of conditions * cost of condition transfer)

*Space Complexity*: O(n)

## Analysis
![alt text](https://github.com/Amory0709/Data-Structure-and-Algorithm/blob/master/wordBreak3.jpeg)

## Code as below:
```python
class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        if not dict:
            return 0
            
        lower_dict = self.lowerDict(dict)
        
        n = len(s)
        path = [0 for _ in range(n+1)]
        # initial status: pointer at the front of the 1st letter and path = 1
        path[0] = 1
        
        for end in range(1,n+1):
            for div in range(end):
                if s[div:end].lower() not in lower_dict:
                    continue
                # use this structure then will beat around 90% submissions
                # use if in -> path+=path will only beat 15%
                path[end] += path[div]
                
        return path[n]
    
    
    
    def lowerDict(self, dict):
        result = set()
        for word in dict:
            result.add(word.lower())
        
        return result
```
