import matplotlib.pyplot as plt
from graph import EuclideanGraph


error_shown = False


def plot_graph(graph, path: list, title: str, filename: str):
    global error_shown
    if not isinstance(graph, EuclideanGraph):
        if not error_shown:
            print("This graph cannot be plotted - doesn't contain Euclidean coordinators.")
            error_shown = True
        return
    axis_list = []
    ayis_list = []
    for item in path:
        axis_list.append(graph.nodes[item][0])
        ayis_list.append(graph.nodes[item][1])

    plot_options = ''
    if graph.num_of_nodes < 50:
        plot_options = '-o'

    plt.plot(axis_list, ayis_list, plot_options)
    plt.plot(axis_list[0], ayis_list[0], 's')
    plt.title(title)
    plt.savefig('plots/' + filename + '.png')
    plt.show()


def plot_iterations_to_k(iterations_list, k_list, num_of_nodes):
    pass


def plot_cost_to_k(costs_list, k_list, num_of_nodes, optimal_cost):
    optimal_y = [optimal_cost, optimal_cost]
    optimal_x = [1, len(k_list)]
    plt.plot(k_list, costs_list)
    plt.plot(optimal_x, optimal_y)
    plt.title('Koszt w zależności od parametru k dla grafu o ' + str(num_of_nodes) + 'wierzchołkach')
    plt.savefig('plots/czas_od_k_' + str(num_of_nodes) + ' wierzcholkow.png')
    plt.show()


def plot_time_per_iteration(time_list, time_k_list, k, num_of_nodes):
    iterations = list(range(1, len(time_list) + 1))
    iterations_k = list(range(1, len(time_k_list) + 1))
    plt.plot(iterations, time_list)
    plt.plot(iterations_k, time_k_list)
    plt.title('Czas wykonania algorytmu od ilości iteracji dla grafu o ' + str(num_of_nodes) + ' wierzchołkach\n'
              'Parametr k: ' + str(k))
    plt.savefig('plots/czas_od_iteracji_dla' + str(num_of_nodes) + ' wierzcholkow.png')
    plt.show()


def plot_iterations_to_graph_size(iterations, iterations_k, graph_size):
    plt.plot(graph_size, iterations)
    plt.plot(graph_size, iterations_k)
    plt.title('Liczba iteracji do wielkości grafu')
    plt.savefig('plots/liczba_iteracji_do_wielkosci_grafu.png')
    plt.show()
