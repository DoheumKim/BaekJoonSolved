out=''
N,X= input().split()
A = input().split()
if len(A) == int(N):
    for i in range(int(N)):
        if int(A[i]) < int(X):
            out += A[i]+' '
print(out[:-1])