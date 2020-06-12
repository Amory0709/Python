class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # Time O(n^2) Space O(n)
        #corner
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        inDegree = {i:0 for i in range(numCourses)} #record inDegree
        edges = {i:[] for i in range(numCourses)} # record edges
        
        for course,prev in prerequisites:
            inDegree[course] += 1
            edges[prev].append(course)
        
        # start BFS from inDegree=0
        queue = [k for k,v in inDegree.items() if v == 0]
        ans = [k for k,v in inDegree.items() if v == 0]
        
        while queue:
            course = queue.pop(0)
            for next_course in edges[course]:
                inDegree[next_course] -= 1
                if inDegree[next_course] == 0:
                    queue.append(next_course)
                    ans.append(next_course)
        
        # Impossible to finish
        if len(ans) != numCourses:
            return []
        
        return ans
        
