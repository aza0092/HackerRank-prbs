import collections

number_of_shoes = int(input())
sizes_in_stock = collections.Counter(map(int, input().split())) #make a counter for each shoes size
total_revenue = 0

for _ in range(int(input())): #number of customers
    size, price = map(int, input().split())
    if sizes_in_stock[size]: #targetted size
        total_revenue += price
        sizes_in_stock[size] -= 1 #update inventory

print(total_revenue)
