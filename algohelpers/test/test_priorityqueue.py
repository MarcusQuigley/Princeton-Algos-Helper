import unittest
import algohelpers.priorityqueue
 
from algohelpers.priorityqueue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_create_priority_queue(self):
        pq = PriorityQueue()
        self.assertIsNotNone(pq)

    def test_enqueue(self):
        pq = PriorityQueue()
        pq.enqueue(4)
        pq.enqueue(2)
        pq.enqueue(3)
        expected = 3
        print(pq)
        self.assertEqual(expected, pq.count)

    def test_dequeue(self):
        pq = PriorityQueue()
        pq.enqueue(4)
        pq.enqueue(2)
        pq.dequeue()
        expected = 1
        print(pq)
        self.assertEqual(expected, pq.count)

    def test_priority(self):
        pq = PriorityQueue()
        pq.enqueue(4)
        pq.enqueue(2)
        pq.enqueue(3)
        expected = 2
        actual =  pq.dequeue()
        print(pq)
        self.assertEqual(expected, actual)

