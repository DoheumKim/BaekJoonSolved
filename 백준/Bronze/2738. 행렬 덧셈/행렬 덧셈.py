N,M = map(int, input().split())
matrix=[];matrix2=[]
for i in range(N):matrix.append(list(map(int,input().split())))
for i in range(N):matrix2.append(list(map(int,input().split())))
for j in range(N):
    for j2 in range(M):print(matrix[j][j2]+matrix2[j][j2],end=' ')
    print()