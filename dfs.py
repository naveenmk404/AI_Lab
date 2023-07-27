graph = {
    'A': ['C', 'B', 'D'],
    'B': ['A', 'E', 'D'],
    'C': ['A', 'D'],
    'D': ['C', 'E', 'A'],
    'E': ['D', 'B']
}

visited = []
stack = []

def dfsTraversal(graph, visited, node):
    stack.append(node)

    while stack:
        m = stack.pop()
        if m not in visited:
            visited.append(m)
            print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                stack.append(neighbour)

dfsTraversal(graph, visited, 'A')
