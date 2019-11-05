# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i # i = 0
        smallest_index = cur_index #0
        value = arr[cur_index]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for item in range(i, len(arr)):
            if arr[item] < arr[smallest_index]:
                smallest_index = item
            

    #[ 3, 2, 9, 4, 5]

        # TO-DO: swap
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = value




    return arr

print(selection_sort([5, 2,3,1 ,6, 7,9]))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps = 0
    while swaps is not None:
        swaps = 0
        for i in range(0, len(arr) - 1):
            current_val = arr[i]
            if current_val > arr[i + 1]:
                arr[i] = arr[i + 1]
                arr[i + 1] = current_val
                swaps += 1
        if swaps == 0:
            swaps = None
    print("swaps", swaps)
    return arr


print(bubble_sort([5, 2,3,1 ,6, 7,9]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr