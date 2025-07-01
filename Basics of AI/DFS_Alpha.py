def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        print(node)
        visited.append(node)
        for child in graph[node]:
            dfs(graph, child, visited)

graph = {
    'A':['B'],
    'B':['C','D'],
    'C':['E'],
    'D':[],
    'E':[]
}

dfs(graph, 'A')


