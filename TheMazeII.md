# 788. The Maze II
[link](lintcode.com/problem/the-maze-ii/description)

*Method*: BFS

*Time Complexity*: O(n^4)?

*Space Complexity*: O(n)

## Analysis
![alt text](https://github.com/Amory0709/Data-Structure-and-Algorithm/blob/master/TheMazeII.jpg)

## Code as below:
```python
#我的代码还是一步一步走， 但是也可以考虑沿着一个方向一直走直到停止
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # TIME SPACE
        # BFS by layer
        if not maze or not maze[0]:
            return -1
            
        start = tuple(start)
        destination = tuple(destination)
        
        queue = [(start, None)] 
        seen = {(start, None)}
        # add direction, same node + diff direction --> different situation
        distance = 0
        isFinished = []
        
        while queue:
            distance += 1 
            for _ in range(len(queue)):
                node, prev_direction = queue.pop(0) 
                # find next node
                for next_node, direction in self.nextNodes(maze, node, prev_direction):
                    if next_node == destination: 
                        if self.isWall(maze, next_node[0] + direction[0], next_node[1] + direction[1]):
                            isFinished.append(distance)
                            #ERROR n: return -1 directly if this direction did not hit the wall
                            
                    if (next_node, direction) not in seen:
                        queue.append((next_node, direction))
                        seen.add((next_node, direction))
                        
        if isFinished:
            return min(isFinished)
            
        return -1
    
    def nextNodes(self, maze, node, prev_direction):
        ans = []
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]
        x, y = node
        
        # have previous directions
        if prev_direction:
            px, py = prev_direction
            if self.isWall(maze, x + px, y + py):
                for dx,dy in directions:
                    if (dx,dy) == (px, py):
                        continue
                    if self.isWall(maze, x + dx, y + dy):
                        continue
                    ans.append(((x + dx, y + dy), (dx, dy)))
                return ans
            return [((x + px, y + py), prev_direction)] 
            
        # no prev_direction            
        for dx,dy in directions:
            if self.isWall(maze, x + dx, y + dy):
                continue
            ans.append(((x + dx, y + dy), (dx, dy)))
        return ans
    
    def isWall(self, maze, x, y):
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
            if not maze[x][y]:
                return False
        return True

#一个我比较喜欢的解法
class Solution1:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """

    def shortestDistance(self, maze, start, destination):
        queue = deque([(start[0], start[1], 0)])
        visited = {(start[0], start[1])}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        minDist = -1

        while queue:
            size = len(queue)

            for _ in range(size):
                x, y, front = queue.popleft()

                if x == destination[0] and y == destination[1]:
                    minDist = front if minDist == -1 else min(minDist, front)

                for dx, dy in directions:
                    nextX, nextY = x + dx, y + dy
                    count = 0
                    while self.isValid(maze, nextX, nextY):
                        nextX += dx
                        nextY += dy
                        count += 1
                    nextX -= dx
                    nextY -= dy

                    if (nextX, nextY) not in visited:
                        queue.append((nextX, nextY, front + count))
                        visited.add((nextX, nextY))

        return minDist

    def isValid(self, maze, x, y):
        rows, cols = len(maze), len(maze[0])
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0
```
