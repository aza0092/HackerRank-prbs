from collections import OrderedDict

n , mydict= int(input()) , {}
for _ in range(n):
    info = input().rsplit(" ",1)
    if info[0] in mydict :
        mydict[info[0]] += int(info[1])
    else:
        mydict[info[0]] = int(info[1])
for item,price in mydict.items():
    print(item,price)
