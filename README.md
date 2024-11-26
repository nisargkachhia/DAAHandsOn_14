# DAAHandsOn_14

## Shortest Path Algorithms

This project implements three popular shortest-path algorithms, packaged with an interactive `main.py` script for easy execution. The supported algorithms are:

1. **Dijkstra's Algorithm** - Calculates the shortest paths from a single source node in a graph with non-negative edge weights.
2. **Bellman-Ford Algorithm** - Computes shortest paths in a graph with possible negative edge weights and detects negative weight cycles.
3. **Floyd-Warshall Algorithm** - Computes shortest paths between all pairs of nodes in a graph.

---

## **Features**

- Modular implementation of the algorithms in separate Python files.
- Interactive `main.py` for testing algorithms with custom inputs.
- Example scripts to demonstrate how each algorithm works.

---

## **File Structure**

DAAHANDSON_14/
│
├── dijkstra.py # Implementation of Dijkstra's algorithm
├── bellman_ford.py # Implementation of Bellman-Ford algorithm
├── floyd_warshall.py # Implementation of Floyd-Warshall algorithm
├── examples/ # Examples demonstrating algorithm usage
│ ├── example_dijkstra.py
│ ├── example_bellman_ford.py
│ └── example_floyd_warshall.py
├── main.py # Interactive program to test algorithms
└── README.md

---

## **Usage**

### **Run `main.py`**

The `main.py` script allows you to interactively select an algorithm and input graph data.

1. Navigate to the project folder:

   ```bash
   cd algorithms
   ```

2. Run the interactive script:

    ```bash
    python main.py
    ```

3. Follow the prompts to:

- Choose an algorithm (1: Dijkstra, 2: Bellman-Ford, 3: Floyd-Warshall, 4: Exit).
- Input the graph data in the appropriate format.
- View the results directly.

## Example Outputs

```markdown
### 1.Dijkstra's Algorithm

**input:**

    ```python
    {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2)],
        'C': []
    }

