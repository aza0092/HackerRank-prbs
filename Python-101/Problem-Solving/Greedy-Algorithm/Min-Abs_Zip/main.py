def minimumAbsoluteDifference(arr):
    arr.sort()
    abs_arr = []
    for current_item, next_item in zip(arr, arr[1:]):  # To get cur,next item in list, use zip
        abs_arr.append(abs(current_item - next_item))
    print(min(abs_arr))