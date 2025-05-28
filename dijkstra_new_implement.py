import heapq

# class for an edge: 
class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node: 
    def __init__(self, name):
        self.name = name
        self.visited = False
        # previous node : 
        self.predecessor = None
        self.neighbors = []
    
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)

# Dijkstra algorithm
class Dijkstra:
    def __init__(self):
        self.heap = []
        self.distances = {}  

    def calculate(self, start_vertex: Node):
        self.heap = []
        self.distances = {}

        self._reset_nodes(start_vertex)
        
        self.distances[start_vertex] = 0
        heapq.heappush(self.heap, (0, start_vertex))  
        
        while self.heap:
            current_distance, actual_vertex = heapq.heappop(self.heap)
            
            if actual_vertex.visited:
                continue
                
            actual_vertex.visited = True
            
            for edge in actual_vertex.neighbors:
                target = edge.target_vertex
                new_distance = current_distance + edge.weight
                
                
                if target not in self.distances or new_distance < self.distances[target]:
                    self.distances[target] = new_distance
                    target.predecessor = actual_vertex
                    heapq.heappush(self.heap, (new_distance, target))


    def _reset_nodes(self, start_vertex):
        # Reset visited status and predecessors for all reachable nodes
        visited_nodes = set()
        stack = [start_vertex]
        
        while stack:
            node = stack.pop()
            if node not in visited_nodes:
                visited_nodes.add(node)
                node.visited = False
                node.predecessor = None
                
                for edge in node.neighbors:
                    if edge.target_vertex not in visited_nodes:
                        stack.append(edge.target_vertex)
    
    def calculate_shortest_path(self, start_vertex, end_vertex):
        self.calculate(start_vertex)
        vertex_list = []
        actual_vertex = end_vertex

        while actual_vertex is not None:
            vertex_list.append(actual_vertex)
            actual_vertex = actual_vertex.predecessor
        
        path = [v.name for v in reversed(vertex_list)]
        distance = self.distances.get(end_vertex, float('inf'))
        return path , distance
    

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')

nodeA.add_edge(1, nodeB)
nodeA.add_edge(10, nodeC)
nodeB.add_edge(2, nodeC)
nodeC.add_edge(10, nodeA)
nodeC.add_edge(3, nodeD)
nodeD.add_edge(3, nodeC)


algorithm = Dijkstra()
print(algorithm.calculate_shortest_path(nodeA, nodeC))