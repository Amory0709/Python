class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # Time O(nm)  n:# of word   m: len of word
        # Space O(n) 
    
        dict.add(end)
        queue = [start]
        seen = set([start])
        
        length = 1
        #ERROR2: wrote queue as start
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.pop(0)
                if word == end:
                    return length
                    
                for next_w in self.getNextWords(word, dict):
                    if next_w not in seen:
                        queue.append(next_w)
                        seen.add(next_w)
            length += 1
        
        return 0
    
    def getNextWords(self, word, dict):
        ans = []
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(word)):
            for letter in letters:
                new_word = word[:i] + letter + word[i+1:]
                # ERROR 1: did not omit the same word
                if new_word in dict and new_word != word:
                    ans.append(word[:i] + letter + word[i+1:])
        
        return ans
