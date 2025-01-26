

class Node:
  def __init__(self, vertex, weight = None):
    self.vertex = vertex
    self.weight = weight
    self.next = None

import numpy as np

class Node:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight
        self.next = None

class AdjacencyList:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = np.array([None] * vertices)

    def create_graph(self, u, v, w=None):
        if w is None:
            n = Node(v)
        else:
            n = Node(v, w)

        if self.graph[u] is None:
            self.graph[u] = n
        else:
            current = self.graph[u]
            while current.next is not None:
                current = current.next
            current.next = n

    def max_degree(self):
        max_degree = 0
        for i in range(self.vertices):
            count = 0
            current = self.graph[i]
            while current:
                count += 1
                current = current.next
            if count > max_degree:
                max_degree = count
        return max_degree

    def sum(self):
        max_val = 0
        max_sum = 0
        for i in range(self.vertices):
            sum_weight = 0
            current = self.graph[i]
            while current:
                if current.weight is not None:
                    sum_weight += current.weight
                current = current.next
            if sum_weight > max_sum:
                max_sum = sum_weight
                max_val = i
        return max_sum, max_val

    #Task 3
    def max_degree_3(self):
        max_degree = 0
        for i in range(self.vertices):
            count = 0
            current = self.graph[i]
            while current:
                count += 1
                current = current.next
            if count > max_degree:
                max_degree = count
        return max_degree
    def sum_3(self):
        max_sum = 0
        max_val = -1
        for i in range(self.vertices):
            sum_weight = 0
            current = self.graph[i]
            while current:
                if current.weight is not None:
                    sum_weight += current.weight
                current = current.next
            if sum_weight > max_sum:
                max_sum = sum_weight
                max_val = i
        return max_val, max_sum

# Task 1
adj_list = AdjacencyList(7)

adj_list.create_graph(0, 1)
adj_list.create_graph(0, 2)
adj_list.create_graph(0, 3)
adj_list.create_graph(0, 4)
adj_list.create_graph(0, 6)
adj_list.create_graph(1, 0)
adj_list.create_graph(1, 2)
adj_list.create_graph(1, 3)
adj_list.create_graph(1, 4)
adj_list.create_graph(1, 5)
adj_list.create_graph(2, 0)
adj_list.create_graph(2, 1)
adj_list.create_graph(2, 4)
adj_list.create_graph(2, 6)
adj_list.create_graph(3, 0)
adj_list.create_graph(3, 1)
adj_list.create_graph(3, 4)
adj_list.create_graph(3, 5)
adj_list.create_graph(4, 0)
adj_list.create_graph(4, 1)
adj_list.create_graph(4, 2)
adj_list.create_graph(4, 3)
adj_list.create_graph(4, 5)
adj_list.create_graph(4, 6)
adj_list.create_graph(5, 1)
adj_list.create_graph(5, 3)
adj_list.create_graph(5, 4)
adj_list.create_graph(5, 6)
adj_list.create_graph(6, 0)
adj_list.create_graph(6, 2)
adj_list.create_graph(6, 4)
adj_list.create_graph(6, 5)




max_deg = adj_list.max_degree()
print(f"The maximum degree is: {max_deg}")


#Task 2
adj_list_2 = AdjacencyList(7)

adj_list_2.create_graph(0, 1, 3)
adj_list_2.create_graph(0, 2, 5)
adj_list_2.create_graph(0, 3, 7)
adj_list_2.create_graph(0, 4, 2)
adj_list_2.create_graph(0, 6, 6)
adj_list_2.create_graph(1, 0, 3)
adj_list_2.create_graph(1, 2, 4)
adj_list_2.create_graph(1, 3, 8)
adj_list_2.create_graph(1, 4, 1)
adj_list_2.create_graph(1, 5, 3)
adj_list_2.create_graph(2, 0, 5)
adj_list_2.create_graph(2, 1, 4)
adj_list_2.create_graph(2, 4, 6)
adj_list_2.create_graph(2, 6, 9)
adj_list_2.create_graph(3, 0, 7)
adj_list_2.create_graph(3, 1, 8)
adj_list_2.create_graph(3, 4, 3)
adj_list_2.create_graph(3, 5, 4)
adj_list_2.create_graph(4, 0, 2)
adj_list_2.create_graph(4, 1, 1)
adj_list_2.create_graph(4, 2, 6)
adj_list_2.create_graph(4, 3, 3)
adj_list_2.create_graph(4, 5, 7)
adj_list_2.create_graph(4, 6, 5)
adj_list_2.create_graph(5, 1, 3)
adj_list_2.create_graph(5, 3, 4)
adj_list_2.create_graph(5, 4, 7)
adj_list_2.create_graph(5, 6, 8)
adj_list_2.create_graph(6, 0, 6)
adj_list_2.create_graph(6, 2, 9)
adj_list_2.create_graph(6, 4, 5)
adj_list_2.create_graph(6, 5, 8)



vertex, max_sum = adj_list_2.sum()
print(f"The vertex with the maximum sum of edge weights is: {vertex} with a sum of {max_sum}")


# Task 3
adj_list_3 = AdjacencyList(7)

adj_list_3.create_graph(0, 1, 3)
adj_list_3.create_graph(0, 2, 5)
adj_list_3.create_graph(0, 3, 7)
adj_list_3.create_graph(0, 4, 2)
adj_list_3.create_graph(0, 6, 6)
adj_list_3.create_graph(1, 2, 4)
adj_list_3.create_graph(1, 3, 8)
adj_list_3.create_graph(1, 4, 1)
adj_list_3.create_graph(1, 5, 3)
adj_list_3.create_graph(2, 4, 6)
adj_list_3.create_graph(2, 6, 9)
adj_list_3.create_graph(3, 4, 3)
adj_list_3.create_graph(3, 5, 4)
adj_list_3.create_graph(4, 5, 7)
adj_list_3.create_graph(4, 6, 5)
adj_list_3.create_graph(5, 6, 8)

max_deg = adj_list.max_degree_3()
print(f"The maximum degree (outgoing) is: {max_deg}")
vertex, max_sum = adj_list_3.sum_3()
print(f"The vertex with the maximum sum of outgoing edge weights is: {vertex} with a sum of {max_sum}")