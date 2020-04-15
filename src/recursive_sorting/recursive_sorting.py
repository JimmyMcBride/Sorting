# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
    while len(arrA) > 0:
        merged_arr.append(arrA.pop(0))
    while len(arrB) > 0:
        merged_arr.append(arrB.pop(0))

    return merged_arr


# print(merge([0, 7, 2, 8], [3, 1, 6, 5]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # (base case) If the array is empty or length 1, return
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        arrA = arr[:middle]
        arrB = arr[middle:]

        arrA = merge_sort(arrA)
        arrB = merge_sort(arrB)

        return merge(arrA, arrB)

    return arr


print(merge_sort([0, 7, 2, 8, 3, 1, 6, 5]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
