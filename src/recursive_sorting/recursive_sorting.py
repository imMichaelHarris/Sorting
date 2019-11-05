# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print("num", elements)
    # TO-DO
    # merged_arr = arrA.extend(arrB)
    for i in range(elements):
        print("if", i, arrA, arrB)
        if arrA[i] > arrB[i]:
            print("yes", arrA[i], arrB[i])
            merged_arr[i] = arrB[i]
        else:
            print("no", arrA[i], arrB[i])
            merged_arr[i] = arrA[i]
            
        print("merged_arr", merged_arr)
    # merged_arr = arrA + arrB  #this can't be it not sure what the other two lines are for will ask about this later
    return merged_arr

# print(merge([9], [6]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # split arr iso each item is in it's own list
    # compare two list together by looking at first index of each list and sort which comes first
    if len(arr) <= 1:
        return arr
    # for item in arr:
    #     newArr = [item]
    #     print("new", newArr)
    half = int(len(arr) / 2)
    leftArr = arr[:half]
    rightArr = arr[half:]
    print("half", leftArr, rightArr)
    merge_sort(rightArr)
    merge_sort(leftArr)
    # if leftArr[0] < rightArr[0]:
    #     print("merge", merge(leftArr, rightArr))
    # else:
    #     print("else merge", merge(rightArr, leftArr))
    # print("after", arr)
    return merge(leftArr, rightArr)

merge_sort([3,6,5,8,2,1,6,9])
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
