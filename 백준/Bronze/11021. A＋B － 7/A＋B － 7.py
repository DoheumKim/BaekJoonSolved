import sys
T=int(input())
A,B= map(int,sys.stdin.readline().split())
x=1
print(f"Case #{x}: {A+B}")
if T<=1000000 and 1<=A<=1000 and 1<=B<=1000:
    for a in range(T-1):
        A,B= map(int,sys.stdin.readline().split())
        x+=1
        print(f"Case #{x}: {A+B}")