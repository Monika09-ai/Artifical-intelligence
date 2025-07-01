def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        print(node)
        visited.append(node)
        for child in graph[node]:
            dfs(graph, child, visited)

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

dfs(graph, 1)

