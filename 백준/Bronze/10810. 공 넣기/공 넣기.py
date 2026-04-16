N,M = map(int,input().split())
lst = [0] * (N+1)
for _ in range(M):
    i,j,k = map(int,input().split())
    for item in range(i,j+1):lst[item] = k
for x in range(len(lst)-1):print(lst[x+1],end=' ')