graph={
    'A' : ['C','B','D'],
    'B' : ['A','E','D'],
    'C' : ['A','D'],
    'D' : ['C','E'],
    'E' : ['D','B']
}

visited = []
queue = []

def bfsTraversal(graph,visited,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited :
                visited.append(neighbour)
                queue.append(neighbour)

bfsTraversal(graph,visited,'A')
