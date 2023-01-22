import math
from timer import start_time, stop_time, measure_time


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


def get_2_opt_reversed_path(path, i, j):
    reversed_list = path[i:j]
    reversed_list.reverse()
    return path[0:i] + reversed_list + path[j:]


def get_indekses_for_2_opt(size):
    return ((i, j)
            for i in range(1, size)
            for j in range(i + 2, size))


def optimization_2_opt(graph: Graph, cycle: list, iterations_until_break_threshold=10):
    old_cost = -1
    iterations_until_break = iterations_until_break_threshold

    times = []
    start_time()
    while iterations_until_break:
        returned_dict = optimization_2_opt_worker(graph, cycle)
        print(returned_dict)
        cycle = returned_dict['path']

        if old_cost == returned_dict['cost']:   # ToDo Fix this comparison of floats
            iterations_until_break -= 1
        else:
            old_cost = returned_dict['cost']
            iterations_until_break = iterations_until_break_threshold
        times.append(measure_time())
    return times


def optimization_2_opt_worker(graph: Graph, path: list):
    best_cost = graph.calculate_cost(path)
    best_path = path
    for i, j in get_indekses_for_2_opt(graph.num_of_nodes):
        current_path = get_2_opt_reversed_path(path, i, j)
        current_cost = graph.calculate_cost(current_path)
        if current_cost < best_cost:
            best_cost = current_cost
            best_path = current_path
    return {'cost': best_cost, 'path': best_path}


def optimization_2_opt_with_k_deterioration(graph: Graph, cycle: list, k: int, iterations_until_break_threshold=10):
    returned = {'cost': [0], 'path': [cycle]}
    old_cost = -1
    iterations_until_break = iterations_until_break_threshold

    times = []
    start_time()
    while iterations_until_break:
        temp_ret = {'cost': [], 'path': []}
        for path in returned['path']:
            temp = optimization_2_opt_with_k_deterioration_worker(graph, path, k)
            temp_ret['cost'] = temp_ret['cost'] + temp['cost']
            temp_ret['path'] = temp_ret['path'] + temp['path']

        # Choose k-best paths and values to start calculations in next iteration
        returned['cost'] = []
        returned['path'] = []
        for x in range(k):
            if len(temp_ret['cost']) > 0:
                min_cost = min(temp_ret['cost'])
                index = temp_ret['cost'].index(min_cost)
                if min_cost not in returned['cost']:
                    returned['cost'].append(temp_ret['cost'][index])
                    returned['path'].append(temp_ret['path'][index])
                temp_ret['cost'].remove(temp_ret['cost'][index])
                temp_ret['path'].remove(temp_ret['path'][index])

        print('Min cost: ', min(returned['cost']), ' len: ', len(returned['cost']), ' returned: ', returned)
        if old_cost == min(returned['cost']):   # ToDo Fix this comparison of floats
            iterations_until_break -= 1
        else:
            old_cost = min(returned['cost'])
            iterations_until_break = iterations_until_break_threshold
        times.append(measure_time())
    return times


def optimization_2_opt_with_k_deterioration_worker(graph: Graph, path: list, considered_items_no=3):
    def update_paths(given_costs, given_paths, new_cost, new_path):
        if len(given_costs) < considered_items_no:
            given_costs.append(new_cost)
            given_paths.append(new_path)
        else:
            max_old_cost = max(given_costs)
            if max_old_cost > new_cost:
                index = given_costs.index(max_old_cost)
                given_costs.insert(index, new_cost)
                given_paths.insert(index, new_path)
        return given_costs, given_paths

    best_costs = [graph.calculate_cost(path)]
    best_paths = [path]
    for i, j in get_indekses_for_2_opt(graph.num_of_nodes):
        current_path = get_2_opt_reversed_path(path, i, j)
        current_cost = graph.calculate_cost(current_path)
        best_costs, best_paths = update_paths(best_costs, best_paths, current_cost, current_path)

    return {'cost': best_costs, 'path': best_paths}
