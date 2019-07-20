if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = arr[:n]
    arr2.sort()
    arr2 = list(dict.fromkeys(arr2)) #remove duplicates, dict cant have duplicate keys
    print(arr2[len(arr2)-2])
