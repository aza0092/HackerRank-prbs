def sock_merchant(n, arr):
    pairs = 0
    for i in set(arr):
        pairs += arr.count(i) // 2
    return pairs
