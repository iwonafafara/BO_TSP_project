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
