import tsplib95
import graph


#odczytanie i korzystanie z danych potrzebnych do stworzenia grafów
graphs_directory = 'graphs\\'


def get_graph1():
    file1_coord = graphs_directory + 'ulysses16.tsp'
    data_coord = tsplib95.load(file1_coord)
    return graph.EuclideanGraph(data_coord.dimension, data_coord.node_coords)


def get_graph2():
    file2_coord = graphs_directory + 'gr24.tsp'
    data_coord2 = tsplib95.load(file2_coord)
    g = graph.Graph(data_coord2.dimension)

    for line in data_coord2.edge_weights:
        node1 = len(line) + 1
        for i in range(len(line)):
            node2 = i + 1
            g.set_weight(node1, node2, line[i])

    return g


def get_graph3():
    file3_coord = graphs_directory + 'bayg29.tsp'
    data_coord3 = tsplib95.load(file3_coord)
    g = graph.EuclideanGraph(data_coord3.dimension, data_coord3.display_data)

    for line in data_coord3.edge_weights:
        node1 = len(line) + 1
        for i in range(len(line)):
            node2 = i + 1
            g.set_weight(node1, node2, line[i])
    return g


def get_graph4():
    file4_coord = graphs_directory + 'gr48.tsp'
    data_coord4 = tsplib95.load(file4_coord)
    g = graph.Graph(data_coord4.dimension)

    for line in data_coord4.edge_weights:
        node1 = len(line) + 1
        for i in range(len(line)):
            node2 = i + 1
            g.set_weight(node1, node2, line[i])

    return g