# Binary index tree: build and get sum.

def getSum(tree, i):
    sum = 0
    i += 1

    while i > 0:               # tree's 0 node is a dummy node, contains nothing.
        sum += tree[i]         # add summary of all left nodes.
        i -= i & (-i)          # go to parent node and continue.

    return sum


def addNode(tree, N, i, val):
    i += 1

    while i <= N:
        tree[i] += val    # update current sum.
        i += i & (-i)     # go to parent-affected node and update it.


def construct(arr, N):
    tree = [0 for _ in range(N+1)]

    for i in range(N):
        addNode(tree, N, i, arr[i])

    return tree


# Driver code to test above methods
array = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BinaryIndexTree = construct(array, len(array))
print("Sum of elements in arr[0..5] is " + str(getSum(BinaryIndexTree, 5)))

# Update code
array[3] += 6
addNode(BinaryIndexTree, len(array), 3, 6)
print("Sum of elements in arr[0..5] is " + str(getSum(BinaryIndexTree,5)))