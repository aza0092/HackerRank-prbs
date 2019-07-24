A = set(input().split())
n = int(input())
check = [] # stores true/false
for _ in range(n):
    B = set(input().split())
    check.append(A.issuperset(B))
print(all(check))