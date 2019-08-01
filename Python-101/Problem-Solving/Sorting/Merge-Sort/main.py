def merge(left, right):
    split_inversion_counter = 0
    result = []  # final result array, that is an empty array
    i, j = 0, 0
    ra = result.append
    left_array_length = len(left)
    right_array_length = len(right)

    while (i < left_array_length) and (j < right_array_length):
        if left[i] <= right[j]:
            ra(left[i])
            i += 1
        else:
            ra(right[j])
            j += 1
            split_inversion_counter += left_array_length - i
    result += left[i:]
    result += right[j:]
    return result, split_inversion_counter


def mergesort(lst):
    if (len(lst) <= 1):
        return lst, 0
    mid = (len(lst) // 2)
    left, counter0 = mergesort(lst[:mid])
    right, counter1 = mergesort(lst[mid:])
    result, counter2 = merge(left, right)
    return result, counter2 + counter0 + counter1


def count_inversions(arr):
    final, counter = mergesort(arr)
    return counter

l = [2,1,3,1,2]
result = count_inversions(l)
print(result)

'''
# https://www.youtube.com/watch?v=PLkuid82dbc
# Inversion count is achieved via recursively calling merge AND SORT
# 1. Check if the array has only one value, return the value
# 2. split the array into Left and Right, and call merge recursively on each side L and R
# 3. Merge both L and R back togethor into a final sorted array:
#       - loop through array length using indexes i for L, j for R, and k for final array 'D'
#       - Compare the leftmost of L and R, and check which has the smallest value
#       - While merging the two subarrays, keep count of number of inversions
#       - When element of 2nd array C gets copied to D, increment total of split inversions by number of elements remaining in 1st array B

# Where does the inversion happen?
#       - 1. If x copied to D before y, then x < y. No split inversion involved
#       - 2. if y copied to D before x, then y < x. x,y are a split inversion


def count_inversions(array):
    final, counter = merge_sort(array)
    return counter


def merge_sort(array):
   if len(array) <= 1:
       return array
   else:
       pivot= len(array)//2
       left, left_splits = merge_sort(array[:pivot])
       right, right_splits = merge_sort(array[pivot:])
       result, total_splits = merge(left,right)
       return result, total_splits + left_splits + right_splits


def count_inversions(arr):
    """
    count inversion sum of L, R, and split
    Key idea: have recursive calls both count inversion and sort
    """
    return count_inversions(arr, 0, len(arr) - 1)




def merge(array1, array2):
   i, j = 0, 0
   result = []
   ra = result.append
   count_split_inversions = 0
   m = len(array1)
   n = len(array2)

   while(i < m) and (j < n):
      if (array1[i] <= array2[j]):
         ra(array1[i])
         i += 1
      else:
         ra(array2[j])
         j += 1
         count_split_inversions += m - i


   result += array1[i:]
   result += array2[j:]
   return result, count_split_inversions


A = [2,1,3,1,2]
print(A)
r = count_inversions(A)
print(r)
'''
