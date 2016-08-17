#
# Problem: Find cyclic loop in a graph.
#
from __future__ import print_function

# DFS method:
INF = float('inf')

def createGraph(V):
    nodes = [[INF] for _ in range(V)]
    return nodes


def addEdge(nodes, v, w):
    if nodes[v][0] == INF:
        nodes[v][0] = w
    else:
        nodes[v] += [w]


def printCyclicLoop(stack):
    print("+" * 40)
    print("These nodes are in a cyclic loop: ")
    for i in range(len(stack)):
        print(str(i) + " ", end="")
    print("\n" + "+" * 40)


def isCyclic(nodes, v, visited, recursionStack):
    if visited[v] == False:
        # visited array contains nodes that has been examined;
        visited[v] = True

        # recursionStack is the buffer stack for the current recursion.
        recursionStack.append(v)

        for i in range(len(nodes[v])):
            node = nodes[v][i]

            # Dead end, definitely not a cyclic loop.
            if visited[node] == INF:
                break

            if visited[node] == False and isCyclic(nodes, node, visited, recursionStack):
                # Start a new recursion to find if it's part of the cyclic.
                return True
            elif recursionStack.count(node) > 0:
                # The neighbor node has already been visited from the current recursion.
                return True

    # reset recursion stack of the current node no matter what.
    recursionStack.remove(v)
    return False


def findCyclic(nodes):
    size = len(nodes)
    visited = [False] * size
    recStack = []

    for node in range(size):
        if isCyclic(nodes, node, visited, recStack):
            printCyclicLoop(recStack)
            return True

    return False


nodes = createGraph(4)
addEdge(nodes, 0, 1)
addEdge(nodes, 0, 2)
addEdge(nodes, 1, 2)
addEdge(nodes, 2, 0)
addEdge(nodes, 2, 3)
addEdge(nodes, 3, 3)

if findCyclic(nodes):
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")
