import tsplib95
import graph


#odczytanie i korzystanie z danych potrzebnych do stworzenia grafów
graphs_directory = 'graphs\\'


def set_weights(edge_weights, g: graph.Graph):
    for line in edge_weights:
        node1 = len(line) + 1
        for i in range(len(line)):
            node2 = i + 1
            g.set_weight(node1, node2, line[i])


def get_normal_graph_with_weights(filename):
    file_coord = graphs_directory + filename
    data_coord = tsplib95.load(file_coord)
    g = graph.Graph(data_coord.dimension)
    set_weights(data_coord.edge_weights, g)
    return g


def get_graph1():
    file1_coord = graphs_directory + 'ulysses16.tsp'
    data_coord = tsplib95.load(file1_coord)
    return graph.EuclideanGraph(data_coord.dimension, data_coord.node_coords)


def get_graph2():
    return get_normal_graph_with_weights('gr24.tsp')


def get_graph3():
    file3_coord = graphs_directory + 'bayg29.tsp'
    data_coord3 = tsplib95.load(file3_coord)
    g = graph.EuclideanGraph(data_coord3.dimension, data_coord3.display_data)
    # set_weights(data_coord3.edge_weights, g)
    return g


def get_graph4():
    return get_normal_graph_with_weights('gr48.tsp')