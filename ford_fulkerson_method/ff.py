class Element:
    def __init__(self, key, color=None, value=None):
        self.color = color
        self.key = key
        self.value = value

    def __eq__(self, new):
        if self.key ==new.key:
            return True

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

class Edge:
    def __init__(self, size, isResidual= False,flow=0):
        self.size = size
        self.flow = flow
        self.residual = size
        self.isResidual  = isResidual
    
    def __str__(self):
        return str(self.size) + ' ' + str(self.flow) + ' ' + str(self.residual) + ' ' + str(self.isResidual)



class AdjacencyList:
    def __init__(self):
        self.elements_lst = []
        self.edges_lst = []
        self.elements_dictn = {}
        self.neighbours_lst = []

    def insertVertex(self,vertex):
        if not vertex in self.elements_lst:
            self.elements_dictn[vertex] = len(self.elements_lst)
            self.elements_lst.append(vertex)
            self.neighbours_lst.append([])
            
    def insertEdge(self, vertex1, vertex2, edge):
        if vertex1 in self.elements_lst and vertex2 in self.elements_lst:
            if self.elements_dictn[vertex2] not in self.neighbours_lst[self.elements_dictn[vertex1]]:
                self.neighbours_lst[self.elements_dictn[vertex1]].append((self.elements_dictn[vertex2], edge))
            self.edges_lst.append((vertex1.key, vertex2.key))

    # def deleteEdge(self, vertex1, vertex2, edge):
    #     if vertex1 in self.elements_lst and vertex2 in self.elements_lst:
    #         self.neighbours_lst[self.elements_dictn[vertex1]].remove((self.elements_dictn[vertex2], edge))
    #         self.neighbours_lst[self.elements_dictn[vertex2]].remove((self.elements_dictn[vertex1], edge))
    #         self.edges_lst.remove((vertex1.key, vertex2.key))

    # def deleteVertex(self, vertex):
    #     if vertex in self.elements_lst:
    #         self.elements_lst.remove(vertex)
    #         del self.neighbours_lst[self.getVertexIdx(vertex)]
    #         for k in self.elements_lst:  # uaktualnienie slownika
    #             if self.elements_dictn[vertex] < self.elements_dictn[k]:
    #                 self.elements_dictn[k] -= 1
    #         help_lst = []  # nowa lista krawedzi,bez tych prowadzacych do usuwanego wierzcholka
    #         for k in self.edges_lst:
    #             if vertex.key not in k[0]:
    #                 help_lst.append(k)
    #         self.edges_lst = help_lst
    #         for k in self.neighbours_lst:  # uaktualnienie lisy sasiadow
    #             if self.elements_dictn[vertex] in k:
    #                 k.remove(self.getVertexIdx(vertex))
    #         del self.elements_dictn[vertex]     
    
    def getVertexIdx(self, vertex):
        return self.elements_dictn[vertex]

    def getVertex(self, vertex_idx):
        return self.elements_lst[vertex_idx]

    def neighbours(self, vertex_idx):
        return self.neighbours_lst[vertex_idx]

    def order(self):
        return len(self.elements_lst)

    def size(self):
        return len(self.edges_lst)

    def edges(self):
        return self.edges_lst
    

def printGraph(g):#z instrukcji
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")

def BFS(graph, start):
    size=len(graph.elements_lst)
    visited = [None for k in range(size)]
    parent = [None for k in range(size)]
    stack = [start]
    while stack:
        element=stack.pop(0)
        for el in graph.neighbours(element):
            if not visited[el[0]] and el[1].residual > 0:
                visited[el[0]] = 1 #1- odwiedzony
                stack.append(el[0])
                parent[el[0]] = element
    return parent


def path_analysis(graph, start, stop, parents):
    actual_idx=graph.getVertexIdx(stop)
    start_idx=graph.getVertexIdx(start)
    minimum_size=float('inf') 
    if not parents[actual_idx]:
        return 0
    while actual_idx != start_idx:
        for element in graph.neighbours_lst[parents[actual_idx]]:
            if element[0] == actual_idx and element[1].residual<minimum_size and element[1].isResidual==False:
                minimum_size = element[1].residual
        actual_idx = parents[actual_idx]
    return minimum_size

def path_augmentation(graph, start, stop, parents, minimum_size):
    actual_idx = graph.getVertexIdx(stop)
    start_idx=graph.getVertexIdx(start)
    if not parents[actual_idx]:
        return 0
    else:
        while actual_idx != start_idx:
            for element in graph.neighbours_lst[parents[actual_idx]]:
                if element[0] == actual_idx:
                    element[1].flow+=minimum_size
                    element[1].residual-=minimum_size
            for element in graph.neighbours_lst[actual_idx]:
                if element[0] == parents[actual_idx]:
                    element[1].residual+=minimum_size
            actual_idx = parents[actual_idx]
            
    
def FordFulkerson(graph, start, stop):
    start_idx = graph.getVertexIdx(start)
    parents = BFS(graph, start_idx)
    minimum_size = path_analysis(graph, start, stop, parents)
    sum=minimum_size
    while minimum_size > 0:
        path_augmentation(graph, start, stop, parents, minimum_size)
        parents = BFS(graph, start_idx)
        minimum_size = path_analysis(graph, start, stop, parents)
        sum+=minimum_size
    return sum
    
graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
graphs=[graf_0,graf_1,graf_2,graf_3]
for graph in graphs:
    new_graph = AdjacencyList()
    for element in graph: 
        new_graph.insertVertex(Element(element[0]))
        new_graph.insertVertex(Element(element[1]))
        new_graph.insertEdge(Element(element[0]), Element(element[1]), Edge(element[2]))
        new_graph.insertEdge(Element(element[1]),Element(element[0]), Edge(0, True))
    print(FordFulkerson(new_graph, Element('s'), Element('t')))
    printGraph(new_graph)