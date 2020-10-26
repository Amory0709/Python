class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.nums = []
        self.size = size
        self.sum = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        if len(self.nums) >= self.size:
            self.sum -= self.nums.pop(0)
        self.sum += val
        self.nums.append(val)
        return self.sum/len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
