# Dijsktra algorithm to find minimum distance from source node to any node presented in the graph

GRAPH_VERTICES = 9

# find the min distance node in the unvisited vertices collection <-- which are the immediate neighbor of the
# visited vertices.
def findNextNode(dist, visited):
    min = float('inf')
    minIndex = -1

    for i in range(GRAPH_VERTICES):
        if visited[i] == False and dist[i] <= min:
            min = dist[i]
            minIndex = i

    return minIndex


def printSolution(dist, N):
    print("Vertex\tDistance from Source")

    for i in range(GRAPH_VERTICES):
        print(str(i) + "\t" + str(dist[i]))


# 1, update neighbor vertices or the current vertices; at step 0, it will be source node's neighbors
# 2, move to the updated node which has the lowest distance to the source node.
# 3, repeat step 1 and update unvisited neighbor vertices.
def dijkstra(graph, srcVertex):
    dist = [float('inf')] * GRAPH_VERTICES
    visited = [False] * GRAPH_VERTICES

    dist[srcVertex] = 0

    for count in range(GRAPH_VERTICES-1):
        currVertex = findNextNode(dist, visited)
        visited[currVertex] = True

        for neighborVertex in range(GRAPH_VERTICES):
            # logic: find unvisited neighbor vertex, which could have a smaller distance than its current
            # min distance, based on the min distance of the currently examined vertex.
            if visited[neighborVertex] != True and graph[currVertex][neighborVertex] != 0 \
                    and dist[currVertex] != float('inf') \
                    and dist[currVertex] + graph[currVertex][neighborVertex] < dist[neighborVertex]:
                dist[neighborVertex] = dist[currVertex] + graph[currVertex][neighborVertex]

    printSolution(dist, GRAPH_VERTICES)


# Test graph set
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 0, 10, 0, 2, 0, 0],
         [0, 0, 0, 14, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
dijkstra(graph, 0)

