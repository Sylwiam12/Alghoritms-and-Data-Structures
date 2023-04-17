import polska
class Element:
    def __init__(self,key,value=None):
        self.key=key
        self.value=value
    def __eq__(self,new):
        if self.key==new.key:
            return True
    def __hash__(self):
        return hash(self.key)

class Edge:
    def __init__(self,size=1):
        self.size=size


class AdjacencyList:
    def __init__(self):
        self.elements_lst=[]
        self.edges_lst=[]
        self.elements_dictn={}
        self.neighbours_lst=[]

    def insertVertex(self,vertex):
        if not vertex in self.elements_lst:
            self.elements_dictn[vertex]=len(self.elements_lst)
            self.elements_lst.append(vertex)
            self.neighbours_lst.append([])
    
    def insertEdge(self,vertex1, vertex2, edge):
        if vertex1 in self.elements_lst and vertex2 in self.elements_lst:
            self.neighbours_lst[self.elements_dictn[vertex1]].append(self.elements_dictn[vertex2])
            self.neighbours_lst[self.elements_dictn[vertex2]].append(self.elements_dictn[vertex1])
            self.edges_lst.append((vertex1.key,vertex2.key))

    def deleteEdge(self,vertex1, vertex2):
        if vertex1 in self.elements_lst and vertex2 in self.elements_lst:
            self.neighbours_lst[self.elements_dictn[vertex1]].remove(self.elements_dictn[vertex2])
            self.neighbours_lst[self.elements_dictn[vertex2]].remove(self.elements_dictn[vertex1])
            self.edges_lst.remove((vertex1.key,vertex2.key))

    def deleteVertex(self, vertex):
        if vertex in self.elements_lst:
            self.elements_lst.remove(vertex)
            del self.neighbours_lst[self.elements_dictn[vertex]]
            for k in self.elements_lst: #uaktualnienie slownika
                if self.elements_dictn[vertex]<self.elements_dictn[k]:
                    self.elements_dictn[k]-=1  
            help_lst=[]  #nowa lista krawedzi,bez tych prowadzacych do usuwanego wierzcholka
            for k in self.edges_lst:
                if vertex.key not in k:
                    help_lst.append(k)
            self.edges_lst=help_lst
            for k in self.neighbours_lst: #uaktualnienie lisy sasiadow
                if self.elements_dictn[vertex] in k:
                    k.remove(self.elements_dictn[vertex])
            del self.elements_dictn[vertex]

    def getVertexIdx(self,vertex):
        if self.elements_dictn[vertex]:
            return self.elements_dictn[vertex]

    def getVertex(self,vertex_idx):
        if self.elements_lst[vertex_idx]:
            return self.elements_lst[vertex_idx]

    def neighbours(self,vertex_idx):
        if self.neighbours_lst[vertex_idx]:
            return self.neighbours_lst[vertex_idx]

    def order(self):
        return len(self.elements_lst)

    def size(self):
        return len(self.edges_lst)

    def edges(self):
        return self.edges_lst

#macierz sasiedztwa
class AdjacencyMatrix:
    def __init__(self):
        self.elements_matrix=[[]]
        self.edges_lst=[]
        self.elements_dictn={}
        self.elements_lst=[]

    def insertVertex(self,vertex):
        if vertex not in self.elements_lst:
            self.elements_dictn[vertex] = len(self.elements_lst)
            self.elements_lst.append(vertex)
            if self.elements_matrix!=[[]]:
                help_lst=[]
                for k in range(len(self.elements_matrix[0])):
                    help_lst.append(0)
                self.elements_matrix.append(help_lst)
            for k in self.elements_matrix:
                k.append(0)

    def insertEdge(self,vertex1, vertex2, edge):
        if vertex1 in self.elements_lst and vertex2 in self.elements_lst:
            self.elements_matrix[self.elements_dictn[vertex1]][self.elements_dictn[vertex2]] = edge.size
            self.elements_matrix[self.elements_dictn[vertex2]][self.elements_dictn[vertex1]]=edge.size
            self.edges_lst.append((vertex1.key,vertex2.key))


    def deleteEdge(self,vertex1, vertex2):
        if vertex1 in self.elements_lst  and vertex2 in self.elements_lst :
            self.elements_matrix[self.elements_dictn[vertex1]][self.elements_dictn[vertex2]]=0
            self.elements_matrix[self.elements_dictn[vertex2]][self.elements_dictn[vertex1]]=0
            self.edges_lst.remove((vertex1.key,vertex2.key))


    def deleteVertex(self, vertex):
        if vertex in self.elements_lst:
            self.elements_lst.remove(vertex)
            del self.elements_matrix[self.elements_dictn[vertex]]
            for k in self.elements_matrix:
                del k[self.elements_dictn[vertex]]    
            for k in self.elements_lst: #uaktualnienie slownika
                if self.elements_dictn[vertex]<self.elements_dictn[k]:
                    self.elements_dictn[k]-=1  
            help_lst=[]  #nowa lista krawedzi,bez tych prowadzacych do usuwanego wierzcholka
            for k in self.edges_lst:
                if vertex.key not in k:
                    help_lst.append(k)
            self.edges_lst=help_lst
            del self.elements_dictn[vertex]

    def getVertexIdx(self,vertex):
        if self.elements_dictn[vertex]:
            return self.elements_dictn[vertex]

    def getVertex(self,vertex_idx):
        if self.elements_lst[vertex_idx]:
            return self.elements_lst[vertex_idx]

    def neighbours(self,vertex_idx):
        neighbour_lst=[]
        for k in range(len(self.elements_matrix[vertex_idx])):
            if self.elements_matrix[vertex_idx][k]==1:
                neighbour_lst.append(k)
        return neighbour_lst    

    def order(self):
        return len(self.elements_lst)

    def size(self):
        return len(self.edges_lst)

    def edges(self):
        return self.edges_lst


# graph = AdjacencyMatrix()
graph = AdjacencyList()    
for element in polska.polska:
    graph.insertVertex(Element(element[2]))  
for edge in polska.graf:
    graph.insertEdge(Element(edge[0]),Element(edge[1]),Edge())
graph.deleteVertex(Element('K'))
graph.deleteEdge(Element('W'), Element('E'))
graph.deleteEdge(Element('E'), Element('W'))
polska.draw_map(graph.edges())