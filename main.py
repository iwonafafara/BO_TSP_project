import graph
from graph import Graph, EuclideanGraph, nearest_neighbour_algorithm, optimization_2_opt, optimization_2_opt_with_k_deterioration
from import_data import get_graph1, get_graph2, get_graph3, get_graph4, get_graph5, get_graph6, get_graph7
from plot import plot_graph
from timer import start_time, stop_time, measure_time


def basic_graph_example():
    g = Graph(8, {
        1: [[2, 2], [3, 2], [4, 4], [5, 3]],
        2: [[1, 2], [3, 2], [6, 1], [7, 1]],
        3: [[1, 2], [2, 2], [5, 2], [6, 1]],
        4: [[1, 4], [6, 2], [8, 3]],
        5: [[1, 3], [3, 2], [7, 4], [8, 5]],
        6: [[2, 1], [3, 1], [4, 2], [7, 2], [8, 2]],
        7: [[2, 1], [5, 4], [6, 2], [8, 2]],
        8: [[4, 3], [5, 5], [6, 2], [7, 2]]})
    print('Num of nodes: ', g.num_of_nodes)
    print('Visited: ', g.visited_nodes)
    print('Vertices: ')
    for node in g.paths:
        print('\t', node, ': ', g.paths[node])

    print(nearest_neighbour_algorithm(g))


def euclidean_graph_example():
    g = EuclideanGraph(5, {0: [4, 1], 1: [2, 1], 2: [1, 3], 3: [5, 3], 4: [3, 4]})
    print('Num of nodes: ', g.num_of_nodes)
    print('Nodes: ', g.nodes)
    print('Visited: ', g.visited_nodes)
    print('Vertices: ')
    for node in g.paths:
        print('\t', node, ': ', g.paths[node])

    print(nearest_neighbour_algorithm(g))


def tsplib_import_example():
    g = get_graph2()
    print(nearest_neighbour_algorithm(g))

    cycle = nearest_neighbour_algorithm(g)
    print(cycle)

    # plot_graph(g, cycle)
    timers = optimization_2_opt_with_k_deterioration(g, cycle, k=10, iterations_until_break_threshold=5)
    print(timers)


def old_opt_2():
    g = get_graph2()
    print(nearest_neighbour_algorithm(g))

    cycle = nearest_neighbour_algorithm(g)
    print(cycle)

    timers = optimization_2_opt(g, cycle, 5)
    print(timers)


if __name__ == '__main__':
    # basic_graph_example()
    # euclidean_graph_example()
    tsplib_import_example()
    old_opt_2()

