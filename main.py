from graph import Graph, EuclideanGraph

if __name__ == '__main__':
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

    g2 = EuclideanGraph(5, {0: [4, 1], 1: [2, 1], 2: [1, 3], 3: [5, 3], 4: [3, 4]})
    print('Num of nodes: ', g2.num_of_nodes)
    print('Nodes: ', g2.nodes)
    print('Visited: ', g.visited_nodes)
    print('Vertices: ')
    for node in g2.paths:
        print('\t', node, ': ', g2.paths[node])
