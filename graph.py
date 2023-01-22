import math


# paths: {node_src: [[node_dest, weight], [node_dest, weight]]}
class Graph:
    def __init__(self, num_of_nodes: int, paths={}):
        self.num_of_nodes = num_of_nodes
        self.paths = paths
        self.visited_nodes = [0 for i in range(0, num_of_nodes + 1)]

    def clear_visited_nodes(self):
        for i in range(len(self.visited_nodes)):
            self.visited_nodes[i] = 0

    def set_weight(self, node1, node2, weight):
        def replace_weight(list, node, weight):
            for item in list:
                if node == item[0]:
                    item[1] = weight
                    break

        if not self.paths:
            self.initialize_empty_paths()

        replace_weight(self.paths[node1], node2, weight)
        replace_weight(self.paths[node2], node1, weight)

    def initialize_empty_paths(self):
        for nodeId in range(1, self.num_of_nodes + 1):
            self.paths[nodeId] = []
            for nodeId2 in range(1, self.num_of_nodes + 1):
                if not nodeId == nodeId2:
                    self.paths[nodeId].append([nodeId2, 0])

    def calculate_cost(self, path: list):
        def find_weight(source, destination):
            for pair in self.paths[source]:
                if pair[0] == destination:
                    return pair[1]

        cost = 0
        for i in range(self.num_of_nodes):
            cost += find_weight(path[i], path[i + 1])
        return cost


# nodes: {nodeId: [x, y]}
class EuclideanGraph(Graph):
    def __init__(self, num_of_nodes: int, nodes: dict):
        super().__init__(num_of_nodes, {})
        self.nodes = nodes
        self.generate_paths(nodes)

    def generate_paths(self, nodes: dict):
        def dist(a, b):
            return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

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
