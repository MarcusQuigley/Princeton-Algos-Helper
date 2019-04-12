class Node(object):
  def __init__(self, value):
    self._value = value
    self._next_node = None
  
  @property
  def value(self):
    return self._value
  
  # @value.setter
  # def value(self, value):
  #   self._value = value
   
  @property
  def next_node(self):
    return self._next_node
  
  @next_node.setter
  def next_node(self, node):
    self._next_node = node
