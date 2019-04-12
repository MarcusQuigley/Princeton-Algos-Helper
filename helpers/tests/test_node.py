import unittest
import helpers.node
#from helpers import node
#import helpers.node
#from helpers import node
from helpers.node import Node
#@unittest.skip('skipping to get Bag working')
class TestNode(unittest.TestCase):
  def test_create_node(self):
    node = Node(123)
    self.assertIsNotNone(node)

  def test_has_value(self):
    expected = 123
    node = Node(expected)
    self.assertEqual(expected,node.value)

  def test_has_node_value(self):
    expected = Node(456)
    node = Node(123)
    node.next_node = expected
    self.assertEqual(expected.value,node.next_node.value)
