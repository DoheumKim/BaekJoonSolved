N,cnt = int(input()),0
lst = list(map(int,input().split()))
v = int(input())
for i in range(len(lst)):
    if lst[i] == v:
        cnt += 1
print(cnt)