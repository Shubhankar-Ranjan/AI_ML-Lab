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

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print (m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Enter graph:")
graph = create_graph()

starting_node = input("Enter starting node for BFS: ")

print("Breadth-First Search:")
bfs(visited, graph, starting_node)