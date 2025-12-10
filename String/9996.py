# https://www.acmicpc.net/problem/9996

times = int(input())    # 시도횟수
pattern = input().split('*')    # 패턴
p1 = len(pattern[0])    # 처음 패턴길이
p2 = len(pattern[-1])   # 마지막 패턴길이
text = []
#print(times,pattern)
for i in range(times):
    text.append(input())    #입력한 str을 text에 차례대로 추가
    out = text
    if len(text[i]) < p1+p2:
        out[i] = 'NE'
        #print('short')
# print(text)
    elif out[i][:p1] == pattern[0] and out[i][-1*p2:] == pattern[1]: #첫글자가 패턴의 첫글자랑 같은가?
            out[i] = 'DA'
            #print('right')
    else:
        #print('b')
        out[i] = 'NE'
        #print('wrong')

for i in range(times):
    print(out[i])
