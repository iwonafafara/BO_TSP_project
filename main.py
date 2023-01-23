import graph
from graph import Graph, EuclideanGraph
from algos import nearest_neighbour_algorithm, optimization_2_opt, optimization_2_opt_with_k_deterioration
from import_data import get_graph1, get_graph2, get_graph3, get_graph4, get_graph5, get_graph6, get_graph7
from plot import plot_graph, plot_iterations_to_k, plot_cost_to_k, plot_time_per_iteration, plot_iterations_to_graph_size
from timer import start_time, stop_time, measure_time


def tsplib_import_example():
    g = get_graph3()
    print(nearest_neighbour_algorithm(g))

    cycle = nearest_neighbour_algorithm(g)
    print(cycle)

    timers = optimization_2_opt_with_k_deterioration(g, cycle, k=10, iterations_until_break_threshold=5)
    print(timers)


def old_opt_2():
    g = get_graph3()
    print(nearest_neighbour_algorithm(g))

    cycle = nearest_neighbour_algorithm(g)
    print(cycle)

    timers = optimization_2_opt(g, cycle, 5)
    print(timers)


def compare_costs_and_times_on_different_graphs():
    def test_graph(g: Graph):
        k = 5
        first_cycle = nearest_neighbour_algorithm(g)
        timers, min_cost, iterations = optimization_2_opt(g, first_cycle, 5)
        timers_k, min_cost_k, iterations_k  = optimization_2_opt_with_k_deterioration(g, first_cycle, k, iterations_until_break_threshold=5)
        print('Graph with ', g.num_of_nodes, ' nodes, optimal solution: ', g.optimal_solution)
        print('Algorithm without deterioration: ')
        print('Min_cost: ', min_cost, ' Iterations: ', iterations, f' Total time: {sum(timers):.03f}ms')
        print('Times: ', timers)
        print('Algorithm with ', k, ' deterioration: ')
        print('Min_cost: ', min_cost_k, ' Iterations: ', iterations_k, f' Total time: {sum(timers_k):.03f}ms')
        print('Times: ', timers_k)
        print('\n\n\n')
        # plot_time_per_iteration(timers, timers_k, k, g.num_of_nodes)
        return g.num_of_nodes, iterations, iterations_k

    graphs_to_test = [get_graph1(), get_graph3(), get_graph4(), get_graph7(), get_graph6()]
    graph_size = []
    iterations_list = []
    iterations_k_list = []
    for g in graphs_to_test:
        print(g)
        node_num, iterations, iterations_k = test_graph(g)
        graph_size.append(node_num)
        iterations_list.append(iterations)
        iterations_k_list.append(iterations_k)
    plot_iterations_to_graph_size(iterations_list, iterations_k_list, graph_size)


def incrementing_k_on_specific_graph(max_k=15):
    g = get_graph3()
    first_cycle = nearest_neighbour_algorithm(g)
    total_times = []
    min_costs = []
    iterations = []
    k_parameter = []
    for k in range(1, max_k + 1):
        timers, min_cost, iterations_no = optimization_2_opt_with_k_deterioration(g, first_cycle, k,
                                                                                 iterations_until_break_threshold=5)
        k_parameter.append(k)
        total_times.append(sum(timers))
        min_costs.append(min_cost)
        iterations.append(iterations_no)
    print('Incrementing k parameter on graph with ', g.num_of_nodes, ' nodes')
    print('k:\t\t\t', k_parameter)
    print('Costs:\t\t', min_costs)
    print('Iterations:\t', iterations)
    plot_iterations_to_k(iterations, k_parameter, g.num_of_nodes)
    plot_cost_to_k(min_costs, k_parameter, g.num_of_nodes, g.optimal_solution)


if __name__ == '__main__':
    # tsplib_import_example()
    # old_opt_2()
    compare_costs_and_times_on_different_graphs()
    # incrementing_k_on_specific_graph(15)
