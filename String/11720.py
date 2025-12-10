# https://www.acmicpc.net/problem/11720

tryy,num = int(input()),input() # 시도횟수 , 입력한값


# 1 #
# out = 0
# for i in range(tryy): 시도횟수만큼 반복
#     out+=eval(num[i]) out에 입력값[0~tryy]까지 모두 더함
# print(out) 출력

# 2 #
print(sum(eval(num[i]) for i in range(tryy)))