DFS
graph={

    'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'E':[],
    'D':[]
}

visited=set()

def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for n in graph[root]:
            dfs(visited,graph,n)

dfs(visited,graph,'A')


BFS
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

visited=[]
queue=[]



def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for n  in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

bfs(visited , graph , '5')

TowerOfHanai
def towerofhanai(n,a,b,c):
    if n==1:
        print('move 1st disk from',a,'to',c)
        return 
    towerofhanai(n-1,a,c,b)
    print('move', n ,'disk from',a,'to',c)
    towerofhanai(n-1,b,a,c)


towerofhanai(2,'s','h','d')

Water Jug
def pour(ja, jb):
    max1, max2, final = 5, 7, 4
    print("%d\t%d" % (ja, jb))  

    if jb == final:
        return
    elif jb == max2:
        pour(0, ja)
    elif ja != 0 and jb == 0:
        pour(0, jb)
    elif ja == final:
        pour(ja, 0)
    elif ja < max1:
        pour(max1, jb)
    elif jb < (max2 - jb):  # Changed to (max2 - ja) for correct subtraction
        pour(0, (ja + jb))
    else:
        pour(ja - (max2 - jb), (max2 - jb) + jb)

print("A \t B")
pour(0,0)


Monkey
class MonkeyBananaProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        actions = []
        if state["monkey"] == "A" and state["box"] == "A":
            actions.append("climb")
        elif state["monkey"] == state["box"]:
            actions.append("push")
        return actions

    def result(self, state, action):
        new_state = state.copy()
        if action == "climb":
            new_state["monkey"] = "B"
        elif action == "push":
            new_state["monkey"] = new_state["box"] = "A"
        return new_state

    def goal_test(self, state):
        return state == self.goal_state

def depth_first_search(problem):
    stack = [(problem.initial_state, [])]
    while stack:
        state, path = stack.pop()
        if problem.goal_test(state):
            return path
        for action in problem.actions(state):
            new_state = problem.result(state, action)
            stack.append((new_state, path + [action]))
    return None

if __name__ == "__main__":
    initial_state = {"monkey": "A", "box": "A", "banana": "B"}
    goal_state = {"monkey": "B", "box": "A", "banana": "B"}

    monkey_banana_problem = MonkeyBananaProblem(initial_state, goal_state)
    solution = depth_first_search(monkey_banana_problem)

    if solution:
        print("Solution:", solution)
    else:
        print("No solution found.")
