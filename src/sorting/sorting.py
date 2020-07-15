# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = [0] * num_elements
    # Your code here
    #set iterators for both arrays
    i = 0
    j = 0

    # set iterator for main list

    k = 0
    #compare values in both list until you reach the end of one list
    while i < len(arrA) and j < len(arrB):
        #compare one value from list A with one value from list B
        if arrA[i] < arrB[j]:
            #if value from first list is lower add that to the proper spot of main list and increment iterator
            merged_arr[k] = arrA[i]
            i += 1
        else:
            #if value from second list is lower add that to the proper spot of main list and increment iterator
            merged_arr[k] = arrB[j]
            j += 1
        #move to the next slot in main list
        k += 1

    #check first list to see if any values remain. if so, add to main list 
    while i < len(arrA):
        #add item to main list
        merged_arr[k] = arrA[i]
        #increment iterator for first list and main list
        i += 1
        k += 1

    #check second list to see if any values remain. if so, add to main list 
    while j < len(arrB):
        #add item to main list
        merged_arr[k] = arrB[j]
        #increment iterator for second list and main list
        j += 1
        k += 1




    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    #check to see if hit the base case where length of array equals 1. We know array with one item is sorted
    
    if len(arr) <= 1:
        return arr
    if len(arr) > 1:
        #if length of arr is 1, split the array into two halves
        mid_point = len(arr) // 2
        left_arr = arr[:mid_point]
        right_arr = arr[mid_point:]

        #run merge_sort on both halves to sort each half
        left = merge_sort(left_arr)
        right = merge_sort(right_arr)

        arr = merge(left, right)
        return arr

   

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


