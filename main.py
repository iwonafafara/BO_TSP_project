import graph
from graph import Graph, EuclideanGraph, nearest_neighbour_algorithm
from import_data import *

def basic_graph_example():
    g = Graph(8, {
        0: [[1, 2], [2, 2], [3, 4], [4, 3]],
        1: [[0, 2], [2, 2], [5, 1], [6, 1]],
        2: [[0, 2], [1, 2], [4, 2], [5, 1]],
        3: [[0, 4], [5, 2], [7, 3]],
        4: [[0, 3], [2, 2], [6, 4], [7, 5]],
        5: [[1, 1], [2, 1], [3, 2], [6, 2], [7, 2]],
        6: [[1, 1], [4, 4], [5, 2], [7, 2]],
        7: [[3, 3], [4, 5], [5, 2], [6, 2]]})
    print('Num of nodes: ', g.num_of_nodes)
    print('Visited: ', g.visited_nodes)
    print('Vertices: ')
    for node in g.paths:
        print('\t', node, ': ', g.paths[node])


def euclidean_graph_example():
    g = EuclideanGraph(5, {0: [4, 1], 1: [2, 1], 2: [1, 3], 3: [5, 3], 4: [3, 4]})
    print('Num of nodes: ', g.num_of_nodes)
    print('Nodes: ', g.nodes)
    print('Visited: ', g.visited_nodes)
    print('Vertices: ')
    for node in g.paths:
        print('\t', node, ': ', g.paths[node])


def tsplib_import_example():
    data_coord = tsplib95.load(file1_coord)
    data_coord2 = tsplib95.load(file3_coord)
    g = graph.EuclideanGraph(data_coord.dimension, data_coord.node_coords)
    g2 = graph.EuclideanGraph(data_coord2.dimension,data_coord2.node_coords)

    print(g.num_of_nodes)
    print(g.nodes)
    print(nearest_neighbour_algorithm(g))


if __name__ == '__main__':
    basic_graph_example()
    euclidean_graph_example()
    tsplib_import_example()

