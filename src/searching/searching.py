# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    #check base case of there being an item in list
    if end >= start:
        # if not base case find midpoint of list
        mid = (end + start) // 2
        # check value at midpoint to see if it is target
        if arr[mid] == target:
            #if so, return mid index as location of target
            return mid
        #if target is less than value at mid point, perform binary search on lower list
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        #if targe is greater than value at mid point, perform binary search on higher list
        else:
            return binary_search(arr, target, mid + 1, end)
    else:
        # reached base case without finding element
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

