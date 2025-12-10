# 다른곳에 있던거
# while True:
#     try:
#         A,B = sorted(map(int,input().split()))
#         print(A+B)
#     except:
#         break


# res = 0
# cnt = 100
# for i in range(cnt):
#     res += ((-1)**i)*(4/(2*i+1))
#     print(res)

# N,cnt = int(input()),0
# lst = list(map(int,input().split()))
# v = int(input())
# for i in range(len(lst)):
#     if lst[i] == v:
#         cnt += 1
# print(cnt)

# txt = 'abcde'
# print(index(txt[1]))

# out =   dict(zip('ABCDEFG',range(7)))
# print(out)

# a = list('0'*26)
# print(list(map(int,a)))

# a = 'hello'
# print(list(a))

# txt = ['abcdef','asdasd','123456']
# p2 = 3
# for i in range(3):
#     print(txt[i][-1*p2:])
#     print(i)

import random
for i in range(100):
    print(random.randint(1,10),end='/')
