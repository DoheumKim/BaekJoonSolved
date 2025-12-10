'''
basket,trial = input().split(' ')
# N개의 바구니(basket)에 M번(trial)만큼 공을 넣음
lst = []
for _ in range(int(basket)):lst.append(0)

method = [] # [0] == start,[1] == end,[2] == num
for _ in range(int(trial)):
    method.append(input().split(' '))
inp_try = []
# start번에서 end번 바구니까지 num번이 적혀있는 공을 넣음
# 바구니에 공이 이미 있다면 원래있던거를 제외하고 새로운 공을 넣음(대체함)
for i in range(int(trial)):
    method[i][0] = int(method[i][0])  #index번호 맞추기(1이면 lst[0]이 되야됨)
    method[i][1] = int(method[i][1])
    method[i][2] = int(method[i][2])
    inp_try.append(method[i][1] - method[i][0])  #넣어야하는 바구니 수
    # print(inp_try)
for fix in range(len(inp_try)):
    if inp_try[fix] == 0:inp_try[fix] = 1
#method[2] #바구니에 넣는 번호

for i2 in range(int(trial)):
    for i3 in range(inp_try[i2]):
        lst[method[i2][0]-1+i3] = method[i2][2]
    #    print(f'{i2}|{i3}: {lst}')
show = ''
for prt in range(len(lst)):
    show += str(lst[prt])
    show += ' '
show = show[:-1]
print(show)
'''

N,M = map(int,input().split())
# N개의 바구니에 M번만큼 공을 넣음
lst = [0] * (N+1)
for _ in range(M):
    i,j,k = map(int,input().split())
    for item in range(i,j+1):lst[item] = k
    
for x in range(len(lst)-1):print(lst[x+1],end=' ')

