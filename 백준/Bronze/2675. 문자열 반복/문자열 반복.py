testcase = int(input())
tryy = 0
put = []
for i in range(testcase):
    a = input().split(' ')
    put.append(a)   # 3 ABC입력시 ['3','ABC']로 입력됨
    put[i][0] = int(put[i][0])  # ['3','ABC'] -> [3,'ABC']


while tryy < testcase:  # testcase만큼 반복
    for i in range(len(put[tryy][1])):   # put == [[3,'ABC'],[4,'/HTP']]일때 3만큼 반복 후 4만큼 반복
        print(put[tryy][1][i] * put[tryy][0],end='')    # put[0] == [3,'ABC']일때 A를 3번, B를 3번,C를 3번 순차적으로 출력

    print('')   #줄바꿈
    tryy += 1
