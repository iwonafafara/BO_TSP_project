from graph import Graph, EuclideanGraph

if __name__ == '__main__':
    g = Graph(5, {0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4], 3: [0, 1, 2, 4], 4: [0, 1, 2, 3]})
    print('Num of nodes: ', g.num_of_nodes)
    print('Visited: ', g.visited_nodes)
    print('Vertices: ', g.paths)

    g2 = EuclideanGraph(5, {0: [4, 1], 1: [2, 1], 2: [1, 3], 3: [5, 3], 4: [3, 4]})
    print('Num of nodes: ', g2.num_of_nodes)
    print('Nodes: ', g2.nodes)
    print('Visited: ', g.visited_nodes)
    print('Vertices: ')
    for node in g2.paths:
        print('\t', node, ': ', g2.paths[node])
