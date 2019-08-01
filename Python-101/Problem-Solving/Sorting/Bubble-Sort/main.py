def countSwaps(a):
    is_sorted = False
    swaps = 0

    while not is_sorted:
        is_sorted = True
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                swap(a, i)
                swaps += 1
                is_sorted = False

    print("Array is sorted in %d swaps." % swaps)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[-1])


def swap(a, i):
    temp = a[i]
    a[i] = a[i + 1]
    a[i + 1] = temp
