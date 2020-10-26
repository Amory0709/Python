class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        hash = {}
        for i, num in enumerate(numbers):
            # Prevent the a + a == target
            if target - num in hash:
                return [hash[target - num], i]
                
            hash[num] = i
            
        return [-1,-1]
        
