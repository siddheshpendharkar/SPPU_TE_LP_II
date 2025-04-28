graph = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (comma separated, leave blank if none): ").split(',')
    if neighbors == ['']:  # if empty input
        neighbors = []
    graph[node] = neighbors

# BFS Implementation
visited = []
queue = []

def breadthFirstSearch(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# DFS Implementation
visited_dfs = set()

def depthFirstSearch(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            depthFirstSearch(visited, graph, neighbour)

start_node = input("Enter the starting node: ").strip()

while start_node not in graph:
    print("Invalid starting node. Please enter a valid node from the graph.")
    start_node = input("Enter the starting node: ").strip()

print("\nBreadth-First Search:")
breadthFirstSearch(visited, graph, start_node)

print("\nDepth-First Search:")
depthFirstSearch(visited_dfs, graph, start_node)
