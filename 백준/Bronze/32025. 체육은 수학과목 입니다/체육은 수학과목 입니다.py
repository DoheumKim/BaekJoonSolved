import sys

H = int(sys.stdin.readline())
W = int(sys.stdin.readline())
print(int(H/2*100) if H<=W else int(W/2*100))