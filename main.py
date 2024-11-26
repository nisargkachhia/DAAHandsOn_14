from dijkstra import dijkstra
from bellman_ford import bellman_ford
from floyd_warshall import floyd_warshall


def get_graph_input():
    """Helper to get graph input as adjacency list or edges."""
    print("Enter the graph as adjacency list:")
    print("Example for Dijkstra/Floyd-Warshall:")
    print("{ 'A': [('B', 1), ('C', 4)], 'B': [('C', 2)], 'C': [] }")
    graph = eval(input("Enter your graph: "))
    return graph


def get_edges_and_vertices():
    """Helper to get graph input as edge list."""
    print("Enter the graph as edge list:")
    print("Example for Bellman-Ford:")
    print("[('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 4)]")
    edges = eval(input("Enter your edges: "))
    vertices = set()
    for u, v, _ in edges:
        vertices.add(u)
        vertices.add(v)
    return edges, list(vertices)


def main():
    while True:
        print("\nChoose an algorithm to run:")
        print("1. Dijkstra's Algorithm")
        print("2. Bellman-Ford Algorithm")
        print("3. Floyd-Warshall Algorithm")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            graph = get_graph_input()
            start = input("Enter the starting node: ")
            distances = dijkstra(graph, start)
            print(f"Shortest distances from {start}: {distances}")

        elif choice == '2':
            edges, vertices = get_edges_and_vertices()
            start = input("Enter the starting node: ")
            try:
                distances = bellman_ford(edges, vertices, start)
                print(f"Shortest distances from {start}: {distances}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            graph = get_graph_input()
            distances = floyd_warshall(graph)
            print("All-pairs shortest paths:")
            for source, targets in distances.items():
                for target, distance in targets.items():
                    print(f"Distance from {source} to {target}: {distance}")

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
