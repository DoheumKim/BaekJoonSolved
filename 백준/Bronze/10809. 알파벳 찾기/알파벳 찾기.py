sentence = input()
out = []

for index in range(97,123): # a~z까지 반복
    if chr(index) in sentence:  #sentence안에 a~z가 있는지 확인
        out.append(str(sentence.index(chr(index)))) # 있으면 sentence내의 a~z의 인덱스를 out에 추가
        # print(out)
    else:
        out.append('-1')    #없으면 -1을 out에 추가
        # print(out)

print(" ".join(out))    # 아래대로 출력