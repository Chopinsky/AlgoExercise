def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def BuildHeap(array):
    n = len(array)
    for i in range(n/2-1, -1, -1):
        SiftDown(array, i)


def SiftDown(arr, i):
    size = len(arr)
    if 2*i+1 >= size:
        # At leaf node
        return arr

    if 2*i+1 == size-1 and arr[i] < arr[2*i+1]:
        # Only left node exists and it's a leaf
        swap(arr, i, 2*i+1)
        return arr
    elif 2*i+2 < size:
        # Both leaf nodes exist, swap parent with the largest child.
        if arr[2*i+2] <= arr[2*i+1] and arr[i] < arr[2*i+1]:
            swap(arr, i, 2*i+1)
            return SiftDown(arr, 2*i+1)
        elif arr[2*i+1] <= arr[2*i+2] and arr[i] < arr[2*i+2]:
            swap(arr, i, 2*i+2)
            return SiftDown(arr, 2*i+2)

    return arr


def HeapSort(arr):
    BuildHeap(arr)

    size = len(arr)
    for i in range(len(arr)-1):
        swap(arr, 0, size-1)
        size -= 1
        # rebuild array, since sift down only affects part of the array.
        arr = SiftDown(arr[:size], 0) + arr[size:]

    return arr


array = [10, 7, 6, 2, 3, 9, 12, 4]
array = HeapSort(array)
print(array)