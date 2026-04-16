import sys
N=sys.stdin.readline()
N=int(N)
if 1<=N<=100:
    for a in range(1,N+1):
        print(' '*(N-a)+'*'*a)