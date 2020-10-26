"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        inDegree = {}
        topOrder = []
        
        #record in-degree
        for node in graph:
            if node not in inDegree:
                inDegree[node] = 0
            for neighbor in node.neighbors:
                inDegree[neighbor] = inDegree.get(neighbor, 0) + 1
        
        queue = [k for k,v in inDegree.items() if v == 0]
        # seen = set([k for k,v in inDegree.items() if v == 0]) 
        # not neccessary cause inDegree only turn to 0 once
        
        while queue:
            node = queue.pop(0)
            topOrder.append(node)
            for neighbor in node.neighbors:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                # and neighbor not in seen:
                    queue.append(neighbor)
                    # seen.add(neighbor)
                    
        return topOrder
        
