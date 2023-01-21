import math


# paths: {node_src: [[node_dest, weight], [node_dest, weight]]}
class Graph:
    def __init__(self, num_of_nodes: int, paths: dict):
        self.num_of_nodes = num_of_nodes
        self.paths = paths
        self.visited_nodes = [0 for i in range(0, num_of_nodes + 1)]

    def clear_visited_nodes(self):
        for node in self.visited_nodes:
            node = 0


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

    def set_weight(self, node1, node2, weight):
        def replace_weight(list, node, weight):
            for item in list:
                if node == item[0]:
                    item[1] = weight
                    break
        replace_weight(self.paths[node1], node2, weight)
        replace_weight(self.paths[node2], node1, weight)


def nearest_neighbour_algorithm(graph: Graph):
    def sorting_comparator(weight_record: []):
        return weight_record[1]

    def is_last_node_valid(node_id):
        last_node_neighbours = graph.paths[node_id]
        for neighbour in last_node_neighbours:
            if neighbour[0] == visited_list[0]:
                return True
        return False

    graph.clear_visited_nodes()

    # every node will be taken exactly once, so we are choosing node 1 to start hamiltionian cycle
    current_node_id = 1
    visited_list = [current_node_id]
    graph.visited_nodes[current_node_id] = 1

    while True:
        sorted_neighbours_list = sorted(graph.paths[current_node_id], key=sorting_comparator)
        old_node_id = current_node_id
        for candidate in sorted_neighbours_list:
            if graph.visited_nodes[candidate[0]] == 0:
                current_node_id = candidate[0]
                break

        if old_node_id == current_node_id:
            print("ERROR no possible exit from node ", current_node_id)
            break

        graph.visited_nodes[current_node_id] = 1
        visited_list.append(current_node_id)

        if len(visited_list) == graph.num_of_nodes:
            if is_last_node_valid(current_node_id):
                print("success - Hamiltonian cycle found")
                visited_list.append(visited_list[0])
            else:
                print("ERROR no Hamiltonian cycle")
            break

    return visited_list
