def linear_search(arr, target):
    for el in arr:
        if el == target:
            return arr.index(el)

    return -1   # not found

# def linear_search(arr, target):
#     # Your code here
#     for i in range(len(arr)):
#         if arr[i] == target:
#             print(i)
#             return i

#     return -1   # not found

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    middle = 0
    end = len(arr) -1

    while start <= end:
        middle = start + end // 2

        if arr[middle] > target:
            end = middle - 1
        else:
            return arr.index(target)

    return -1  # not found


arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]

print(linear_search(arr1, 7))