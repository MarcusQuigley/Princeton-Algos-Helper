import unittest
import algohelpers.graph
import algohelpers.bag

from algohelpers.graph import Graph

from algohelpers.bag import Bag

class TestGraph(unittest.TestCase):
  def test_create_graph_with_vertex(self):
    graph = Graph(None,5)
    self.assertIsNotNone(graph)

  def test_create_graph_with_graph(self):
    graph = Graph(None,5)
    newgraph = Graph(graph)
    self.assertIsNotNone(graph)

  def test_create_graph_with_negative(self):
    self.assertRaises(ValueError, Graph,-5)  

  def test_get_vertex(self):
    expected = 3
    graph = Graph(None, expected)
    self.assertEqual(expected,graph.vertex)

  #this tests both get edge and validate vertex
  def test_add_valid_edge(self):
    expected_edge = 1
    graph = Graph(None, 3)
    graph.add_edge(1,2)
    self.assertEqual(expected_edge,graph.edge)

  def test_add_invalid_edge(self):
    graph = Graph(None, 3)
    self.assertRaises(ValueError, graph.add_edge,1,5)   

  def test_degree(self):
    graph = self._create_graph()
    expected = 3
    self.assertEqual(expected, graph.degree(1))

  #@unittest.skip('skipping as I cant test bag contents')
  def test_adjacent_vertices(self):
    graph = self._create_graph()
    
    expected = Bag()
    expected.addend(3)
    expected.addend(2)
    expected.addend(2)

    list_expected = []
    list_actual = []
    actual = graph.adjacent_vertices(1)
    for n in expected: #range(expected.size)
      list_expected.append(n.value)
    for n in actual: #range(expected.size)
      list_actual.append(n.value)
    
    self.assertCountEqual(list_expected, list_actual)

  def test_string_returned(self):
    expected = self._create_graph()
    xx = expected.__str__()
    self.assertIsNotNone(expected.__str__())


  def _create_graph(self):
    graph = Graph(None, 4)
    graph.add_edge(1,3)
    graph.add_edge(1,2)
    graph.add_edge(2,1)
    return graph

  


  
  if __name__ == '__main__':
    unittest.main()