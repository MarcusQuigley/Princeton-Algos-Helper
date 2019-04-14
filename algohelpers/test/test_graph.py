import io
import os
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

  def test_create_graph_with_stream(self):
    try:
      TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'tiny_graph_data.txt')
      data = open(TESTDATA_FILENAME, 'r')

      graph = Graph(None,0, data)
      self.assertTrue(graph.edges>0)
    except Exception as e:
      print(e)
    finally:
      if data:
        data.close()

  def test_create_graph_with_badstream(self):
    try:
      # TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'tiny_graph_data.txt')
      # data = open(TESTDATA_FILENAME, 'r')
      data = io.StringIO('some random data')

      graph = Graph(None,0, data)
      self.assertTrue( graph.edges == 0)
    except Exception as e:
      print(e)
    finally:
      if data:
        data.close()


  def test_create_graph_with_negative(self):
    self.assertRaises(ValueError, None,-5)  

  def test_get_vertex(self):
    expected = 3
    graph = Graph(None, expected)
    self.assertEqual(expected,graph.vertices)

  #this tests both get edges and validate vertices
  def test_add_valid_edges(self):
    expected_edges = 1
    graph = Graph(None, 3)
    graph.add_edge(1,2)
    self.assertEqual(expected_edges,graph.edges)

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
    self.assertTrue(len(expected.__str__()) > 0)


  def _create_graph(self):
    graph = Graph(None, 4)
    graph.add_edge(1,3)
    graph.add_edge(1,2)
    graph.add_edge(2,1)
    return graph

  


  
  if __name__ == '__main__':
    unittest.main()