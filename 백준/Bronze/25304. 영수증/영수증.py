X = int(input())
N = int(input())
lst= list(i for i in range(N))
summ = 0
for i in lst:
    lst[i] = eval(input().replace(*' *'))
    summ += lst[i]

if X == summ:
    print('Yes')
else:
    print('No')