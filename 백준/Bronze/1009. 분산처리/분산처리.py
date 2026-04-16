import sys

T = int(sys.stdin.readline());res=1
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    res = pow(a,b,10)
    if res:print(res)
    else:print(10)