def ways_to_climb(n):
    steps = [1, 2, 3]  # how many steps can take
    ways = [1] + [0] * n
    for i in range(1, n + 1):
        for step in steps:
            if i - step >= 0:
                ways[i] += ways[i - step]
    return(ways[n])
