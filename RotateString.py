class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        #!!!!!
        if len(s) > 0:
            offset = offset % len(s)
            
        temp = (s + s)[len(s) - offset : 2 * len(s) - offset]

        for i in range(len(temp)):
            s[i] = temp[i]
