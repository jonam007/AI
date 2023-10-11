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