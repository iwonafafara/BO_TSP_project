from graph import Graph, EuclideanGraph
from timer import start_time, measure_time
from plot import plot_graph
import numpy as np


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

    plot_graph(graph, cycle,
               'Wykres grafu przed optymalizacją 2-opt bez pogorszenia, \n nodes = ' + str(graph.num_of_nodes),
               'graf_przed_optymalizacja_2_opt_bez_pogorszenia_' + str(graph.num_of_nodes) + 'wierzcholkow')
    iteration_no = 0
    times = []
    start_time()
    while iterations_until_break:
        returned_dict = optimization_2_opt_worker(graph, cycle)
        print(returned_dict)
        cycle = returned_dict['path']
        iteration_no += 1
        plot_graph(graph, cycle,
                   'Wykres grafu w trakcie optymalizacji ścieżki 2-opt bez pogorszenia, \n nodes = ' + str(
                       graph.num_of_nodes) + ' Iteracja: ' + str(iteration_no),
                   'graf_w_trakcie_optymalizacji_2_opt_bez_pogorszenia_' + str(
                       graph.num_of_nodes) + 'wierzcholkow_' + str(iteration_no))

        if abs(old_cost - returned_dict['cost']) < np.finfo(float).eps:
            iterations_until_break -= 1
        else:
            old_cost = returned_dict['cost']
            iterations_until_break = iterations_until_break_threshold
        times.append(measure_time())

    plot_graph(graph, cycle,
               'Graf zoptymalizowany metodą 2-opt bez pogorszenia dla ' + str(
                   graph.num_of_nodes) + ' węzłów. \n Po: ' + str(iteration_no) + ' iteracjach.',
               'graf_po_optymalizacji_2_opt_bez_pogorszenia_' + str(graph.num_of_nodes) + 'wierzcholkow')
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

    plot_graph(graph, cycle,
               'Wykres grafu przed optymalizacją 2-opt z pogorszeniem, \n nodes = ' + str(graph.num_of_nodes),
               'graf_przed_optymalizacja_2_opt_z_pogorszeniem_' + str(graph.num_of_nodes) + 'wierzcholkow')
    iterations_no = 0
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
        if abs(old_cost - min(returned['cost'])) < np.finfo(float).eps:
            iterations_until_break -= 1
        else:
            old_cost = min(returned['cost'])
            iterations_until_break = iterations_until_break_threshold
        times.append(measure_time())
        iterations_no += 1

    min_cost = min(returned['cost'])
    index = returned['cost'].index(min_cost)
    end_cycle = returned['path'][index]

    plot_graph(graph, end_cycle,
               'Graf zoptymalizowany metodą 2-opt z pogorszeniem dla ' + str(
                   graph.num_of_nodes) + ' węzłów. \n Po: ' + str(iterations_no) + ' iteracjach.',
               'graf_po_optymalizacji_2_opt_z_pogorszeniem_' + str(graph.num_of_nodes) + 'wierzcholkow')
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
