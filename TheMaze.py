class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # Time O(n*m)
        # Space O(n*m)
        
        queue = [tuple(start)]
        seen = {tuple(start)}
        
        while queue:
            node = queue.pop(0)
            #ERROR3: destination is a list, should be changed to tuple
            if node == tuple(destination):
                return True
            for next_node in self.getNextNodes(node, maze, seen):
                if next_node not in seen:
                    queue.append(next_node)
                    seen.add(next_node)
        
        return False
                
    def getNextNodes(self, node, maze, seen):
        ans = []
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # x,  y = node ERROR: x, y should be back to initial status when change directions
        
        for dx, dy in DIRECTIONS:
            x,  y = node
            while not self.isWall(x+dx, y+dy, maze):
                x += dx
                y += dy
            if (x, y) != node and (x, y) not in seen:
                ans.append((x, y))
        
        return ans
        
    def isWall(self, x, y, maze):
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
            return maze[x][y]
            
        return True# ERROE: wrote False
