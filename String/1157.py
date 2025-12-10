# https://www.acmicpc.net/problem/1157

# chr(65) == 'A'
# chr(90) == 'Z'

A_Z = (chr(i) for i in range(65,91))    # == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
A_Z = "".join(A_Z)  # == 'ABCDEFGHIJKLMNOPQRSTUVWXY'

input_info = input()
input_info = list(input_info.upper())

out = dict(zip(A_Z,list(map(int,'0'*26))))  # key값이 'A'~'Z'이고 모든 value값은 0인 딕셔너리
maximum = []
output = ''

 
for i in range(65,91): # a~z까지 반복

    out[chr(i)] = input_info.count(chr(i))  #input_info안에 A~Z가 있는지 확인    # input_infp[0~ -1]까지 중에 A가 있으면 out['A'] = A의 수
    maximum = ([k for k,v in out.items() if max(out.values()) == v])    # maximum에 A~Z중 가장 많이 나온 값 추가
    if len(maximum) > 1:    # A~Z중 가장 많이 나온 값이 2개이상일때 output = '?'
        output = '?'
    else:
        output = maximum[0] # output = A~Z중 가장 많이 나온 값 
    
print(output)

