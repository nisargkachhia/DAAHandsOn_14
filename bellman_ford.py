def bellman_ford(graph, vertices, start):
    # Graph is represented as a list of edges
    # edges = [(source, destination, weight), ...]
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Check for negative weight cycles
    for u, v, w in graph:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return distances
