The goal of the exercise is to implement two most popular graph representations - adjacency matrix and adjacency list.
In the implementation, please create a class representing node data and a class representing edge data (as a backup - it will be useful in subsequent exercises).
Let all nodes be placed in a list, while the representations will contain indexes to elements of this list.
In addition, a dictionary will be useful - a map converting a node to its index in the above list.

To make the implementation of the graph independent of the class describing the node, please put in this class the methods:
eq (comparing nodes based on the chosen field identifying the node) and hash (used by the dictionary). The hash method should have the form:
def __hash__(self):
    return hash(self.key)

where key is an example name of the field that will be used to identify the node (e.g. today it will be the letter from the license plate).

Two classes with the same interface should be implemented:
- insertVertex(vertex) - inserts the given vertex into the graph
- insertEdge(vertex1, vertex2, edge) - inserts an edge between the given nodes into the graph
- deleteVertex(vertex) - deletes the given node
- deleteEdge(vertex1, vertex2) - deletes the edge between the given nodes
- getVertexIdx(vertex) - returns the index of the node (using the aforementioned dictionary)
- getVertex(vertex_idx) - returns the node with the given index (kind of the opposite of the above method)
- neighbours(vertex_idx) - returns a list of indexes of nodes adjacent to the node with the given index (outgoing connections)
- order() - returns the order of the graph (number of nodes)
- size() - returns the size of the graph (number of edges)
Additionally, the following method will be needed:
- edges() - returning all edges of the graph in the form of a list of pairs: (key_of_starting_node, key_of_ending_node) - this implementation is not standard, but it will be more useful for us to draw the graph.

When deleting a node, it should be taken into account that:

in the adjacency list, its index should be removed from all lists of neighbors, and indexes higher than it should be decremented
the dictionary needs to be updated (go through all nodes and enter their current indexes into the dictionary)