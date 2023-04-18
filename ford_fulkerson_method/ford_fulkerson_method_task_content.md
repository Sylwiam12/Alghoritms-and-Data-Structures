1. Introduction
The maximum flow problem involves finding a permissible maximum-value flow for a given flow network.
A flow network is a directed graph in which each edge has a non-negative capacity and two special vertices s and t.
The maximum flow/minimum cut theorem states that in a flow network, the maximum value of flow from the source (s) to the sink (t) is equal to the total weight of edges in a minimum cut, i.e., the smallest total weight of edges that will separate the source from the sink.

2. Exercise objective
    - adaptation of the data structure describing the graph to the FF/EK algorithms
    - implementation of the FF/EK algorithms and tests for selected directed graphs:

        - BFS search

        - path analysis, flow calculation

        - path augmentation

    - application of the max flow/min cut theorem


3. Modification of the data structure
Concept: We need a better description of the edges. In addition to weight (capacity), it is necessary to store information about the current flow (flow), residual flow (residual), and a flag called isResidual, which indicates whether the edge is "real" or "residual."

Implementation (proposal):

- Create a class (e.g., Edge) with the mentioned attributes, in which init receives the capacity and information about whether the edge is "residual." In the "non-residual" edge, the initial residual flow is initialized with the capacity value, and the initial flow is set to 0. In the "residual" edge, the initial residual flow is zero (the 'flow' flow is not used).

- Allow the edge to be printed using the print method (the repr method that places capacity, flow, residual flow, and True or False - whether the edge is residual or not - separated by spaces in the string).

4. Graph loading
During graph loading, we proceed similarly to the previous exercise: we add two vertices that the loaded edge connects, as well as the edge itself. The number given with the edge represents the capacity (which will initiate the residual flow value). In addition, we add a second edge connecting the vertices in the opposite direction - this residual edge has the initial residual flow set to zero and is flagged as residual.
Note. The described solution is not the only one and certainly not the best. If the proposal "does not fit" the used graph representation - please adjust the algorithm. Nevertheless, the "explicit" addition of residual edges simplifies the implementation of graph traversal and is certainly easier to interpret.

5. Breadth First Search (BFS)
We will use the algorithm for traversing a graph in breadth-first order (BFS). Additionally, since we need to keep track of the path taken, we will save the parent of each selected vertex.

Short description:

initialization:

- create and initialize the visited and parent arrays of size equal to the number of vertices, and create a queue (list in Python),

- add the starting point (index of the initial vertex) to the queue and mark it as visited (in the visited array)

- in a while loop with the condition of the queue not being empty:

- get an element from the queue,

- get its neighbors,

- in a loop over the neighbors, check if the vertices have not been visited and if the residual flow is greater than 0 (note - this is the "non-standard" condition). If so, add the neighbor to the queue, mark it as visited, and save its parent (i.e., the element we removed from the queue).

Wrap the whole thing in a function (or a class method) that returns the parent list.

6. Path analysis, calculating the smallest capacity.
Concept: We are given a graph, a starting vertex, an ending vertex, and a parent list. Based on this, we need to reconstruct the path and determine the maximum flow through the path, which is the smallest capacity edge (the "bottleneck").

Implementation:

1. We need two variables to store the current vertex index and the smallest capacity. We initialize the first with the index of the end vertex and the second with a "large number" such as float('Inf').

2. At the beginning, we check if the end vertex has a parent (which in practice means that there is a path to it in the current iteration, and the BFS algorithm has "reached" it). If not, we return a flow value of 0.

3. Otherwise, in a while loop, as long as we have not reached the starting vertex:

    - for the current vertex, we find the "real" edge leading to its parent (not the residual edge),

    - we check if the residual flow of this edge is smaller than the smallest found so far - if so, we update it,

    - we move the current vertex index to its parent.

We pack the code into a function and return the calculated smallest capacity.

7. Path augmentation
Concept. The input is a graph, a start vertex, an end vertex, a list of parents, and a minimum capacity. We "traverse" the path again, this time updating the flow and residual flow.

Implementation:

1. The general approach is very similar to calculating the minimum capacity described above.

2. When traversing the path, we need to consider two edges: the "actual" edge from the parent to the current node and the "residual" edge from the current node to its parent:

    - For "actual" edges, we add the minimum capacity value to the flow (increasing the flow in that edge), while subtracting this value from the residual flow.

    - For "residual" edges, we add the minimum capacity to the residual flow.

8. Ford-Fulkerson Algorithm in Edmonds-Karp version
Concept and implementation. After preparing everything, we can assemble the complete algorithm. We start by performing a BFS search on the graph, checking if there is a path from the start vertex to the end vertex and calculating the minimum flow for it. Then, in a while loop, if the minimum flow > 0, the following steps will be executed:

    - path augmentation,

    - BFS,

    - calculating the new value of the minimum flow.

Finally, we need to return the sum of the flows through the edges entering the end vertex.