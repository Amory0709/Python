# LintCode 582. Longest Increasing Subsequence

[link](lintcode.com/problem/longest-increasing-subsequence/description)

*Method*: 倒推法（对于接龙型DP）

*Time Complexity*: O(n<sup>2</sup>)  
*Space Complexity*: O(n)

## Analysis
![alt text](https://github.com/Amory0709/Data-Structure-and-Algorithm/blob/master/%20LongestIncreasingSubsequence.jpeg)

## Code as below:
```python
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
            
        n = len(nums)
        count = [1] * n
        prev = [-1] * n
        
        for end in range(n):
            for i in range(end):
                if nums[end] > nums[i] and count[i] + 1 > count[end]:
                    count[end] = count[i] + 1
                    prev[end] = i
        
        return max(count)
```
