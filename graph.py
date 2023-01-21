import math


# paths: {node_src: [[node_dest, weight], [node_dest, weight]]}
class Graph:
    def __init__(self, num_of_nodes: int, paths: dict):
        self.num_of_nodes = num_of_nodes
        self.paths = paths
        self.visited_nodes = [0 for i in range(0, num_of_nodes)]


def dist(a, b):
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


# nodes: {nodeId: [x, y]}
class EuclideanGraph:
    def __init__(self, num_of_nodes: int, nodes: dict):
        self.num_of_nodes = num_of_nodes
        self.nodes = nodes
        self.paths = {}
        self.generate_paths(nodes)
        self.visited_nodes = [0 for i in range(0, num_of_nodes)]

    def generate_paths(self, nodes: dict):
        for nodeId in nodes:
            if not self.paths.get(nodeId):
                self.paths[nodeId] = []
            for nodeId2 in nodes:
                if not self.paths.get(nodeId2):
                    self.paths[nodeId2] = []
                if nodeId == nodeId2:
                    continue
                distance = dist(nodes[nodeId], nodes[nodeId2])
                self.paths[nodeId].append([nodeId2, distance])
