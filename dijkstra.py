from heapq import *

class Node:
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return self.key
    
    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        return other.key == self.key

    def __lt__(self, other):
        return self.key > other.key 


# graph is an adjacency matrix
class Graph:
    def __init__(self, graph):
        self.graph = graph

    def __iter__(self):
        for v in self.graph:
            yield v

    def __getitem__(self, key):
        return self.graph[key]

        
class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def reset(self, start):
        self.distMatrix = self.init_dist(self.graph, start)
        self.pq = self.init_pq(self.distMatrix)

    def init_dist(self, graph, start):
        import sys
        res =  {v: sys.maxsize for v in graph}
        res[start] = 0
        return res
        
    def init_pq(self, distMatrix):
        pq = []
        for vertex, dist in distMatrix.items():
            heappush(pq, (dist, vertex))
        return pq
    
    def decreasePriority(self, pq, vertex, dist):
        # TODO: Optimize the following heap implementation
        entries = [i for i in pq if i[1] == vertex]
        if not entries: return 
        pq.remove(entries[0])
        heapify(pq)
        heappush(pq, (dist, vertex))
    
    def run(self, start, final):
        self.reset(start)
        while self.pq:
            curdist, vertex = heappop(self.pq)
            if vertex == final: return self.distMatrix[final]
            for neighbor, d in self.graph[vertex].items():
                if self.distMatrix[vertex] + d < self.distMatrix[neighbor]:
                    self.distMatrix[neighbor] = self.distMatrix[vertex] + d
                    self.decreasePriority(
                            self.pq, neighbor, self.distMatrix[neighbor])
        return -1


g = Graph({
    Node('A'): dict([(Node('B'), 3), (Node('C'), 6)]),
    Node('B'): dict([(Node('D'), 4), (Node('E'), 10)]),
    Node('C'): dict([(Node('D'), 2)]),
    Node('D'): {Node('E'): 5},
    Node('E'): {}
})

d = Dijkstra(g)
res = d.run(Node('A'), Node('E'))
print(res)
