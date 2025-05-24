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
        self.min_distance = float('inf')
    
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)

# Dijkstra algorithm
class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex: Node):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # pop element with lowest distance 
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance: 
                    target.min_distance = new_distance
                    target.predecessor = start
                    # update the heap 
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True
    
    def get_shortest_path(self, vertex):
        print(f"Shortest path : {vertex.min_distance}")
        vertex_list = []
        actual_vertex = vertex
        while actual_vertex is not None:
            # print(actual_vertex.name, end = " ")
            vertex_list.append(actual_vertex)
            actual_vertex = actual_vertex.predecessor
            path = [v.name for v in reversed(vertex_list)]
        return  path 


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
algorithm.calculate(nodeA)
print(algorithm.get_shortest_path(nodeC))