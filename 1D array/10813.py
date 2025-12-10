N,M = map(int,input().split())
# print(N,M)
basket = list((i) for i in range(1,N+1))
chn = []    #바꿀 바구니 [i][0] -> [i][1]
# print(basket)
for i in range(M):
    chn.append(list(map(int,input().split())))
    # print(f'chn: {chn}')
    a = basket[(chn[i][0]-1)]   #바꿀 바구니 숫자 저장
    basket[(chn[i][0]-1)] = basket[(chn[i][1]-1)]   #입력받은 바구니끼리 바꾸기(1 2면 1번바구니 숫자를 2번 바구니 숫자로 바꾸기)
    basket[(chn[i][1]-1)] = a   # 2번바구니 숫자를 1번으로 바꿈
    # print(f'basket: {basket}')
for i in range(len(basket)):print(basket[i],end=' ')

