# coding=cp1251

# Python program for Bellman-Ford's single source
# shortest path algorithm.

from collections import defaultdict


# Class to represent a graph
class Graph:

    def __init__(self):
    # def __init__(self, vertices):
        self.V = 0  # No. of vertices
        self.graph = []  # default dictionary to store graph
        self.predecessor = [-1]

    def set_num_vertices(self, vertices):
        self.V = vertices
        self.predecessor = [-1] * vertices

    # function to add an edge to graph
    def addEdge(self, u, v, w, a):
        self.graph.append([u, v, w, a])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(i, dist[i])

        # The main function that finds shortest distances from src to

    def reset_map(self):
        self.graph = []

    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):

        self.predecessor = [-1] * self.V
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for i in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w, a in self.graph:
                if a == 1:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        self.predecessor[v] = u

                # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w, a in self.graph:
            if a == 1:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    print("Graph contains negative weight cycle")
                    return

        # print all distance
        # self.printArr(dist)
        # print(self.predecessor)
        return [self.predecessor, dist]


def main():
    # Граф для тестов
    g = Graph()
    g.set_num_vertices(4)
    g.addEdge(0, 1, 8, 1)
    g.addEdge(1, 2, 5, 1)
    g.addEdge(2, 3, 8, 1)
    g.addEdge(2, 0, 9, 1)
    g.addEdge(3, 0, 5, 1)

    # Print the solution
    print(g.BellmanFord(0))


if __name__ == '__main__':
    main()


# This code is contributed by Neelam Yadav
