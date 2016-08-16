#
# Problem: find shortest distances between every pair of vertices in a given edge weighted directed graph.
#
from __future__ import print_function
from copy import deepcopy

INF = float('inf')
test_graph = [
    [  0,   5, INF,  10],
    [INF,   0,   3, INF],
    [INF, INF,   0,   1],
    [INF, INF, INF,   0]]
GRAPH_VERTICES = len(test_graph)


def FWAlgorithm(graph):
    dist = deepcopy(graph)

    # Check all intermediate vertex and update if there exists a 'shorter' path.
    for k in range(GRAPH_VERTICES):
        for i in range(GRAPH_VERTICES):
            for j in range(GRAPH_VERTICES):
                if dist[i][k] != INF and dist[k][j] != INF \
                        and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    printSolution(dist)


def printSolution(dist):
    for i in range(GRAPH_VERTICES):
        for j in range(GRAPH_VERTICES):
            if dist[i][j] == INF:
                print("INF ", end="")
            else:
                print(str(dist[i][j]) + "   ", end="")
        print()


FWAlgorithm(test_graph)
