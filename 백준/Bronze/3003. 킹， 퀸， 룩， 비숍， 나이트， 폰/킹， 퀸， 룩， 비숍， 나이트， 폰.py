lst = [1,1,2,2,2,8]
lst2 = list(map(int,input().split(' ')))
for i in range(len(lst)):
    lst[i] = lst[i] - lst2[i]
    print(lst[i],end=' ')