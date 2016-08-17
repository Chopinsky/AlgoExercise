#
# Problem:
#

def union(edge, MSTSet, result):
    src = -1
    dst = -1

    # Find source and destination sub-array
    for i in range(len(MSTSet)):
        if edge[0] in MSTSet[i]:
            src = i
        if edge[1] in MSTSet[i]:
            dst = i

    if src == -1 and dst == -1:
        # Edge doesn't exist in MST yet
        MSTSet += [[edge[0], edge[1]]]
    elif src == dst:
        # Will create cyclic loop, don't do anything
        return
    elif src > -1 and dst > -1:
        MSTSet[src] += MSTSet[dst]
        MSTSet.remove(MSTSet[dst])
    elif src > -1:
        MSTSet[src] += [edge[1]]
    elif dst > -1:
        MSTSet[dst] += [edge[0]]

    result += [edge]

def getKey(item):
    return item[2]


def findMST(edges, verticesCount):
    sortedEdges = sorted(edges, key=getKey)
    MSTSet = []
    result = []
    for i in range(len(edges)):
        union(sortedEdges[i], MSTSet, result)

    printSolution(result)


def printSolution(result):
    print("+" * 40)
    print(str(len(result)) + " edges: ")
    for i in range(len(result)):
        print(str(result[i][0]) + " - " + str(result[i][1]) + " : " + str(result[i][2]))
    print("+" * 40)


edges = []
edges += [[0, 1, 10]]
edges += [[0, 2, 6]]
edges += [[0, 3, 5]]
edges += [[1, 3, 15]]
edges += [[2, 3, 4]]
findMST(edges, 4)

newSet = [
    [8, 2, 2],
    [7, 6, 1],
    [0, 1, 4],
    [6, 5, 2],
    [2, 5, 4],
    [8, 6, 6],
    [2, 3, 7],
    [7, 8, 7],
    [0, 7, 8],
    [1, 2, 8],
    [3, 4, 9],
    [5, 4, 10],
    [1, 7, 11],
    [3, 5, 14]
]
findMST(newSet, 9)

