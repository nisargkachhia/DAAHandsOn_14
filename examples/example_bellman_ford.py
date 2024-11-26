from bellman_ford import bellman_ford

edges = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 4),
    ('C', 'D', 3),
    ('B', 'D', 6)
]
vertices = ['A', 'B', 'C', 'D']
start_node = 'A'

distances = bellman_ford(edges, vertices, start_node)
print(f"Shortest distances from {start_node}: {distances}")
