class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    Time: O(n) n stands for node count
    Space: O(n)
    """
    def zombie(self, grid):
        #多源点bfs
        m = len(grid)
        n = len(grid[0])
        
        if not m or not n:
            return -1
            
        zombieQ = []
        isPeople = set()
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    isPeople.add((i,j))
                if  grid[i][j] == 1:
                    zombieQ.append((i,j))
                    visited.add((i,j))
        
        day = 0
        while zombieQ:
            #do we still have people alive
            if len(isPeople) == 0:
                return day
                
            for i in range(len(zombieQ)):
                #BFS for each zombie
                x, y = zombieQ.pop(0)
                for next_x, next_y in self.getNexts(x, y, grid, visited):
                    zombieQ.append((next_x,next_y))
                    visited.add((next_x, next_y))
                    isPeople.remove((next_x, next_y))
                
            day += 1
            
        if len(isPeople) != 0:
            return -1
    
    def getNexts(self, x, y, grid, visited):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = []
        
        for dx, dy in DIRECTIONS:
            next_x, next_y = x + dx, y + dy 
            # decide if is Wall
            if (0 <= next_x < len(grid)) and (0 <= next_y < len(grid[0])) and grid[next_x][next_y] != 2:
                if (next_x, next_y) not in visited:
                    ans.append((next_x,next_y))
        
        return ans
