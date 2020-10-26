# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem,actions = None,passedStates = None):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print "Start:",problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # print "successor type",type(problem.getSuccessors(problem.getStartState()))

    fringe = util.Stack()
    passedStates = set()
    fringe.push((problem.getStartState(),[]))

    while not fringe.isEmpty():
        state,actions = fringe.pop()
        if problem.isGoalState(state):
            return actions
        passedStates.add(state)
        for nextStep in problem.getSuccessors(state):
            if nextStep[0] not in passedStates:
                path = list(actions)
                path.append(nextStep[1])
                fringe.push((nextStep[0],path))


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    passedStates = set()
    fringe.push((problem.getStartState(),[]))
    while not fringe.isEmpty():
        node = fringe.pop()
        if not node[0] in passedStates:
            if problem.isGoalState(node[0]):
                return node[1]
            passedStates.add(node[0])
            # print "successor: ", problem.getSuccessors(node[0])
            for next in problem.getSuccessors(node[0]):
            # if next[0] not in passedStates:
                path = list(node[1])
                path.append(next[1])
                fringe.push((next[0],path))

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    passedStates = set()
    fringe.push((problem.getStartState(),[],0),0)
    while not fringe.isEmpty():
        state,actions,cost = fringe.pop()
        if problem.isGoalState(state):
            return actions
        passedStates.add(state)
        for next in problem.getSuccessors(state):
            if next[0] not in passedStates:
                path = list(actions)
                path.append(next[1])
                newCost = cost + next[2]
                fringe.push((next[0],path,newCost),newCost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."

    fringe = util.PriorityQueue()
    passedStates = set()
    fringe.push((problem.getStartState(), [], 0), 0)
    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()
        if state not in passedStates:
            passedStates.add(state)
            if problem.isGoalState(state):
                return actions
            for successor in problem.getSuccessors(state):
                newState = successor[0]
                action = successor[1]
                newActions = actions + [action]
                newCost = problem.getCostOfActions(newActions)
                hCost = heuristic(newState,problem)
                allCost = newCost + hCost
                # print "newCost: ",type(newCost)
                # print "hCost: ",type(hCost)
                fringe.push((newState, newActions,allCost), allCost)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
