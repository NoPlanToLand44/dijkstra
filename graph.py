class Graph: 
    def __init__(self, gdict:dict = None ):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_vertex(self,vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False


    def addEdge(self, vertex, *edge):
        # create the vertex in question 
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
        # make sure edges lead to real vertexes 
        for vert2 in edge:
            if vert2 in self.gdict.keys():
                # make sure the connection doesnt exist already 
                if vert2 not in self.gdict[vertex]:
                    self.gdict[vertex].extend(edge)
            else: 
                raise Exception("vertex not in graph")

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            try: 
               self.gdict[vertex1].remove(vertex2)
               self.gdict[vertex2].remove(vertex1)
            except ValueError:
                pass
    def removeVertex(self, vertex):
        # check if vertex exists
        if vertex in self.gdict.keys():
            #try to remove it, raise an error if u cannt
            try: 
                self.gdict.pop(vertex)
                # remove all the edges as well: 
                for key in self.gdict.keys():
                    if vertex in self.gdict[key]:
                        self.gdict[key].remove(vertex)
            except ValueError:
                pass

    def print_grapf(self):
        for vertex  in self.gdict:
            print(vertex, ":", self.gdict[vertex])

    def BFS(self, init_vertex):
        # we que all the vertexed that were not checked and we visit them in the sequence of the edges from the initial vertex

        # we make a set of visited vertexes 
        visited = set()
        visited.add(init_vertex)
        # we make a queue, with which we start the traversal 
        queue = [init_vertex]
        # we while loop it till the queue is empty 
        while queue: 
            # we check with a for loop, if we visited a vertex and we queue the the ones not visited
            current_vertex = queue.pop(0)
            print(current_vertex)
            for adj_vertex in self.gdict[current_vertex]:
                if adj_vertex not in visited: 
                    visited.add(adj_vertex)
                    queue.append(adj_vertex)
            
custom_dict_graph = {
    'a':['b','c'],
    'b':['a','e','d'],
    'c':['a','e'],
    'd':['b','e','f'],
    'e':['c','b','d','f'],
    'f':['d','e']
}

dict_graph = Graph(custom_dict_graph)
dict_graph.addEdge('e','c')
#dict_graph.addEdge('g','m','k')
dict_graph.removeVertex('f')
dict_graph.print_grapf()
dict_graph.BFS('a')

