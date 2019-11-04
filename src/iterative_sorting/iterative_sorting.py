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
            smallest = item
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

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr