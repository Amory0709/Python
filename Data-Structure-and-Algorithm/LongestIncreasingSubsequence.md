# LintCode 582. Longest Increasing Subsequence

[link](lintcode.com/problem/longest-increasing-subsequence/description)

*Method*: 倒推法（对于接龙型DP）

*Time Complexity*: O(n<sup>2</sup>)  
*Space Complexity*: O(n)

## Analysis
![alt text](https://github.com/Amory0709/Data-Structure-and-Algorithm/blob/master/LongestIncreasingSubsequence.jpeg)

## Code as below:
```python
class Solution1:
# to print the best solution
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

class Solution2:
# don't need to print the best solution
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums)
        for curr, val in enumerate(nums):
            for prev in range(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        return max(dp)

class Solution3:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    Time O(nlogn)
    """
    def longestIncreasingSubsequence(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        
        n = len(nums)
        f = [0] * n         # f[i] 表示以 nums[i] 结尾的 LIS 长度
        g = [0] * (n + 1)   # g[i] 表示长度为 i 的 LIS 结尾最小是谁
        
        lis = f[0] = 1
        g[1] = nums[0]
        
        for i in range(1, n):
            # 二分查找 nums[i] 可以放到 g 数组的哪个数后面
            # 即查找 g 数组中第一个不小于 nums[i] 的位置
            
            if nums[i] > g[lis]: # 特判, nums[i] 比全部的都大
                f[i] = lis
                lis += 1
                g[lis] = nums[i]
            else:
                l, r =  1, lis 
                while l != r:
                    mid = (l + r) // 2 
                    if g[mid] < nums[i]:
                        l = mid + 1 
                    else:
                        r = mid
                f[i] = l
                g[l] = min(g[l], nums[i])
            
        return lis
```
