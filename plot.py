import matplotlib.pyplot as plt
from graph import EuclideanGraph


def plot_graph(graph: EuclideanGraph, path: list):
    axis_list = []
    ayis_list = []
    for item in path:
        axis_list.append(graph.nodes[item][0])
        ayis_list.append(graph.nodes[item][1])

    plt.plot(axis_list, ayis_list, '-o')
    plt.plot(axis_list[0], ayis_list[0], 's')
    plt.title('Graf zoptymalizowany dla ' + str(graph.num_of_nodes) + ' węzłów')
    plt.show()


