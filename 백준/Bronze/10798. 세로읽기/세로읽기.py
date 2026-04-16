from sys import stdin
TRY = 5;lst = list()
for _ in range(TRY):
    lst.append(list(stdin.readline().strip()))
for i in range(15):
    for j in lst:
        if i<len(j):print(j[i],end='')