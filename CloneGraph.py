"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        #ERROR1: corner case
        if not node:
            return node
            
        # Time Space
        nodes = self.getNodes(node)
        
        #record old -> new
        mapping = {}
        # copy node
        for nod in nodes:
            mapping[nod] = UndirectedGraphNode(nod.label)
        
        #copy edges
        for nod in nodes:
            for neighbor in nod.neighbors:
                mapping[nod].neighbors.append(mapping[neighbor])
        
        return mapping[node]
    
    def getNodes(self, node):
        queue = [node]
        ans = {node}
        
        while queue:
            node = queue.pop()
            for neighbor in node.neighbors:
                if neighbor not in ans:
                    queue.append(neighbor)
                    ans.add(neighbor)
                    
        return ans                  

# use stack
class Solution1:

    def __init__(self):
        self.dict = {}
        
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node is None:
            return None
            
        if node.label in self.dict:
            return self.dict[node.label]
            
        root = UndirectedGraphNode(node.label)
        self.dict[node.label] = root
        for item in node.neighbors:
            root.neighbors.append(self.cloneGraph(item))

        return root
