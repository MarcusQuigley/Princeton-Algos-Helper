import algohelpers.bag
from algohelpers.bag import Bag

class Graph(object):
  def __init__(self, graph = None,  vertex = 0,inputstream = None):
    if (vertex == 0 and graph is None and inputstream is None):
      raise ValueError('Graph constructor must have at least 1 input')
    
    if graph is not None:
      self.__init_graph(graph)
    elif inputstream is not None:
      self.__init_stream(graph)
    else:
      self.__init_vertex(vertex)
      

  def __init_vertex(self, vertex):
    if (vertex < 0): 
        raise ValueError('Number of vertices must be nonnegative')
    self.__edge = 0
    self.__vertex = vertex
    self.__adjacent = [0] * vertex
    self.__populate_adjacents(vertex)

  def __init_graph(self, graph):
    self.__init_vertex(graph.vertex)
    self.__edge = graph.edge
    for v in range(graph.vertex):
      stack = []
      for w in graph.__adjacent[v]:
        stack.append(w)
      for ww in stack:
        self.__adjacent.addfirst(w)

  def __init_stream(self, input):
    return 2

  def __populate_adjacents(self, vertex):
    for i in range(vertex):
      self.__adjacent[i] = Bag()

  @property
  def edge(self):
    return self.__edge

  @property
  def vertex(self):
    return self.__vertex

  def __validate_vertex(self,v):
    if v < 0 or v >= self.__vertex:
      raise ValueError(v, ' was outside the range')

  def add_edge(self, v, w):
    self.__validate_vertex(v)
    self.__validate_vertex(w)
    self.__edge+=1
    self.__adjacent[v].addfirst(w)
    self.__adjacent[w].addfirst(v)

  def degree(self, v):
    self.__validate_vertex(v)
    return self.__adjacent[v].size

  def adjacent_vertices(self, v):
    self.__validate_vertex(v)
    return self.__adjacent[v]

  def __str__(self):
    #str = ''
    str = f'{self.vertex} vertices, {self.edge} edges.\n'
    #str += self.vertex + ' vertices, ' +  self.edge + ' edges. \n'
    for v in range(self.vertex):
      str += f' {v}: '
      for w in self.__adjacent[v]:
        str += f'   print{w.value} '
      str += '\n'
    return str


    
