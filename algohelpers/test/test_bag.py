import unittest
import algohelpers.bag

from algohelpers.bag import Bag

class TestBag(unittest.TestCase):
  def test_create_bag(self):
    bag = Bag()
    self.assertIsNotNone(bag)

  def test_bag(self):
    bag = Bag()
    self.assertTrue(bag.isEmpty)

  def test_add_works(self):
    bag = Bag()
    bag.addend('12')
    self.assertTrue(bag.size == 1)
    #self.assertFalse(bag.isEmpty

  def test_add__multiple_from_front_works(self):
    bag = Bag()
    for i in range(3):
      bag.addfirst(i)
    self.assertTrue(bag.size == 3)

  def test_add__multiple_works(self):
    bag = Bag()
    for i in range(3):
      bag.addend(i)
    self.assertTrue(bag.size == 3)

  def test_add__multiple_not_empty(self):
    bag = Bag()
    for i in range(3):
      bag.addfirst(i)
    self.assertFalse(bag.isEmpty)

  def test_add__multiple_contains_2(self):
    bag = Bag()
    for i in range(1,3):
      bag.addfirst(i)
    self.assertTrue(bag.contains(2))

  def test_add__multiple_doesnt_contain_5(self):
    bag = Bag()
    for i in range(1,3):
      bag.addfirst(i)
    self.assertFalse(bag.contains(5))

  def test_iterate_bag(self):
    bag = Bag()
    for i in range(2):
      bag.addend(i)
    temp = None#Node(12)
    for b in bag:
      temp = b
    self.assertEqual(1,temp.value)
    #self.assertIsNone(temp.next_node)
     