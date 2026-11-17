# CMPS 2200 Recitation 09

## Answers

**Name:**Zack Mitra


Place all written answers from `recitation-09.md` here for easier grading.



- **2) (2 pts)** What is the worst-case work of your algorithm, assuming $G$ has $k$ connected components?

The worst-case work is O(V + E log V + k), where V is the number of vertices, E is the number of edges, and k is the number of connected components. The outer loop visits each vertex once, requiring O(V) work. We initialize Prim's algorithm for each of the k components, requiring O(k) additional work. Each edge is processed a constant number of times, and heap operations require O(log V) work, giving O(E log V). Since k ≤ V, the total work simplifies to O(V + E log V)



- **4) (2 pts)** What is the work of your full algorithm in the previous answer?


The total work is O((n^2)log n), where n is the number of cities. First, creating the vertices requires O(n) work. Next, constructing the fully connected graph requires O(n^2) work because we calculate the Euclidean distance between every pair of cities. Finally, Prim's algorithm takes O(V + E log V) work using a min-heap. Since the fully connected graph has n vertices and O(n^2) edges, Prim's algorithm requires O((n^2)log n) work. Therefore, the overall work is O((n^2)log n).