N,M = map(int,input().split())
basket = list((i) for i in range(1,N+1))
chn = []
for i in range(M):
    chn.append(list(map(int,input().split())))
    a = basket[(chn[i][0]-1)]
    basket[(chn[i][0]-1)] = basket[(chn[i][1]-1)]
    basket[(chn[i][1]-1)] = a
for i in range(len(basket)):print(basket[i],end=' ')

