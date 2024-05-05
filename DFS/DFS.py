
# Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected
# graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
# structure. 


def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': [],
}

print("DFS:")
visited = set()
dfs(graph, '5', visited)