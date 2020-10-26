class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        #Time O(n^2) Space O(n)
        #ERROR2: forget to write corner case
        if not prerequisites:
            return True
        
        inDegree = {i:0 for i in range(numCourses)} 
        # ERROR3: did not think that some courses does not have constraints
        edges = {i:[] for i in range(numCourses)}
        
         # count in-degree and record edges
        for prev, course in prerequisites:
            edges[prev].append(course)
            # ERROR1: did not create indegree = 0 for pre-courses
            # inDegree[prerequisite[0]] = inDegree.get(prerequisite[0], 0)
            inDegree[course] += 1
        
        # start bfs from inDegree = 0
        starts = [k for k,v in inDegree.items() if v == 0]
        
        from collections import deque
        queue = deque(starts)
        isFinish = len(starts)
        # seen = set(starts) # record the course that can be finished,
        # #but not be necessary because every course only have 0 in-degree once

        # BFS 
        while queue:
            course = queue.popleft()
            for next_course in edges[course]:
                inDegree[next_course] -= 1
                if inDegree[next_course] == 0: # and next_course not in seen:
                    queue.append(next_course)
                    isFinish += 1
                
        return isFinish == numCourses
