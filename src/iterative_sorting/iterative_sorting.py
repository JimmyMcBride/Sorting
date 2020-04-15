#TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # for each element from the current index to the end of the array
        for ele in range(i, len(arr)):
            arr_element = arr[ele]
            print("array element", arr_element)
            arr_smallest = arr[smallest_index]
            print("array smallest" ,arr_smallest)
            if arr_element <= arr_smallest:
                smallest_index = ele

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


print(selection_sort([9, 5, 8, 4, 2, 1, 6, 0, 3, 7]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

    if sorted:
        return arr

    return arr


bubble_sort([9, 5, 8, 4, 2, 1, 6, 0, 3, 7])

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
