if __name__ == '__main__':
    N = int(input())
    li =[]
    # Dictionary of list "li" methods but print
    actions ={'insert': li.insert,
              'remove': li.remove,
              'append': li.append,
              'sort': li.sort,
              'pop': li.pop,
              'reverse': li.reverse,
             }
    # We do the loop for each line of input
    for _ in range(N):
        order, *args = input().split()
        # Execute "print" separately
        if(order == 'print'):
            print(li)
        # Execute any list method here
        else:
            actions[order](*map(int,args))
