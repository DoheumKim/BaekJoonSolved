A = int(input())
B = int(input())
C = int(input())
cc = [0,0,0,0,0,0,0,0,0,0]


D = str(A*B*C)
for i in range(len(D)):
    if '0' in D[i]:
        cc[0] +=1
    if '1' in D[i]:
        cc[1] +=1
    if '2' in D[i]:
        cc[2] +=1
    if '3' in D[i]:
        cc[3] +=1
    if '4' in D[i]:
        cc[4] +=1
    if '5' in D[i]:
        cc[5] +=1
    if '6' in D[i]:
        cc[6] +=1
    if '7' in D[i]:
        cc[7] +=1
    if '8' in D[i]:
        cc[8] +=1
    if '9' in D[i]:
        cc[9] +=1
for i in range(len(cc)):
    print(int(cc[i]))