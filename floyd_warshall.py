def floyd_warshall(graph):
    # Graph is represented as a dictionary of dictionaries
    # graph = {node: {neighbor: weight, ...}, ...}
    nodes = list(graph.keys())
    dist = {node: {neighbor: float('inf') for neighbor in nodes} for node in nodes}

    for node in nodes:
        dist[node][node] = 0
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
