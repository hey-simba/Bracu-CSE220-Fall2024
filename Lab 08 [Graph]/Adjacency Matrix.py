

import numpy as np

class AdjacencyMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = np.zeros((vertices, vertices), dtype=int)

    def add_weighted_edge(self, u, v, w=1):

        self.graph[u][v] = w

    def display(self):

        print("Adjacency Matrix:")
        print(self.graph)


    #Task 1
    def max_degree(self,matrix):

        max = 0

        for i in range(self.vertices):
            degree = 0
            for j in range(self.vertices):
                if self.graph[i][j]>0:
                  degree += self.graph[i][j]
            if degree > max:
                max= degree
        return max

    #Task 2
    def sum(self,matrix):
        max_sum = 0
        vertex = 0


        for i in range(self.vertices):
            edge_sum = 0
            for j in range(self.vertices):
                edge_sum += self.graph[i][j]
            if edge_sum > max_sum:
                max_sum = edge_sum
                vertex = i

        return vertex, max_sum

    #Task 3
    def max_degree_task3(self,matrix):
        max_degree = 0
        for i in range(self.vertices):
            degree = 0
            for j in range(self.vertices):
                if self.graph[i][j] > 0:
                    degree += 1
            if degree > max_degree:
                max_degree = degree
        return max_degree

    #Task 4
    def convert_to_undirected(self,matrix):
      undirected_graph = np.zeros((self.vertices, self.vertices), dtype=int)
      for i in range(self.vertices):
        for j in range(self.vertices):
            if self.graph[i][j] > 0:
                undirected_graph[i][j] = self.graph[i][j]
                undirected_graph[j][i] = self.graph[i][j]


      return undirected_graph


# Task 1
vertices = 7
graph = AdjacencyMatrix(vertices)
edges = [
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 6),
    (1, 0), (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 0), (2, 1), (2, 4), (2, 6),
    (3, 0), (3, 1), (3, 4), (3, 5),
    (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6),
    (5, 1), (5, 3), (5, 4), (5, 6),
    (6, 0), (6, 2), (6, 4), (6, 5),
]
for edge in edges:
    graph.add_weighted_edge(edge[0], edge[1])
graph.display()
max_deg = graph.max_degree(graph)
print("The maximum degree is:", max_deg)



#Task 2
vertices = 7
graph_2 = AdjacencyMatrix(vertices)

edges_2 = [
    (0, 1, 3), (0, 2, 5), (0, 3, 7), (0, 4, 2), (0, 6, 6),
    (1, 0, 3), (1, 2, 4), (1, 3, 8), (1, 4, 1), (1, 5, 3),
    (2, 0, 5), (2, 1, 4), (2, 4, 6), (2, 6, 9),
    (3, 0, 7), (3, 1, 8), (3, 4, 3), (3, 5, 4),
    (4, 0, 2), (4, 1, 1), (4, 2, 6), (4, 3, 3), (4, 5, 7), (4, 6, 5),
    (5, 1, 3), (5, 3, 4), (5, 4, 7), (5, 6, 8),
    (6, 0, 6), (6, 2, 9), (6, 4, 5), (6, 5, 8)
]


for edge in edges_2:
    graph_2.add_weighted_edge(edge[0], edge[1], edge[2])

graph_2.display()

vertex, max_sum = graph_2.sum(graph_2)
print(f"The vertex with the maximum sum of edge weights is: {vertex} with a sum of {max_sum}")


#Task 3
vertices = 7
graph_3= AdjacencyMatrix(vertices)

edges_3 = [
    (0, 1, 3), (0, 2, 5), (0, 3, 7), (0, 4, 2), (0, 6, 6),
    (1, 2, 4), (1, 3, 8), (1, 4, 1), (1, 5, 3),
    (2, 4, 6), (2, 6, 9),
    (3, 4, 3), (3, 5, 4),
    (4, 5, 7), (4, 6, 5),
    (5, 6, 8)
]

for edge in edges_3:
    graph_3.add_weighted_edge(edge[0], edge[1], edge[2])

graph_3.display()
max = graph_3.max_degree_task3(graph)
print("The maximum degree is:", max)

ver, sum = graph_3.sum(graph_3)
print(f"The vertex with the maximum sum of edge weights is: {ver} with a sum of {sum}")

#Task 4
new= graph_3.convert_to_undirected(graph_3)
print(new)