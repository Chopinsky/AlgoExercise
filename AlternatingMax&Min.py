#
# Problem: re-arrange an array, such that maximum and minimum values alternate by order.
#

def stitchArray(arr):
    if len(arr) == 0:
        return arr

    result = [0] * len(arr)
    arr.sort()
    start = 0
    end = len(arr) - 1
    count = 0

    while start < end:
        result[count] = arr[start]
        result[count+1] = arr[end]
        count += 2
        start += 1
        end -=1

    if start == end:
        result[count] = arr[start]

    return result


print(stitchArray([1, 3, 8, 2, 7, 5, 6, 4]))
print(stitchArray([1, 2, 3, 4, 5, 6, 7]))
print(stitchArray([1, 6, 2, 5, 3, 4]))