from floyd_warshall import floyd_warshall

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3},
    'D': {}
}

distances = floyd_warshall(graph)
print("All-pairs shortest paths:")
for source, targets in distances.items():
    for target, distance in targets.items():
        print(f"Distance from {source} to {target}: {distance}")
