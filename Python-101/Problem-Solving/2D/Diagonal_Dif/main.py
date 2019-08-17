def diagonal_difference(arr):
    left_sum = 0
    right_sum = 0
    array_length = len(arr)
    for index in range(array_length):
        left_sum += arr[index][index]  # \  [row][col].. (0,0),(1,1),(2,2)
        right_sum += arr[index][array_length - index - 1]  # /  [row][col].. (0,2),(1,1),(2,0)
    return abs(left_sum - right_sum)


num_in_each_row = int(input().strip())
row = []
for _ in range(num_in_each_row):
    row.append(list(map(int, input().rstrip().split())))

result = diagonal_difference(row)
print(result)

'''
SAMPLE INPUT:
3
11 2 4
4 5 6
10 8 -12
RESULT: 15
'''