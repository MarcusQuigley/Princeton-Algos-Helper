import algohelpers


from algohelpers.node import Node

class Bag(object):
  def __init__(self):
    self._head = None
    self._size = 0

  def __iter__(self):
    node = self._head
    while node is not None:
      yield node
      node = node.next_node

  @property
  def size(self):
    return self._size
  
  @property
  def isEmpty(self):
    return self._head is None

  def contains(self, item):
    node = self._head
    while node is not None:
      if node.value == item:
        return True
      node = node.next_node
    return False

  def addend(self, value):
    newnode = Node(value)
    if self._head is None:
      self._head = newnode
    else:
      node = self._head
      while node is not None:
        if node.next_node is None:
          node.next_node = newnode
          break
        node = node.next_node
    self._size += 1

  def addfirst(self, value):
    newnode = Node(value)
    if self._head is None:
      self._head = newnode
    else:
      tempnode = self._head
      newnode.next_node = tempnode
      self._head = newnode
    self._size += 1
    
  def __str__(self):
    str = f'size:{self.size}'
    count=1
    for node in self:
      str += f' {node.value}'
      if count == 3:
        break
      else:
        str += '->'
    return str


 
  
    
