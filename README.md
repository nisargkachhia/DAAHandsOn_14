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

### **1.Dijkstra's Algorithm**

**Input:**

    graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
    }

**Output:**

   ```plaintext
   Shortest distances from A: {'A': 0, 'B': 1, 'C': 3}
   ```
![Dijkstra](https://github.com/user-attachments/assets/c4b71744-d1a5-4ab6-84e0-44e4d4d33502)

### **2.Bellman-Ford Algorithm**
**Input**
   ```python
   edges = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 4),
    ('C', 'D', 3),
    ('B', 'D', 6)
   ]
   ```
**Output:**

   ```plaintext
   Shortest distances from A: {'A': 0, 'B': 1, 'C': 3}
   ```
![Bellman-Ford](https://github.com/user-attachments/assets/9f017b7d-4e12-465c-be4a-682e9a57fa2c)

### **3.Floyd-Warshall Algorithm**
**Input**
   ```python
   {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2},
    'C': {}
   }
   ```
**Output:**

   ```vbnet
   All-pairs shortest paths:
   Distance from A to A: 0
   Distance from A to B: 1
   Distance from A to C: 3
   Distance from B to A: inf
   Distance from B to B: 0
   Distance from B to C: 2
   Distance from C to A: inf
   Distance from C to B: inf
   Distance from C to C: 0
   ```
![Floyd-Warshall](https://github.com/user-attachments/assets/8f0b94d5-7886-40f7-bb2b-aafa95cdb9da)
