class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.queue1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        for _ in range(len(self.queue1) - 1):
            self.queue2.append(self.queue1.pop(0))
            
        value = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return value

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.queue1[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.queue1) == 0
