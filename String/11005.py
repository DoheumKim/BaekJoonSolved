'''
시간 제한	            메모리 제한	    제출	정답	맞힌 사람	정답 비율
0.5 초 (추가 시간 없음)	256 MB	        46886	21870	18863	    46.709%

문제
10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

출력
첫째 줄에 10진법 수 N을 B진법으로 출력한다.
'''
#chr(65) == A
n,typ = map(int,input().split())    #숫자, 진수
out = [0];typ2 = typ -10;loc = 0;lst_i = 0
# loc = 자리수
if typ <= 10:lst = list(_ for _ in range(typ))
else:lst = list(ten for ten in range(10))
for i in range(65,65+typ2):lst.append(chr(i))

print(lst,'ㅁㄴㅇ')

        
for i2 in range(1,n+1):
    if lst_i <len(lst):lst_i += 1
    else:lst_i=1
    # if out[0] == lst[-1]:   #첫번째(가장 큰 자리수)가 최대치일때
    #     for p in range(len(out)):out[p] = 0      #99 -> 100, 1젤앞에 넣고 나머지 0으로 바꾸기
    #     out.insert(0,1)
    #     print(out,'p')
    if out[-1] ==lst[-1]:
        for p in range(len(out)):out[p] = 0      #99 -> 100, 1젤앞에 넣고 나머지 0으로 바꾸기
        out.insert(0,lst[-1])   #자리수 넘어간거 추가(17이면 F1)에서 F추가
       # print(out,'p')
    else:out[-1] = (lst[lst_i])
        
    #print(out,'out')
    #out = out[::-1]

for ou in out:print(ou,end='')
# while n:
#     out += str(n%typ)
#     loc += 1
#     n = n//typ
# out = out[::-1] #뒤집기
# if int(out) > 10:
#     outf = str(out)[:-1]
#     print(lst[-1*int(outf)],loc)
#print(n)