def create_graph():
    graph = {}
    while True:
        source = input("Enter source node (or 'done' to finish): ")
        if source == "done":
            break
        destination = input("Enter destination node: ")

        # Add edge for source node
        graph.setdefault(source, []).append(destination)

        # Add edge for destination node (if undirected graph)
        if graph.get(destination) is None:
            graph[destination] = []
        graph[destination].append(source)

    return graph

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Enter graph:")
graph = create_graph()

starting_node = input("Enter starting node for DFS: ")

print("Depth-First Search:")
dfs(visited, graph, starting_node)