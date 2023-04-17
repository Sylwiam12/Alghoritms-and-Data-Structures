import graf_mst
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
    def __init__(self, size):
        self.size = size


# lista sasiedztwa
class AdjacencyList:
    def __init__(self):
        self.elements_lst = []
        self.edges_lst = []
        self.elements_dictn = {}
        self.neighbours_lst = []

    def insertVertex(self, vertex):
        if not vertex in self.elements_lst:
            self.elements_dictn[vertex] = len(self.elements_lst)
            self.elements_lst.append(vertex)
            self.neighbours_lst.append([])

    def insertEdge(self, vertex1, vertex2, edge):
        if vertex1 in self.elements_lst and vertex2 in self.elements_lst:
            self.neighbours_lst[self.elements_dictn[vertex1]].append((self.elements_dictn[vertex2], edge.size))
            self.neighbours_lst[self.elements_dictn[vertex2]].append((self.elements_dictn[vertex1], edge.size))
            self.edges_lst.append((vertex1.key, vertex2.key))

    def deleteEdge(self, vertex1, vertex2, edge):
        if vertex1 in self.elements_lst and vertex2 in self.elements_lst:
            self.neighbours_lst[self.elements_dictn[vertex1]].remove((self.elements_dictn[vertex2], edge.size))
            self.neighbours_lst[self.elements_dictn[vertex2]].remove((self.elements_dictn[vertex1], edge.size))
            self.edges_lst.remove((vertex1.key, vertex2.key))

    def deleteVertex(self, vertex):
        if vertex in self.elements_lst:
            self.elements_lst.remove(vertex)
            del self.neighbours_lst[self.getVertexIdx(vertex)]
            for k in self.elements_lst:  # uaktualnienie slownika
                if self.elements_dictn[vertex] < self.elements_dictn[k]:
                    self.elements_dictn[k] -= 1
            help_lst = []  # nowa lista krawedzi,bez tych prowadzacych do usuwanego wierzcholka
            for k in self.edges_lst:
                if vertex.key not in k[0]:
                    help_lst.append(k)
            self.edges_lst = help_lst
            for k in self.neighbours_lst:  # uaktualnienie lisy sasiadow
                if self.elements_dictn[vertex] in k:
                    k.remove(self.getVertexIdx(vertex))
            del self.elements_dictn[vertex]

    def getVertexIdx(self, vertex):
        if self.elements_dictn[vertex]:
            return self.elements_dictn[vertex]

    def getVertex(self, vertex_idx):
        return self.elements_lst[vertex_idx]

    def neighbours(self, vertex_idx):
        lst=[]
        for element in self.neighbours_lst[vertex_idx].copy():
            if element not in lst:
                lst.append(element)
        return lst
        #return list(set(self.neighbours_lst[vertex_idx].copy()))
    def order(self):
        return len(self.elements_lst)

    def size(self):
        return len(self.edges_lst)

    def edges(self):
        return self.edges_lst


def prime_algorithm(graph):
    size = len(graph.elements_lst)
    intree = [0 for k in range(size)]
    distance = [float('inf') for k in range(size)]
    parent = [-1 for k in range(size)]

    MST_graph = AdjacencyList()
    elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for element in elements:
        MST_graph.insertVertex(Element(element))

    el_index=0 
    while intree[el_index]==0:
        intree[el_index]=1
        for element in graph.neighbours(el_index):
            if distance[element[0]] > element[1]:
                parent[element[0]] = el_index
                distance[element[0]] = element[1]

        minimum=float('inf')
        for k in range(len(distance)):
            if distance[k] < minimum  and intree[k] == 0:
                minimum = distance[k]
                el_index= k
                
        MST_graph.insertEdge(graph.getVertex(el_index),graph.getVertex(parent[el_index]),Edge(distance[el_index]))
        MST_graph.insertEdge(graph.getVertex(parent[el_index]),graph.getVertex(el_index),Edge(distance[el_index]))
    return MST_graph


def printGraph(g):
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


graph = AdjacencyList()
elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for element in elements:
    graph.insertVertex(Element(element))
for element in graf_mst.graf:
    graph.insertEdge(Element(element[0]),Element(element[1]),Edge(element[2]))
    graph.insertEdge(Element(element[1]),Element(element[0]),Edge(element[2]))
printGraph(prime_algorithm(graph))