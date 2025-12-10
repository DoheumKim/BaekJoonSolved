# https://www.acmicpc.net/problem/10809

# chr(97) == 'a'
# chr(122) == 'z'
#index = 97
sentence = input()
out = []

for index in range(97,123): # a~z까지 반복
    if chr(index) in sentence:  #sentence안에 a~z가 있는지 확인
        out.append(str(sentence.index(chr(index)))) # 있으면 sentence내의 a~z의 인덱스를 out에 추가
        # print(out)
    else:
        out.append('-1')    #없으면 -1을 out에 추가
        # print(out)
print('asd',out)
print(" ".join(out))    # 아래대로 출력
# 입력: baekjoon
# 출력: 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1





    # #for i in range(len(sentence)):
    #     if index == 122:
    #         out.append(-1)
    #         print(out)
    #     else:
            
    #         index += 1
    #         print(out,index)
