import pytest

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dijkstra_new_implement import Node, Dijkstra



@pytest.fixture
def basic_graph():
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

    return nodeA, nodeB, nodeC, nodeD

def test_shortest_distances(basic_graph):
    nodeA, nodeB, nodeC,  nodeD = basic_graph
    dijkstra = Dijkstra()
    assert dijkstra.calculate_shortest_path(nodeA,nodeB)[1] == 1
    assert dijkstra.calculate_shortest_path(nodeC,nodeD)[1] == 3
    assert dijkstra.calculate_shortest_path(nodeA,nodeD)[1] == 6

   
    
    
def test_single_node_graph():
    nodeA = Node('A')
    dijkstra = Dijkstra()
    min_distance = dijkstra.calculate_shortest_path(nodeA,nodeA)[1]
    assert min_distance == 0
    assert dijkstra.calculate_shortest_path(nodeA,nodeA)[0] == ['A']