N,M = map(int,input().split());lst = list(i for i in range(1,N+1))
for i in range(M):a,b = map(int,input().split());\
    lst2 = lst[a-1:b];lst2.reverse();lst[a-1:b] = lst2
for i in lst:print(i,end=' ')