import graph
from graph import Graph, EuclideanGraph
from algos import nearest_neighbour_algorithm, optimization_2_opt, optimization_2_opt_with_k_deterioration
from import_data import get_graph1, get_graph2, get_graph3, get_graph4, get_graph5, get_graph6, get_graph7
from plot import plot_graph
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
        print('Graph with ', g.num_of_nodes, ' nodes:')
        print('Algorithm without deterioration: ')
        print('Min_cost: ', min_cost, ' Iterations: ', iterations, f' Total time: {sum(timers):.03f}ms')
        print('Times: ', timers)
        print('Algorithm with ', k, ' deterioration: ')
        print('Min_cost: ', min_cost_k, ' Iterations: ', iterations_k, f' Total time: {sum(timers_k):.03f}ms')
        print('Times: ', timers_k)
        print('\n\n\n')

    graphs_to_test = [get_graph1(), get_graph2(), get_graph3()]
    for g in graphs_to_test:
        print(g)
        test_graph(g)


if __name__ == '__main__':
    # tsplib_import_example()
    # old_opt_2()
    compare_costs_and_times_on_different_graphs()
