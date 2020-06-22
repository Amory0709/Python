class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict): # Write your code here
        que = [s]
        hash = set([s])
        minLen = len(s)

        while que:
            s = que.pop(0)
            for sub in dict:
                found = s.find(sub)
                while found != -1:
                    new_s = s[:found] + s[found + len(sub):]
                    if new_s not in hash:
                        minLen = min(len(new_s), minLen)
                        que.append(new_s)
                        hash.add(new_s)

                    found = s.find(sub, found + 1)
        return minLen
