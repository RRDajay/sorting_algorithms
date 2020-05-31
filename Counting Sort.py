def _counting_sort(arr):
    sorted_array = [None] * len(arr)

    # Find occurrences of each number
    occ = [arr.count(i) for i in range(max(arr) + 1)]

    # Cumulative sum
    for i in range(len(occ) - 1):
        occ[i + 1] = occ[i] + occ[i + 1]

    # Shif cum sum index one place to the right
    occ.insert(0, 0)
    occ = occ[:-1]

    # Counting sort;
    for i in range(len(arr)):
        sorted_array[occ[arr[i]]] = arr[i]
        occ[arr[i]] += 1

    return sorted_array

arr = [0, 0, 3, 1, 5, 9, 2, 7, 8, 3, 4]
print(_counting_sort(arr))
