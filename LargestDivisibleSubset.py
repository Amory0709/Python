"""
A very tricky problem.
I thought I can use memoization
And I ignore the calculation order so I forgot to sort.
"""
class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        #error1: ignored the order of the nums
        nums.sort()
        
        #dp[i] presents record how many divisible numbers so far
        dp = [1] * len(nums)
        #prev[i] record the index of the previous divisible number
        prev = [-1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                #update dp only when the dp can be higher
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[i] + 1
                    prev[i] = j
        
        #organize the result
        path = []
        longest, last = max(dp), dp.index(max(dp))
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        
        return path[::-1] #reverse the result
