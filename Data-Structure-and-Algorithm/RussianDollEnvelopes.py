import bisect

class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    Time O(nlogn)
    Space O(n)
    link: lintcode.com/problem/russian-doll-envelopes/description
    learned a lot from this
    """
    def maxEnvelopes(self, envelopes):
        # sort by width, so we can focus on height comparation
        # reverse height for the same width incase wrong case included
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        result = []
        # if use dp array all start from 1, Time Limit Exceeded
        for envelope in envelopes:
            height = envelope[1]
            if len(result) < 1 or height > result[-1]:
                result.append(height)
            else:
                index = bisect.bisect_left(result, height)
                result[index] = height
                
        
        return len(result)
