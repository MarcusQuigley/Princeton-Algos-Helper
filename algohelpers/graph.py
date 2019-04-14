import io
import sys
import algohelpers.bag
from algohelpers.bag import Bag

class Graph(object):
  def __init__(self, graph = None,  vertices = 0,inputstream = None):
    if (vertices == 0 and graph is None and inputstream is None):
      raise ValueError('Graph constructor must have at least 1 input')
    
    if graph is not None:
      self.__init_graph(graph)
    elif inputstream is not None:
      self.__init_stream(inputstream)
    else:
      self.__init_vertex(vertices)

  def __init_vertex(self, vertices):
    if (vertices < 0): 
        raise ValueError('Number of vertices must be nonnegative')
    self.__edges = 0
    self.__vertices = vertices
    self.__adjacent = [0] * vertices
    self.__populate_adjacents(vertices)

  def __init_graph(self, graph):
    self.__init_vertex(graph.vertices)
    self.__edges = graph.edges
    for v in range(graph.vertices):
      stack = []
      for w in graph.__adjacent[v]:
        stack.append(w)
      for ww in stack:
        self.__adjacent.addfirst(w)

  def __init_stream(self, input):
    if (input is None):
      raise ValueError('input is none')
    try:
      inputdata = input.read().splitlines()
      self.__vertices =  int(inputdata.pop(0))
      if self.__vertices < 0:
        raise ValueError('Number of vertices must be nonnegative')
      self.__adjacent = [0] * self.__vertices
      self.__populate_adjacents(self.__vertices)
      self.__edges = int(inputdata.pop(0))
      if self.__edges < 0:
        raise ValueError('Number of edges must be nonnegative')
      for i in range(self.__edges):
        vertices = inputdata.pop(0).split(' ')
        v = int(vertices.pop(0))
        w = int(vertices.pop(0))
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        self.add_edge(v,w)
    except IOError as error:
      print(f'ioerror: {error}')
    except ValueError as error:
      print(f'valueerror: {error}')
    except BaseException as error:
      print(f'Unexpected error: {error}')
    

  def __populate_adjacents(self, vertices):
    for i in range(vertices):
      self.__adjacent[i] = Bag()

  @property
  def edges(self):
    return self.__edges

  @property
  def vertices(self):
    return self.__vertices

  def __validate_vertex(self,vertex):
    if vertex < 0 or vertex >= self.__vertices:
      raise ValueError(vertex, ' was outside the range')

  def add_edge(self, vertex, w):
    self.__validate_vertex(vertex)
    self.__validate_vertex(w)
    self.__edges+=1
    self.__adjacent[vertex].addfirst(w)
    self.__adjacent[w].addfirst(vertex)

  def degree(self, vertex):
    self.__validate_vertex(vertex)
    return self.__adjacent[vertex].size

  def adjacent_vertices(self, vertex):
    self.__validate_vertex(vertex)
    return self.__adjacent[vertex]

  def __str__(self):
    #str = ''
    str = f'{self.vertices} vertices, {self.edges} edges.\n'
    #str += self.vertex + ' vertices, ' +  self.edge + ' edges. \n'
    for vertex in range(self.vertices):
      str += f' {vertex}: '
      for w in self.__adjacent[vertex]:
        str += f'   print{w.value} '
      str += '\n'
    return str


    
