def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


sorted_array = selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
print(sorted_array)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                sorted = False

    return arr


sorted_array = bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
print(sorted_array)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
