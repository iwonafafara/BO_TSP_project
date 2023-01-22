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
            for tuple in self.paths[source]:
                if tuple[0] == destination:
                    return tuple[1]

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


def optimization_2_opt(graph: Graph, path: list):
    best_cost = graph.calculate_cost(path)
    best_path = path
    for i in range(1, graph.num_of_nodes):
        for j in range(i + 2, graph.num_of_nodes):
            reversed_list = path[i:j]
            reversed_list.reverse()
            current_path = path[0:i] + reversed_list + path[j:]
            current_cost = graph.calculate_cost(current_path)
            if current_cost < best_cost:
                best_cost = current_cost
                best_path = current_path
    return {'cost': best_cost, 'path': best_path}


