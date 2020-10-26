"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # use preOrderTraverse and BFS by layer
        # Time O(n) Space O(n)
        if not root:
            return []
            
        from collections import deque
        queue = deque([root])
        ans = []
        
        while queue:
            temp = [] # to record node of this layer
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #finish loop of this layer        
            ans.append(temp)
            
        return ans     
