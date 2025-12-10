# https://www.acmicpc.net/problem/2675

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



T = int(input())

for _ in range(T):
    R, S = input().split()  # 3 ABC입력시 R == '3', S == 'ABC'로 입력됨
    
    K = ""  # 빈문자열(str)
    for i in range(1, len(S)+1):    # 1부터 S길이+1까지(1~4)
        a = S[i-1] * int(R)     # R == '3', S == 'ABC'일때, S[i-1] == 'A'->'B'->'C'순으로 바뀜, 각각을 int(R)만큼 반복해서 출력
        K= K + a    # R == '3', S == 'ABC'일때, K == 'AAABBBCCC'
    
    print(K)