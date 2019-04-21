import unittest

from algohelpers.maxheap import MaxHeap

class TestMaxHeap(unittest.TestCase):
    def test_create_maxheap(self):
        heap = MaxHeap()
        self.assertIsNotNone(heap)

    def test_add_to_maxheap(self):
        heap = MaxHeap()
        heap.insert(3)
        heap.insert(4)
        expected = 2
        self.assertEqual(expected, heap.count)

    def test_remove_from_maxheap(self):
        heap = MaxHeap()
        heap = MaxHeap()
        heap.insert(3)
        heap.insert(4)
        heap.insert(6)
        heap.insert(2)
        heap.insert(7)
        heap.insert(1)
        expected = 7
        self.assertEqual(expected, heap.remove())
