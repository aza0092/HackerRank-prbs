def is_palandrome(numstr):
    numstr = str(numstr)
    if numstr == numstr[::-1]:  # if its the same forward and back. 
        return True
    return False
        
n = int(input())
lst = [ int(x) for x in input().split() ]

if all( (i >= 0) for i in lst):
  # if any items are a palandrome, it will print true, otherwise, prints false.
    print( any( is_palandrome(n) for n in lst) )
else:
    print(False)
